from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog

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
import file_handling
import styles

class FunctionsInCommon():
    def __init__(self) -> None:
        pass

    def able_disable_buttons(self, button, able:bool,  stylesheet):
        if able:
            button.setEnabled(True)
            button.setStyleSheet(stylesheet)
        else:
            button.setEnabled(False)
            button.setStyleSheet(stylesheet)



    def show_message_box(self, icon, title, message, parent=None, ok_and_cancel=False):
        """
        Exibe uma caixa de mensagem, definindo parâmetros de hierarquia, ícone, título e texto.
        Por fim, define o estilo da caixa com comandos QSS
        """
        msg_box = QMessageBox(parent)
        msg_box.setIcon(icon)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        font = QFont("Candara", 14)

        if ok_and_cancel:
            msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        msg_box.setFont(font)
        msg_box.setStyleSheet(styles.dark_messagebox_stylesheet)
        msg_box.exec()

    def validate_email(self, email):
        """
        Define uma expressão regular para validar o formato do e-mail digitado pelo usuário,
        e verifica se o e-mail corresponde a esse padrão estabelecido.

        Se valido retorna True, caso contrátio retorna False.
        """
        standard = r'^[\w]+[\.\w-]*@[\w-]+\.[a-zA-Z]{2,}$'

        if re.match(standard, email):
            return True
        else:
            self.false = False
            return self.false


class Login(QWidget, Ui_login, FunctionsInCommon):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")

        # *--EVENTOS DA TELA DE LOGIN--*
        self.btn_entre.clicked.connect(self.validate_login_data)
        self.password_lineEdit.returnPressed.connect(self.validate_login_data)

        self.btn_cadastre.clicked.connect(self.open_signup_window)

        self.forget_password_pushButton.clicked.connect(self.open_forget_password_window)

    def open_signup_window(self):
        # ABRE A TELA DE CADASTRO
        self.signup_window = SignUp()
        self.signup_window.show()
        self.close()

    def validate_login_data(self):
        # VALIDA SE OS DADOS DIGITADOS ESTÃO NO BANCO DE DADOS. SE SIM, REALIZA O LOGIN. SE NÃO, EXIBE MENSAGEM DE ERRO.
        db = DataBase()
        db.connect()
        authenticated = db.already_exists(self.username_lineEdit.text().upper(), self.password_lineEdit.text())

        # SE SIM
        if authenticated:
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()

        # SE NÃO
        else:
            self.show_message_box(QMessageBox.Warning, "Erro", "Login ou senha inválidos", self)

        db.close_connection()

    def open_forget_password_window(self):
        self.forget_w = ForgetPassword()
        self.forget_w.show()


