from PlayerInterface import PlayerInterface
from PySide6.QtWidgets import QApplication
import sys
app = QApplication(sys.argv)
if 'main_window' not in globals():  # Garantir que não criamos outra instância
    main_window = PlayerInterface()
    main_window.show()
app.exec()