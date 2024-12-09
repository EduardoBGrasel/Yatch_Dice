from PySide6.QtWidgets import QMainWindow, QMessageBox, QTextBrowser, QPushButton, QLabel, QInputDialog
from PySide6.QtGui import QPixmap, QAction
from PySide6.QtCore import Qt, QEvent, QObject, QGenericArgument
from window import Ui_MainWindow
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from PySide6.QtCore import QMetaObject, Signal, Slot
from dominio_da_solucao.Tabuleiro import Tabuleiro
import sys
import re
from random import randint

class PlayerInterface(QMainWindow, Ui_MainWindow, DogPlayerInterface):
    received_start_signal = Signal(str)
    update_category_signal = Signal(str, int)  # sinal que passa o nome do botão e os pontos
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tabuleiro = Tabuleiro()
        self.received_start_signal.connect(self.show_message)
        self.update_category_signal.connect(self.atualiza_categoria)
        # Definindo o título da janela
        self.setWindowTitle("Jogo")

        # Criando a barra de menu
        menu_bar = self.menuBar()

        # Adicionando o menu principal "Jogo" na barra de menu
        jogo_menu = menu_bar.addMenu("Jogo")

        # Criando a ação "Iniciar Partida"
        iniciar_acao = QAction("Iniciar Partida", self)
        iniciar_acao.triggered.connect(self.start_match)  # Conectando a ação ao método iniciar_partida

        # Adicionando a ação ao menu "Jogo"
        jogo_menu.addAction(iniciar_acao)
        self.dados_interface = list()

        player_name, _ = QInputDialog.getText(None, "Nome do Jogador", "Digite seu nome:")
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        QMessageBox.about(self, "DogActor", f"{message}")
        self.setupUi(self)

        # lista para os labels dos dados
        self.dados_interface.append(self.dado_1)
        self.dados_interface.append(self.dado_2)
        self.dados_interface.append(self.dado_3)
        self.dados_interface.append(self.dado_4)
        self.dados_interface.append(self.dado_5)
        self.dado_map = {self.dado_1: 1, self.dado_2: 2, self.dado_3: 3, self.dado_4: 4, self.dado_5: 5}
        for dado in self.dados_interface:
            dado.setVisible(False)
            dado.installEventFilter(self)  # Instala o filtro de eventos em cada QLabel

        for button in self.findChildren(QPushButton):
            # Conectar o sinal clicked() de cada botão ao slot Category_points_button
            button.clicked.connect(self.escolher_categoria)

        # conectar o sinal clicked com seu slot
        #self.Selecionar_dados.clicked.connect(self.Seleciona_dados)
        self.Jogar_dados.clicked.connect(self.Joga_dados)
    
    def escolher_categoria(self):
        # Obter o botão que enviou o sinal (foi clicado)
        button = self.sender()
        # Recuperar o nome do botão
        if '1' in button.objectName() and self.tabuleiro.get_match_status() == 4:
            for box in self.findChildren(QTextBrowser):
                if box.objectName().replace('_value', "") == button.objectName().replace('_btn', ""):
                    button.hide()
                    move_to_send = self.tabuleiro.escolher_categoria(button.objectName())
                    points = move_to_send["pontuacao"]
                    box.setText(str(points))
                    for dado in self.dados_interface:
                        dado.setVisible(False)
                    #self.player_points[0] += points
                    #self.Player_1_label.setText(f"Player_1: {self.player_points[0]}")
                    game_state = self.tabuleiro.get_status()
                    self.atualiza_mensagem(game_state)
                    self.dog_server_interface.send_move(move_to_send)

    
    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        # Verifica se o evento ocorreu em um QLabel e se é um clique do mouse
        if obj in self.dados_interface and event.type() == QEvent.MouseButtonPress:
            self.Seleciona_Dado(obj)  # Chama o método para tratar o clique
            return True  # Indica que o evento foi tratado
        return super().eventFilter(obj, event)

    def Seleciona_Dado(self, dado: QLabel):
        match_status = self.tabuleiro.get_match_status()
        index = self.dado_map[dado] - 1 # REFERENTE AO LABEL DA INTERFACE
        move_to_send = {}
        if match_status == 4 or match_status == 3:
            # Verifica se o dado já está destacado
            if "border: 3px solid red;" in dado.styleSheet():
                # Remove o destaque (borda vermelha)
                move_to_send = self.tabuleiro.dado_selecionado(index, "remove")
                dado.setStyleSheet("")
            else:
                # Adiciona o destaque (borda vermelha)
                move_to_send = self.tabuleiro.dado_selecionado(index, "add")
                dado.setStyleSheet("border: 3px solid red;")
        self.dog_server_interface.send_move(move_to_send)


    def Joga_dados(self):
        match_status = self.tabuleiro.get_match_status()
        if (match_status == 3 or match_status == 4):
            move_to_send = self.tabuleiro.jogar_dados()
            if move_to_send == 1:
                QMessageBox.about(self, "DogActor", "Tentativas máximas, escolha categoria")
                return
            self.atualiza_dados_jogados(move_to_send["dados"])
            if (bool(move_to_send)):
                self.dog_server_interface.send_move(move_to_send)

    
    def start_match(self):
        match_status = self.tabuleiro.get_match_status()
        if match_status == 1:
            start_status = self.dog_server_interface.start_match(2)
            code = start_status.get_code()
            message = start_status.get_message()
            if code == "0" or code == "1":
                QMessageBox.about(self, "DogActor", f"{message}")
            else:
                players = start_status.get_players()
                local_player_id = start_status.get_local_id()
                self.tabuleiro.start_match(players, local_player_id)
                game_state = self.tabuleiro.get_status()
                self.atualiza_mensagem(game_state)
                QMessageBox.about(self, "DogActor", f"{start_status.get_message()}")
    

    @Slot(str)
    def show_message(self, message):
        self.status_label.setText(message)  # Adicione QLabel ao layout da interface

    def receive_start(self, start_status):
        players = start_status.get_players()
        local_player_id = start_status.get_local_id()
        self.tabuleiro.start_match(players, local_player_id)
        game_state = self.tabuleiro.get_status()
        self.atualiza_mensagem(game_state)
    
    def receive_withdrawal_notification(self):
        self.tabuleiro.receive_withdrawal_notification()
        game_state = self.tabuleiro.get_status()
        self.atualiza_mensagem(game_state)

    def atualiza_mensagem(self, game_state):
        self.show_message(game_state.get_message())
        #QMessageBox.about(self, "DogActor", f"{game_state.get_message()}")
    
    def atualiza_dados_jogados(self, dados):
        for index in range(len(dados)):
            pixmap = QPixmap(f"dados_img/{dados[index]['number']}.png")
            pixmap = pixmap.scaled(101, 101)
            self.dados_interface[index].setPixmap(pixmap)
            # Remove a borda vermelha após rejogar
            self.dados_interface[index].setStyleSheet("")  # Remove a borda
            status = self.tabuleiro.get_status()
            self.atualiza_mensagem(status)

        # Torna todos os dados visíveis (apenas se eles foram jogados)
        for dado_interface in self.dados_interface:
            dado_interface.setVisible(True)
    
    def atualiza_dados_selecionados(self, index, destaque):
        dado = self.dados_interface[index]
        if not destaque:
            dado.setStyleSheet("")
        else:
            dado.setStyleSheet("border: 3px solid red;")
    
    def atualiza_categoria(self, button_name, points):
        # Encontrar o botão na interface pelo nome
        button_name = button_name.replace("_btn_1", "_btn_2")
        button = self.findChild(QPushButton, button_name)  # Substitua QPushButton pelo tipo correto, se necessário
        button.hide()  # Esconde o botão
        label_name = button_name.replace("_btn_2", "_value_2")
        label = self.findChild(QTextBrowser, label_name)
        points = str(points)
        label.setText(points)
        for dado in self.dados_interface:
            dado.setVisible(False)
        game_state = self.tabuleiro.get_status()
        self.atualiza_mensagem(game_state)

    
    def receive_move(self, a_move):
        if a_move["type"] == "dados_jogados":
            dados = a_move["dados"]
            self.atualiza_dados_jogados(dados)
        elif a_move["type"] == "dado_selecionado":
            index = a_move["index"]
            destaque = a_move["destaque"]
            self.atualiza_dados_selecionados(index, destaque)
        elif a_move["type"] == "categoria":
            self.tabuleiro.recieve_category(a_move)
            pontuacao = a_move["pontuacao"]
            button = a_move["category"]
            self.update_category_signal.emit(button, pontuacao)
            