class SignUp(QWidget, Ui_signup, FunctionsInCommon):
    def __init__(self) -> None:
        super(SignUp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadastro")

        # *--EVENTOS DA TELA DE CADASTRO--*
        self.btn_cadastrar.clicked.connect(self.collect_user_data)
        self.password_repeat_lineEdit.returnPressed.connect(self.collect_user_data)
        self.btn_return.clicked.connect(self.open_login)

    def collect_user_data(self):
        """
        Insere usuários no banco de dados.
        Porém antes são realizadas uma série de validações a fim de tratar os dados fornecidos pelo usuário.

        1° Valida se todos os campos estão preenchidos.
        2° Valida se o e-mail é válido, de acordo com a função validate_email.
        3° Valida se as senhas digitadas são iguais.

        Após esse processo ele estabelece uma conexão com o banco de dados para realizar a 4° validação.

        4º Valida se os dados já existem no banco de dados através da função db.already_exists

        Se passar pelas validações ele envia o código de verificação para o e-mail fornecido
        e abre a tela de verificação.
        """

        if not self.username_lineEdit.text() or not self.email_lineEdit.text() or not self.password_lineEdit.text():
            self.show_message_box(QMessageBox.Warning, "Erro", "Todos os campos são obrigatórios", self)
            return None

        if not self.validate_email(self.email_lineEdit.text()):
            self.show_message_box(QMessageBox.Warning, "Erro", "E-mail inválido", self)

            return None

        if self.password_lineEdit.text() != self.password_repeat_lineEdit.text():
            self.show_message_box(QMessageBox.Warning, "Erro", "As senhas digitadas são diferentes", self)
            return None

        user = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        email = self.email_lineEdit.text()

        db = DataBase()
        db.connect()

        if db.already_exists(user, password, email):
            self.show_message_box(QMessageBox.Warning, "Erro", "E-mail ou usuário já cadastrado", self)
            db.close_connection()
            return None

        db.close_connection()

        verification_code = send_verify_code(user, email)

        self.verify_window = VerificationCode(verification_code, user, email, password)
        self.verify_window.show()

        self.username_lineEdit.setText("")
        self.password_lineEdit.setText("")
        self.password_repeat_lineEdit.setText("")
        self.email_lineEdit.setText("")

    def open_login(self):
        # ABRE A TELA DE LOGIN
        self.w = Login()
        self.w.show()
        self.close()


class ForgetPassword(QWidget, Ui_forgetpassword, FunctionsInCommon):
    def __init__(self) -> None:
        super(ForgetPassword, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Redefinição de senha")

        # *--EVENTOS DA TELA DE REDEFINIÇÃO DE SENHA--*
        self.btn_redefine.clicked.connect(self.redefine_password)
        self.repeat_password_lineEdit.returnPressed.connect(self.redefine_password)

    def redefine_password(self):
        """
        Redefine a senha do usuário.
        Porém antes são realizadas uma série de validações a fim de tratar os dados fornecidos pelo usuário.

        1° Valida se todos os campos estão preenchidos.
        2° Valida se o e-mail é válido, de acordo com a função validate_email.
        3° Valida se as senhas digitadas são iguais.

        Após esse processo, é estabelecida uma conexão com o banco de dados para realizar a 4° validação.

        4° Valida se o e-mail digitado existe no banco de dados através da função db.search_email.

        Se passar pelas validações ele envia o código de verificação para o e-mail fornecido
        e abre a tela de verificação.
        """

        if not self.email_lineEdit.text() or not self.password_lineEdit.text():
            self.show_message_box(QMessageBox.Warning, "Erro", "Todos os campos são obrigatórios", self)
            return None

        if not self.validate_email(self.email_lineEdit.text()):
            self.show_message_box(QMessageBox.Warning, "Erro", "E-mail inválido", self)
            return None

        if self.password_lineEdit.text() != self.repeat_password_lineEdit.text():
            self.show_message_box(QMessageBox.Warning, "Erro", "As senhas digitadas são diferentes", self)
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
            self.show_message_box(QMessageBox.Warning, "Erro", "Esse e-mail não está cadastrado", self)

        db.close_connection()


class VerificationCode(QWidget, Ui_verificationCode, FunctionsInCommon):
    def __init__(self, verification_code, user="", email="", password="", redefine_password=False) -> None:
        super(VerificationCode, self).__init__()
        self.verification_code = verification_code
        self.user = user
        self.email = email
        self.password = password
        self.redefine_password = redefine_password

        self.setupUi(self)
        self.setWindowTitle("Verificação de e-mail")

        # *--EVENTOS DA TELA DO CÓDIGO DE VERIFICAÇÃO-*
        self.code_lineEdit.textChanged.connect(self.to_upper)
        self.btn_verify.clicked.connect(self.verify)
        self.code_lineEdit.returnPressed.connect(self.verify)
        self.btn_resend.clicked.connect(self.resend_verify_code)

    def to_upper(self):
        # CONVERTE O CARACTERE DIGITADO PARA MAIÚSCULO
        if self.code_lineEdit.text().isupper():
            return
        self.code_lineEdit.setText(self.code_lineEdit.text().upper())

    def resend_verify_code(self):
        # REENVIA O CÓDIGO DE VERIFICAÇÃO
        self.verification_code = send_verify_code(self.user, self.email)

    def verify(self):
        """
        Valida o código de verificação enviado ao e-mail fornecido e realiza a devida operação.

        A classe possúi o parâmetro "redefine_password", que quando True realiza a redefinição da senha através
        da função db.update_password.

        Quando o parâmetro "redefine_password" for False,
        ele insere o usuário no banco de dados através da função db.insert_user.
        """
        if self.redefine_password:
            if self.code_lineEdit.text() == self.verification_code:
                db = DataBase()
                db.connect()
                db.update_password(self.user, self.password)
                db.close_connection()

                self.show_message_box(QMessageBox.Information, "Sucesso", "Redefinição de senha realizada com sucesso!",
                                      self)

                self.close()

            else:
                self.show_message_box(QMessageBox.Warning, "Erro", "Código de verificação inválido", self)


        else:
            if self.code_lineEdit.text() == self.verification_code:
                db = DataBase()
                db.connect()

                db.insert_user(self.user.upper(), self.email, self.password)

                db.close_connection()

                self.show_message_box(QMessageBox.Information, "Sucesso", "Cadastro realizado com sucesso!", self)

                self.close()

            else:
                self.show_message_box(QMessageBox.Warning, "Erro", "Código de verificação inválido", self)


class MainWindow(QMainWindow, Ui_MainWindow, FunctionsInCommon):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Appostman")
        self.recipients_filename = ''

        # *--EVENTOS DA TELA PRINCIPAL--*
        self.btn_toggle.clicked.connect(self.left_menu)

        # *--EVENTOS PÁGINA DESTINATÁRIOS--*
        self.btn_search.clicked.connect(self.open_file_dialog)
        self.btn_validate.clicked.connect(self.validate_and_get_contacts)

        # # *--PÁGINAS DA TELA PRINCIPAL--*
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_home))
        self.btn_configurations.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_configurations))
        self.btn_recipients.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_recipients))
        self.btn_messages.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_messages))
        self.btn_help.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_help))
        self.btn_about.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_about))

    # *--*---*FUNÇÕES PÁGINA DESTINATÁRIOS*---*--*
    def open_file_dialog(self):
        """
        Abre o explorador de arquivos a fim de receber um arquivo .csv,
        ao selecionar o arquivo a função passa o caminho deste arquivo
        para o atributo recipients_filename da classe MainWindow, e também ativa o botão "Validar" (btn_validate).

        Caso o usuário abra o explorador de arquivos e feche sem selecionar nada o botão "Validar" é desativado.
        """
        file_name = QFileDialog.getOpenFileName(self, "Selecione o Arquivo",
                                                "", "Valores Separados por Vírgula (*.csv)")

        if file_name[0]:
            self.label_file_name.setText(file_name[0])

            self.able_disable_buttons(self.btn_validate, True, styles.light_blue_button_stylesheet)

            self.recipients_filename = file_name[0]
        else:
            self.label_file_name.setText("Selecione um arquivo")
            self.able_disable_buttons(self.btn_validate, False, styles.gray_button_stylesheet)

        self.able_disable_buttons(self.btn_signup_recipients, False, styles.gray_button_stylesheet)

    def validate_and_get_contacts(self):
        """
        Extraí os nomes e e-mails através da função get_contacts do módulo file_handling.

        Para realizar a validação é utilizado o Try - Except capturando a excessão ValueError, que significa que a
        função get_contacts encontrou um email inválido no arquivo. Exibindo assim uma mensagem de erro ao usuário.

        Caso passe pela validação exibe a quatindade de contatos válidos para inserção no banco de dados, e por fim
        ativa o botão "Cadastrar" (self.btn_signup_recipients)

        *Antes de exibir a mensagem de sucesso, valida se a quantidade de nomes extraídos é igual a de e-mails
        a fim de evitar problemas na inserção do banco de dados.
        """
        try:
            names, emails = file_handling.get_contacts(self.recipients_filename)

            if len(names) == len(emails):
                success_message = f"Arquivo válido.\nForam encontrados {len(emails)} contatos válidos."
                self.show_message_box(QMessageBox.Information, "Sucesso", success_message, self)

            self.able_disable_buttons(self.btn_signup_recipients, True, styles.green_button_stylesheet)

        except(IndexError):
            self.show_message_box(QMessageBox.Warning, "Erro", "Arquivo inválido. "
                                                               "Consulte o menu AJUDA "
                                                               "para uma explicação do leiaute do arquivo.", self)
        except(ValueError):
            error = file_handling.get_contacts(self.recipients_filename)

            self.show_message_box(QMessageBox.Warning, "Erro", error, self)

    def left_menu(self):
        #  ABRE O MENU LATERAL ESQUERDO DE FORMA ANIMADA
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
    # BLOCO DE CÓDIGO DESTINADO A TESTES, INICIA A TELA ESPECÍFICADA.
    app = QApplication(sys.argv)
    # window = Login()
    window = MainWindow()
    window.show()
    # window = VerificationCode()
    # window.show()
    app.exec()
