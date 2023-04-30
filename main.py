from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox

from PySide6.QtCore import QPropertyAnimation, QEasingCurve

from PySide6.QtGui import QFont

from ui_login import Ui_login
from ui_main import Ui_MainWindow
from ui_signup import Ui_signup
from ui_verificationCode import Ui_verificationCode
from ui_forgetPassword import Ui_forgetpassword

from database import DataBase

from smtp import send_verify_code

import sys

import re



def show_message_box(icon, title, message, parent=None, ok_and_cancel=False): # EXIBE UMA CAIXA DE MENSAGEM
    msg_box = QMessageBox(parent)
    msg_box.setIcon(icon)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)

    font = QFont("Candara", 14)

    if ok_and_cancel:
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    msg_box.setFont(font)
    msg_box.setStyleSheet("""
        QMessageBox {
            background-color: rgb(49, 49, 49);
            color: white;
        }
        QPushButton[class='QPushButton'] {
            background-color: gray;
            color: white;
        }
        QLabel {
            background-color: rgb(49, 49, 49);
            color: white;
        }
    """)
    msg_box.exec()





class Login(QWidget, Ui_login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Appostman Login")

        # *--EVENTOS DA TELA DE LOGIN--*
        self.btn_entre.clicked.connect(self.validate_login_data)
        self.password_lineEdit.returnPressed.connect(self.validate_login_data)

        self.btn_cadastre.clicked.connect(self.open_signup_window)

        self.forget_password_pushButton.clicked.connect(self.open_forget_password_window)

    def open_signup_window(self):  # ABRE A TELA DE CADASTRO
        self.signup_window = SignUp()
        self.signup_window.show()
        self.close()

    def validate_login_data(self):
        # VALIDA SE OS DADOS DIGITADOS ESTÃO NO BANCO DE DADOS. SE SIM, REALIZA O LOGIN. SE NÃO, EXIBE MENSAGEM DE ERRO.
        self.users = DataBase()
        self.users.connect()
        authenticated = self.users.already_exists(self.username_lineEdit.text().upper(), self.password_lineEdit.text())

        # SE SIM
        if authenticated:
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()

        # SE NÃO
        else:
            show_message_box(QMessageBox.Warning, "Erro", "Login ou senha inválidos", self)

    def open_forget_password_window(self):
        self.forget_w = ForgetPassword()
        self.forget_w.show()


class SignUp(QWidget, Ui_signup):
    def __init__(self) -> None:
        super(SignUp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadastro")

        # eventos tela de cadastro
        self.btn_cadastrar.clicked.connect(self.collect_user_data)
        self.password_repeat_lineEdit.returnPressed.connect(self.collect_user_data)
        self.btn_return.clicked.connect(self.open_login)

    def validar_email(self, email):
        # Define o padrão de expressão regular para verificar o formato do e-mail
        standard = r'^[\w]+[\.\w-]*@[\w-]+\.[a-zA-Z]{2,}$'

        # Verifica se o e-mail corresponde ao padrão
        if re.match(standard, email):
            return True
        else:
            self.false = False
            return self.false

    def collect_user_data(self):  # insere usuários no banco de dados

        if not self.username_lineEdit.text() or not self.email_lineEdit.text() or not self.password_lineEdit.text():

            show_message_box(QMessageBox.Warning, "Erro", "Todos os campos são obrigatórios", self)
            return None

        if not self.validar_email(self.email_lineEdit.text()):
            show_message_box(QMessageBox.Warning, "Erro", "E-mail inválido", self)

            return None

        if self.password_lineEdit.text() != self.password_repeat_lineEdit.text():
            show_message_box(QMessageBox.Warning, "Erro", "As senhas digitadas são diferentes", self)
            return None

        user = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        email = self.email_lineEdit.text()

        db = DataBase()
        db.connect()

        if db.already_exists(user, password, email):
            show_message_box(QMessageBox.Warning, "Erro", "E-mail ou usuário já cadastrado", self)
            db.close_connection()
            return None

        db.close_connection()

        verification_code = send_verify_code(self.username_lineEdit.text(), self.email_lineEdit.text())

        self.verify_window = VerificationCode(verification_code, user, email, password)
        self.verify_window.show()

        self.username_lineEdit.setText("")
        self.password_lineEdit.setText("")
        self.password_repeat_lineEdit.setText("")
        self.email_lineEdit.setText("")

    def open_login(self):  # abre tela de login
        self.w = Login()
        self.w.show()
        self.close()


class ForgetPassword(QWidget, Ui_forgetpassword):
    def __init__(self) -> None:
        super(ForgetPassword, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Redefinição de senha")

        # eventos tela de redefinição de senha
        self.btn_redefine.clicked.connect(self.redefine)
        self.repeat_password_lineEdit.returnPressed.connect(self.redefine)

    def validar_email(self, email):
        # Define o padrão de expressão regular para verificar o formato do e-mail
        standard = r'^[\w]+[\.\w-]*@[\w-]+\.[a-zA-Z]{2,}$'

        # Verifica se o e-mail corresponde ao padrão
        if re.match(standard, email):
            return True
        else:
            self.false = False
            return self.false

    def redefine(self):

        #  restrições para digitação do usuário ao pressionar o botão

        if not self.email_lineEdit.text() or not self.password_lineEdit.text():
            show_message_box(QMessageBox.Warning, "Erro", "Todos os campos são obrigatórios", self)
            return None

        if not self.validar_email(self.email_lineEdit.text()):
            show_message_box(QMessageBox.Warning, "Erro", "E-mail inválido", self)
            return None

        if self.password_lineEdit.text() != self.repeat_password_lineEdit.text():
            show_message_box(QMessageBox.Warning, "Erro", "As senhas digitadas são diferentes", self)
            return None

        db = DataBase()
        db.connect()

        user_data = db.search_email(self.email_lineEdit.text())
        if user_data:

            verification_code = send_verify_code(user_data[1], user_data[3])

            self.verify_window = VerificationCode(verification_code, password=self.password_lineEdit.text(),
                                                  redefine_password=True, user=user_data[1])
            self.verify_window.show()
            self.close()

        else:
            show_message_box(QMessageBox.Warning, "Erro", "Esse e-mail não está cadastrado", self)

        db.close_connection()


class VerificationCode(QWidget, Ui_verificationCode):
    def __init__(self, verification_code, user="", email="", password="", redefine_password=False) -> None:
        super(VerificationCode, self).__init__()
        self.verification_code = verification_code
        self.user = user
        self.email = email
        self.password = password
        self.redefine_password = redefine_password

        self.setupUi(self)
        self.setWindowTitle("Verificação de e-mail")

        # eventos tela de verificação de e-mail
        self.code_lineEdit.textChanged.connect(self.text_changed)
        self.btn_verify.clicked.connect(self.verify)
        self.code_lineEdit.returnPressed.connect(self.verify)

    def text_changed(self):  # verifica se o caractere digitado é maisculo, caso não seja, converte para maiúsculo
        if self.code_lineEdit.text().isupper():
            return
        self.code_lineEdit.setText(self.code_lineEdit.text().upper())

    def verify(self):

        if self.redefine_password:
            if self.code_lineEdit.text() == self.verification_code:
                db = DataBase()
                db.connect()
                db.update_password(self.user, self.password)
                db.close_connection()

                show_message_box(QMessageBox.Information, "Sucesso", "Redefinição de senha realizada com sucesso!", self)

                self.close()

            else:
                show_message_box(QMessageBox.Warning, "Erro", "Código de verificação inválido", self)


        else:
            if self.code_lineEdit.text() == self.verification_code:
                db = DataBase()
                db.connect()

                db.insert_user(self.user, self.email, self.password)

                db.close_connection()

                show_message_box(QMessageBox.Information, "Sucesso", "Cadastro realizado com sucesso!", self)

                self.close()

            else:
                show_message_box(QMessageBox.Warning, "Erro", "Código de verificação inválido", self)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Appostman")

        # eventos tela principal

        self.btn_toggle.clicked.connect(self.left_menu)

        # paginas
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_home))
        self.btn_configurations.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_configurations))
        self.btn_recipients.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_recipients))
        self.btn_messages.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_messages))
        self.btn_help.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_help))
        self.btn_about.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_about))

    def left_menu(self):

        width = self.left_container.width()

        if width == 0:
            newWidth = 250
        else:
            newWidth = 0

        self.animation = QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    # window = MainWindow()
    window.show()
    # window = VerificationCode()
    # window.show()
    app.exec()
