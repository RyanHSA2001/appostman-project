from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QMessageBox,
    QFileDialog, QHeaderView, QTableWidgetItem
)

from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt

from PySide6.QtGui import QFont, QColor

from ui_login import Ui_login
from ui_main import Ui_MainWindow
from ui_signup import Ui_signup
from ui_verificationCode import Ui_verificationCode
from ui_forgetPassword import Ui_forgetpassword
from ui_registeredRecipients import Ui_RegisteredRecipients

from database import DataBase

from smtp import send_verify_code

import sys
import re
import file_handling
import styles


# noinspection PyUnresolvedReferences
class FunctionsInCommon:
    def __init__(self):
        pass

    @staticmethod
    def able_disable_buttons(button, able: bool, stylesheet):
        """
        Habilita ou desabilita um botão e define seu estilo.
        """
        button.setEnabled(able)
        button.setStyleSheet(stylesheet)

    @staticmethod
    def show_message_box(icon, title, message, parent=None, ok_and_cancel=False):
        """
        Exibe uma caixa de mensagem com ícone, título e texto personalizados.
        Permite definir se a caixa terá botões "Ok" e "Cancelar".
        Aplica um estilo de caixa de mensagem personalizado.
        """
        msg_box = QMessageBox(parent)
        msg_box.setIcon(icon)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        font = QFont("Candara", 14)
        msg_box.setFont(font)

        if ok_and_cancel:
            msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        msg_box.setStyleSheet(styles.dark_messagebox_stylesheet)
        msg_box.exec()

    @staticmethod
    def validate_email(email):
        """
        Valida o formato do e-mail digitado pelo usuário.
        Retorna True se válido, False caso contrário.
        """
        standard = r'^[\w]+[\.\w-]*@[\w-]+\.[a-zA-Z]{2,}$'

        if re.match(standard, email):
            return True
        else:
            return False


