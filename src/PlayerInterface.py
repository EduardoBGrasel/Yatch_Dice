from PySide6.QtWidgets import QMainWindow, QMessageBox, QTextBrowser, QPushButton, QLabel, QInputDialog
from PySide6.QtGui import QPixmap, QAction
from PySide6.QtCore import Qt, QEvent, QObject
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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tabuleiro = Tabuleiro()
        self.received_start_signal.connect(self.show_message)
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

        self.dados_jogados = False
        self.player_turn = 1
        #self.verifica_dados = False
        self.verifica_selecionado = False
        self.dados_interface = list()
        self.max_jogadas = 4
        self.jogadas_atuais = 0
        self.player_points = [0, 0]
        
        #estado_jogo = self.tabuleiro.get_status()
        #self.atualiza_interface(estado_jogo)

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

        # conectar o sinal clicked com seu slot
        #self.Selecionar_dados.clicked.connect(self.Seleciona_dados)
        self.Jogar_dados.clicked.connect(self.Joga_dados)
    
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
            if "border: 1px solid red;" in dado.styleSheet():
                # Remove o destaque (borda vermelha)
                move_to_send = self.tabuleiro.dado_selecionado(index, "remove")
                dado.setStyleSheet("")
            else:
                # Adiciona o destaque (borda vermelha)
                move_to_send = self.tabuleiro.dado_selecionado(index, "add")
                dado.setStyleSheet("border: 1px solid red;")
        self.dog_server_interface.send_move(move_to_send)


    def Joga_dados(self):
        match_status = self.tabuleiro.get_match_status()
        if (match_status == 3 or match_status == 4):
            move_to_send = self.tabuleiro.jogar_dados()
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
                self.atualiza_interface(game_state)
                QMessageBox.about(self, "DogActor", f"{start_status.get_message()}")
    

    @Slot(str)
    def show_message(self, message):
        self.status_label.setText(message)  # Adicione QLabel ao layout da interface

    def receive_start(self, start_status):
        players = start_status.get_players()
        local_player_id = start_status.get_local_id()
        self.tabuleiro.start_match(players, local_player_id)
        game_state = self.tabuleiro.get_status()
        self.atualiza_interface(game_state)
    
    def receive_withdrawal_notification(self):
        self.tabuleiro.receive_withdrawal_notification()
        game_state = self.tabuleiro.get_status()
        self.atualiza_interface(game_state)

    def atualiza_interface(self, game_state):
        self.dados_jogados = game_state.get_lista_dados()
        self.dados_selecionados = game_state.get_lista_selecionados()
        self.show_message(game_state.get_message())
        #QMessageBox.about(self, "DogActor", f"{game_state.get_message()}")
    
    def atualiza_dados_jogados(self, dados):
        for index in range(len(dados)):
            pixmap = QPixmap(f"dados_img/{dados[index]['number']}.png")
            pixmap = pixmap.scaled(101, 101)
            self.dados_interface[index].setPixmap(pixmap)

            # Remove a borda vermelha após rejogar
            self.dados_interface[index].setStyleSheet("")  # Remove a borda

        # Torna todos os dados visíveis (apenas se eles foram jogados)
        for dado_interface in self.dados_interface:
            dado_interface.setVisible(True)
    
    def atualiza_dados_selecionados(self, index, destaque):
        dado = self.dados_interface[index]
        if not destaque:
            dado.setStyleSheet("")
        else:
            dado.setStyleSheet("border: 1px solid red;")

    
    def receive_move(self, a_move):
        if a_move["type"] == "dados_jogados":
            dados = a_move["dados"]
            self.atualiza_dados_jogados(dados)
        elif a_move["type"] == "dado_selecionado":
            index = a_move["index"]
            destaque = a_move["destaque"]
            self.atualiza_dados_selecionados(index, destaque)



    # def Seleciona_dados(self):
    #     if self.dados_jogados:
    #         QMessageBox.about(main_window, "SUCESSO", "Selecionar dados")
    #         self.verifica_selecionado = True
    #         self.dados_jogados = False
    #     else:
    #         QMessageBox.about(main_window, "ERRO", "JOGUE OS DADOS PRIMEIRO")
