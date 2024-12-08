from PlayerInterface import PlayerInterface
from PySide6.QtWidgets import QApplication
import sys
from PySide6.QtGui import QFontDatabase, QFont

app = QApplication(sys.argv)
font_id = QFontDatabase.addApplicationFont("font/Arial.ttf")  # Caminho do arquivo de fonte
font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
font = QFont(font_family, 12)
app.setFont(font)
if 'main_window' not in globals():  # Garantir que não criamos outra instância
    main_window = PlayerInterface()
    main_window.show()
app.exec()