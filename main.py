from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
from ui_signup import Ui_Signup
from database import DataBase

import sys


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tries = 0
        self.setupUi(self)
        self.setWindowTitle("Appostman Login")

        # eventos tela de login
        self.btn_entre.clicked.connect(self.login_auth)
        self.password_lineEdit.returnPressed.connect(self.login_auth)
        self.btn_cadastre.clicked.connect(self.open_signup)

    def open_signup(self): # abre a tela de cadastro
        self.w = SignUp()
        self.w.show()
        self.close()

    def login_auth(self): # valida os dados digitados no banco de dados. Se existente, realiza o login
        self.users = DataBase()
        self.users.connect()
        authenticated = self.users.auth(self.username_lineEdit.text().upper(), self.password_lineEdit.text())

        print(authenticated)

        if authenticated:
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            if self.tries < 3: # caso dados incorretos, inicia contagem de tentativas !!!AINDA NÃO FUNCIONANDO!!!
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro")
                msg.setText(f'Login ou senha inválidos. Após três tentativas sua conta será bloqueada.\n\n'
                            f'Tentativa: {self.tries + 1}/3')
                msg.exec()
                self.tries += 1
            if self.tries == 3:
                # bloquear o usuário posteriormente no banco de dados
                self.users.close_connection()
                sys.exit(0)


class SignUp(QWidget, Ui_Signup):
    def __init__(self) -> None:
        super(SignUp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadastro")

        # eventos tela de cadastro
        self.btn_cadastrar.clicked.connect(self.insert_user)
        self.password_repeat_lineEdit.returnPressed.connect(self.insert_user)
        self.btn_return.clicked.connect(self.open_login)

    def insert_user(self): # insere usuários no banco de dados
        if self.password_lineEdit.text() != self.password_repeat_lineEdit.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("As senhas digitadas são diferentes")
            msg.exec()
            return None

        user = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        email = self.email_lineEdit.text()

        db = DataBase()
        db.connect()

        insertion = db.insert_user(user, email, password)
        if insertion == 'already_exists':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("Email ou usuário já cadastrado")
            msg.exec()
            db.close_connection()
            return None

        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Sucesso")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec()

        self.username_lineEdit.setText("")
        self.password_lineEdit.setText("")
        self.password_repeat_lineEdit.setText("")
        self.email_lineEdit.setText("")

    def open_login(self): # abre tela de login
        self.w = Login()
        self.w.show()
        self.close()


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
