from PlayerInterface import PlayerInterface
from PySide6.QtWidgets import QApplication
import sys
from PySide6.QtGui import QFont

app = QApplication(sys.argv)
font = QFont("Arial", 12)  # Usando uma fonte amplamente disponível
app.setFont(font)
if 'main_window' not in globals():  # Garantir que não criamos outra instância
    main_window = PlayerInterface()
    main_window.show()
app.exec()