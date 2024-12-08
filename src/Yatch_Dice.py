from PlayerInterface import PlayerInterface
from PySide6.QtWidgets import QApplication
import sys
from PySide6.QtGui import QFontDatabase, QFont

app = QApplication(sys.argv)
if 'main_window' not in globals():  # Garantir que não criamos outra instância
    main_window = PlayerInterface()
    main_window.show()
app.exec()