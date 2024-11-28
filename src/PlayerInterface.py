from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTextBrowser, QPushButton, QLabel, QInputDialog
from PySide6.QtGui import QPixmap, QAction
from PySide6.QtCore import Qt, QEvent
from window import Ui_MainWindow
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from PySide6.QtCore import QMetaObject, Signal, Slot

import sys
import re
from random import randint

class PlayerInterface(QMainWindow, Ui_MainWindow, DogPlayerInterface):
    received_start_signal = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
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
        self.dados = list()
        self.numeros_dados = [0] * 5
        self.max_jogadas = 4
        self.jogadas_atuais = 0
        self.player_points = [0, 0]
        self.setupUi(self)
        
        player_name, _ = QInputDialog.getText(None, "Nome do Jogador", "Digite seu nome:")
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        QMessageBox.about(self, "DogActor", f"{message}")

        self.dados.append(self.dado_1)
        self.dados.append(self.dado_2)
        self.dados.append(self.dado_3)
        self.dados.append(self.dado_4)
        self.dados.append(self.dado_5)
        self.dados_selecionados = [True, True, True, True, True]
        for dado in self.dados:
            dado.setVisible(False)

        # conectar o sinal clicked com seu slot
        #self.Selecionar_dados.clicked.connect(self.Seleciona_dados)
        self.Jogar_dados.clicked.connect(self.Joga_dados)

        for button in self.findChildren(QPushButton):
            # Conectar o sinal clicked() de cada botão ao slot Category_points_button
            button.clicked.connect(self.Category_points_button)
        
        for dado in self.dados:
            dado.setVisible(False)
            dado.installEventFilter(self)  # Instala o filtro de eventos em cada label
    
    def Category_points_button(self):
        # Obter o botão que enviou o sinal (foi clicado)
        button = self.sender()
        # Recuperar o nome do botão
        button_name = button.objectName()
        if '1' in button_name and self.player_turn == 1 and self.verifica_selecionado:
            button.hide()
            for box in self.findChildren(QTextBrowser):
                if box.objectName().replace('_value', "") == button.objectName().replace('_btn', ""):
                    points = (randint(1, 10))
                    box.setText(str(points))
                    self.player_turn = (self.player_turn % 2) + 1
                    self.verifica_selecionado = False
                    self.jogadas_atuais = 0
                    for dado in self.dados:
                        dado.setVisible(False)
                        self.dados_selecionados = [True, True, True, True, True]
                    self.player_points[0] += points
                    self.Player_1_label.setText(f"Player_1: {self.player_points[0]}")
                    return
                
        elif '2' in button_name and self.player_turn == 2 and self.verifica_selecionado:
            button.hide()
            for box in self.findChildren(QTextBrowser):
                if box.objectName().replace('_value', "") == button.objectName().replace('_btn', ""):
                    points = (randint(1, 10))
                    box.setText(str(points))
                    self.player_turn = (self.player_turn % 2) + 1
                    self.verifica_selecionado = False
                    self.jogadas_atuais = 0
                    for dado in self.dados:
                        dado.setVisible(False)
                        self.dados_selecionados = [True, True, True, True, True]
                    self.player_points[1] += points
                    self.Player_2_label.setText(f"Player_2: {self.player_points[1]}")
                    return
        if '1' in button_name or '2' in button_name:
            QMessageBox.about(main_window, "ERRO", f"Verifique se selecionou os dados e se você selecionou o campo certo jogador {self.player_turn}")

    def Joga_dados(self):
        if self.jogadas_atuais == self.max_jogadas:
            QMessageBox.about(self, "Maximo de jogadas", "selecione a categoria")
        else:
            QMessageBox.about(self, "SUCESSO", "Jogando dados")
            self.dados_jogados = True
            self.verifica_selecionado = True
            
            # Loop para rejogar apenas os dados selecionados
            for index, dado in enumerate(self.dados):
                if self.dados_selecionados[index]:  # Verifica se o dado está selecionado
                    i = randint(1, 6)
                    pixmap = QPixmap(f"dados_img/{i}.png")
                    pixmap = pixmap.scaled(101, 101)
                    dado.setPixmap(pixmap)

                    # Armazena o número do dado jogado
                    self.numeros_dados[index] = i  # Atualiza a lista com o número do dado

                    # Remove a borda vermelha após rejogar
                    dado.setStyleSheet("")  # Remove a borda
                    self.dados_selecionados[index] = False  # Marca como não selecionado

            # Torna todos os dados visíveis (apenas se eles foram jogados)
            for dado in self.dados:
                dado.setVisible(True)
            print(self.numeros_dados)
            self.jogadas_atuais += 1

    
    def eventFilter(self, source, event):
        # Verifica se o evento é um clique e se o nome da label segue o padrão "dado_x"
        if event.type() == QEvent.MouseButtonPress and re.match(r"dado_\d+", source.objectName()):
            index = int(source.objectName().split('_')[1]) - 1  # Obtém o índice do dado (0 a 4)
            current_style = source.styleSheet()
            if "border: 1px solid red;" in current_style:
                source.setStyleSheet("")  # Remove a borda vermelha
                self.dados_selecionados[index] = False  # Marca como não selecionado
            else:
                source.setStyleSheet("border: 1px solid red;")  # Aplica a borda vermelha
                self.dados_selecionados[index] = True  # Marca como selecionado
            return True  # Indica que o evento foi processado
        return super(PlayerInterface, self).eventFilter(source, event)
    
    def start_match(self):
        start_status = self.dog_server_interface.start_match(2)
        message = start_status.get_message()
        QMessageBox.about(self, "DogActor", f"{message}")

    @Slot(str)
    def show_message(self, message):
        QMessageBox.about(self, "DogActor", f"{message}")

    def receive_start(self, start_status):
        message = start_status.get_message()
        self.received_start_signal.emit(message)



    # def Seleciona_dados(self):
    #     if self.dados_jogados:
    #         QMessageBox.about(main_window, "SUCESSO", "Selecionar dados")
    #         self.verifica_selecionado = True
    #         self.dados_jogados = False
    #     else:
    #         QMessageBox.about(main_window, "ERRO", "JOGUE OS DADOS PRIMEIRO")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = PlayerInterface()
    main_window.show()
    app.exec()