# noinspection PyUnresolvedReferences
class Login(QWidget, Ui_login, FunctionsInCommon):
    def __init__(self) -> None:
        super(Login, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Login")

        # Conecte os eventos da tela de login aos métodos correspondentes
        self.btn_entre.clicked.connect(self.validate_login_data)
        self.password_lineEdit.returnPressed.connect(self.validate_login_data)

        self.btn_cadastre.clicked.connect(self.open_signup_window)

        self.forget_password_pushButton.clicked.connect(self.open_forget_password_window)

    def open_signup_window(self):
        # Abre a tela de cadastro e fecha a janela de login
        self.signup_window = SignUp()
        self.signup_window.show()
        self.close()

    def validate_login_data(self):
        # Valida se os dados digitados estão no banco de dados. Se sim, realiza o login. Se não, exibe uma mensagem de erro.
        db = DataBase()  # Crie uma instância da classe de banco de dados
        db.connect()
        authenticated = db.already_exists(self.username_lineEdit.text().upper(), self.password_lineEdit.text())

        # Se autenticado
        if authenticated:
            self.main_window = MainWindow()  # Crie uma instância da classe da janela principal
            self.main_window.show()
            self.close()

        # Se não autenticado
        else:
            self.show_message_box(QMessageBox.Warning, "Erro", "Login ou senha inválidos", self)

        db.close_connection()

    def open_forget_password_window(self):
        # Abre a janela de recuperação de senha
        self.forget_w = ForgetPassword()
        self.forget_w.show()


class SignUp(QWidget, Ui_signup, FunctionsInCommon):
    def __init__(self) -> None:
        super(SignUp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadastro")

        # Conecte os eventos da tela de cadastro aos métodos correspondentes
        self.btn_cadastrar.clicked.connect(self.collect_user_data)
        self.password_repeat_lineEdit.returnPressed.connect(self.collect_user_data)
        self.btn_return.clicked.connect(self.open_login)

    def collect_user_data(self):
        """
        Insere usuários no banco de dados.
        Realiza uma série de validações para tratar os dados fornecidos pelo usuário.
        Envia um código de verificação para o email fornecido e abre a tela de verificação, se as validações passarem.
        """

        if not self.username_lineEdit.text() or not self.email_lineEdit.text() or not self.password_lineEdit.text():
            self.show_message_box(QMessageBox.Warning, "Erro", "Todos os campos são obrigatórios", self)
            return

        if not self.validate_email(self.email_lineEdit.text()):
            self.show_message_box(QMessageBox.Warning, "Erro", "E-mail inválido", self)
            return

        if self.password_lineEdit.text() != self.password_repeat_lineEdit.text():
            self.show_message_box(QMessageBox.Warning, "Erro", "As senhas digitadas são diferentes", self)
            return

        user = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        email = self.email_lineEdit.text()

        db = DataBase()  # Crie uma instância da classe de banco de dados
        db.connect()

        if db.already_exists(user, password, email):
            self.show_message_box(QMessageBox.Warning, "Erro", "E-mail ou usuário já cadastrado", self)
            db.close_connection()
            return

        db.close_connection()

        verification_code = send_verify_code(user, email)  # Envie o código de verificação para o email fornecido

        self.verify_window = VerificationCode(verification_code, user, email, password)  # Crie uma instância da classe de código de verificação
        self.verify_window.show()

        # Limpe os campos de entrada de dados
        self.username_lineEdit.setText("")
        self.password_lineEdit.setText("")
        self.password_repeat_lineEdit.setText("")
        self.email_lineEdit.setText("")

    def open_login(self):
        # Abre a tela de login e fecha a janela de cadastro
        self.w = Login()
        self.w.show()
        self.close()


class ForgetPassword(QWidget, Ui_forgetpassword, FunctionsInCommon):
    def __init__(self) -> None:
        super(ForgetPassword, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Redefinição de senha")

        # Conecte os eventos da tela de redefinição de senha aos métodos correspondentes
        self.btn_redefine.clicked.connect(self.redefine_password)
        self.repeat_password_lineEdit.returnPressed.connect(self.redefine_password)

    def redefine_password(self):
        """
        Redefine a senha do usuário.
        Realiza uma série de validações para tratar os dados fornecidos pelo usuário.
        Envia um código de verificação para o email fornecido e abre a tela de verificação, se as validações passarem.
        """

        if not self.email_lineEdit.text() or not self.password_lineEdit.text():
            self.show_message_box(QMessageBox.Warning, "Erro", "Todos os campos são obrigatórios", self)
            return

        if not self.validate_email(self.email_lineEdit.text()):
            self.show_message_box(QMessageBox.Warning, "Erro", "E-mail inválido", self)
            return

        if self.password_lineEdit.text() != self.repeat_password_lineEdit.text():
            self.show_message_box(QMessageBox.Warning, "Erro", "As senhas digitadas são diferentes", self)
            return

        db = DataBase()  # Crie uma instância da classe de banco de dados
        db.connect()

        user_data = db.search_email(self.email_lineEdit.text())

        if user_data:
            verification_code = send_verify_code(user_data[1], user_data[3])  # Envie o código de verificação para o email correspondente

            self.verify_window = VerificationCode(verification_code, password=self.password_lineEdit.text(),
                                                  redefine_password=True, user=user_data[1])  # Crie uma instância da classe de código de verificação
            self.verify_window.show()
            self.close()

        else:
            self.show_message_box(QMessageBox.Warning, "Erro", "Esse e-mail não está cadastrado", self)

        db.close_connection()


class RegisteredRecipients(QWidget, Ui_RegisteredRecipients):
    def __init__(self) -> None:
        super(RegisteredRecipients, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Visualização de destinatários")

        horizontal_header = self.tableWidget.horizontalHeader()

        # Define uma fonte para o cabeçalho das colunas
        horizontal_header.setStyleSheet(styles.horizontal_header_style)
        # Para fazer as colunas ocuparem a tela toda
        horizontal_header.setSectionResizeMode(0, QHeaderView.Stretch)
        horizontal_header.setSectionResizeMode(1, QHeaderView.Stretch)

        self.show_recipients()

    def show_recipients(self):
        db = DataBase()  # Crie uma instância da classe de banco de dados
        db.connect()
        result = db.show_recipients()
        db.close_connection()

        row = 0
        self.tableWidget.setRowCount(len(result))
        for recipient in result:
            item1 = QTableWidgetItem(recipient[0])
            item2 = QTableWidgetItem(recipient[1])

            font = QFont("Candara", 14)  # Define a fonte Candara com tamanho 14 para os itens
            font_color = QColor("white")  # Define a cor branca para a fonte
            item1.setFont(font)
            item1.setForeground(font_color)
            item2.setFont(font)
            item2.setForeground(font_color)

            item1.setFlags(item1.flags() ^ Qt.ItemIsEditable)
            item2.setFlags(item2.flags() ^ Qt.ItemIsEditable)

            self.tableWidget.setItem(row, 0, item1)
            self.tableWidget.setItem(row, 1, item2)

            row += 1
        self.registered_recipients.setText(f"Destinatários cadastrados: {row}")


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

        A classe possui o parâmetro "redefine_password", que quando True realiza a redefinição da senha através
        da função db.update_password.

        Quando o parâmetro "redefine_password" for False,
        ele insere o usuário no banco de dados através da função db.insert_user.
        """
        if self.redefine_password:
            if self.code_lineEdit.text() == self.verification_code:
                db = DataBase()  # Crie uma instância da classe de banco de dados
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
                db = DataBase()  # Crie uma instância da classe de banco de dados
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
        # ATRIBUTOS DESTINATÁRIOS
        self.recipients_filename = ''
        self.recipients_emails = []
        self.recipients_names = []

        # *--EVENTOS DA TELA PRINCIPAL--*
        self.btn_toggle.clicked.connect(self.left_menu)

        # *--EVENTOS PÁGINA DESTINATÁRIOS--*
        self.btn_search.clicked.connect(self.open_file_dialog)
        self.btn_validate.clicked.connect(self.validate_and_get_contacts)
        self.btn_signup_recipients.clicked.connect(self.upload_recipients)
        self.btn_registered_recipients.clicked.connect(self.open_registered_recipients)

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
        Abre o explorador de arquivos de modo a receber um arquivo (.csv),
        ao selecionar o mesmo, a função passa o caminho deste arquivo
        para o atributo recipients_filename da classe MainWindow, e também ativa o botão "Validar" (btn_validate).

        Caso o usuário abra o explorador de arquivos e feche sem selecionar nada o botão "Validar" é desativado.
        """
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Valores Separados por Vírgula (*.csv)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec():
            file_name = file_dialog.selectedFiles()[0]
            self.label_file_name.setText(file_name)

            self.able_disable_buttons(self.btn_validate, True, styles.green_button_stylesheet)

            self.recipients_filename = file_name
        else:
            self.label_file_name.setText("Selecione um arquivo")
            self.able_disable_buttons(self.btn_validate, False, styles.gray_button_stylesheet)

        self.able_disable_buttons(self.btn_signup_recipients, False, styles.gray_button_stylesheet)

    def validate_and_get_contacts(self):
        """
        Extraí os nomes e e-mails através da função get_contacts do módulo file_handling.

        Para realizar a validação é utilizado o Try — Except capturando a excessão ValueError, que significa que a
        função get_contacts encontrou um email inválido no arquivo. Exibindo assim uma mensagem de erro ao usuário.

        Caso passe pela validação exibe a quantidade de contatos válidos para inserção no banco de dados, e por fim
        ativa o botão "Cadastrar" (self.btn_signup_recipients)

        *Antes de exibir a mensagem de sucesso, valida se a quantidade de nomes extraídos é igual a de e-mails
        de modo a evitar problemas na inserção do banco de dados.
        """
        try:
            names, emails = file_handling.get_contacts(self.recipients_filename)

            if len(names) == len(emails):
                success_message = f"Arquivo válido.\nForam encontrados {len(emails)} contatos válidos."
                self.show_message_box(QMessageBox.Information, "Sucesso", success_message, self)

                self.able_disable_buttons(self.btn_signup_recipients, True, styles.green_button_stylesheet)

                self.recipients_names = names
                self.recipients_emails = emails
            else:
                self.show_message_box(QMessageBox.Warning, "Erro", "Erro desconhecido na leitura do arquivo", self)

        except (IndexError, UnicodeDecodeError):
            self.show_message_box(QMessageBox.Warning, "Erro", "Arquivo inválido. Consulte o menu AJUDA para uma explicação do leiaute do arquivo.", self)
        except ValueError as e:
            self.show_message_box(QMessageBox.Warning, "Erro", str(e), self)

    def upload_recipients(self):
        """
        Adiciona os destinatários ao banco de dados, ao terminar a inserção desativa os botões validar e cadastrar
        """
        try:
            db = DataBase()
            db.connect()
            for i, name in enumerate(self.recipients_names):
                db.insert_recipient(name, self.recipients_emails[i])

            self.show_message_box(QMessageBox.Information, "Sucesso", "Destinatários cadastrados com sucesso!", self)

            self.label_file_name.setText("Selecione um arquivo")
            self.able_disable_buttons(self.btn_validate, False, styles.gray_button_stylesheet)
            self.able_disable_buttons(self.btn_signup_recipients, False, styles.gray_button_stylesheet)

        except Exception as e:
            self.show_message_box(QMessageBox.Warning, "Erro", str(e), self)

    def open_registered_recipients(self):
        self.registered_recipients_window = RegisteredRecipients()
        self.registered_recipients_window.show()

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
    # BLOCO DE CÓDIGO DESTINADO A TESTES, INICIA A TELA ESPECIFICADA.
    app = QApplication(sys.argv)
    window = Login()
    # window = MainWindow()
    window.show()
    # window = VerificationCode()
    # window.show()
    app.exec()
