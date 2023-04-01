from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from ui_login import Ui_Login
from ui_main import Ui_MainWindow

import sys

class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Appostman Login")

        self.btn_entre.clicked.connect(self.open_system)
        self.password_lineEdit.returnPressed.connect(self.open_system)

    def open_system(self):
        if self.password_lineEdit.text() == "Warisadrug1":
            self.w = MainWindow()
            self.w.show()
            self.close()

        else:
            print("Senha inválida")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Appostman")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()

    app.exec()
