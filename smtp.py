import socket
from string import Template
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from random import randint





# Function to read the message from a given message file and return a template object
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


"""
Trabalhando ainda nessa função.

Faltam capturar todas as exceções possíveis relacionadas a erros na conexão e arrumar a interface gráfica pra
não deixar o usuário disparar essa função sem ter digitado nada, ou ter digitado dados incoerentes.
"""
def auth_smtp(smtp_server:str, port_:str, email_address:str, password:str):
    try:
        # cria a conexão SMTP
        smtp_connection = smtplib.SMTP(smtp_server, port_)
        # inicia a criptografia
        smtp_connection.starttls()
        # loga no servidor SMTP
        smtp_connection.login(email_address, password)
        # encerra a conexão
        smtp_connection.quit()

        # chegando até aqui os dados são válidos
        return True

    # caso dispare qualquer exceção, os dados são inválidos.
    except socket.gaierror:
        return False





def send_email(sender:str, names, emails:list, message_template:Template, smtp_object:smtplib.SMTP):

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # Create a message

        message = message_template.substitute(PERSON_NAME=name.title())

        # setup the parameters of the message

        msg['From'] = sender
        msg['To'] = email
        msg['Subject'] = "This is TEST"

        # add in the message body

        msg.attach(MIMEText(message, 'plain'))

        smtp_object.send_message(msg)

        del msg

def generate_code():
    abc = "a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9"
    abc = abc.split(" ")

    code = ""
    for i in range(10):
        i = randint(0, 31)
        code += abc[i].upper()

    return code

def send_verify_code(username, email):

    smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)

    smtp.starttls()

    smtp.login('appostman.noreply@gmail.com', 'itsfjeqvrkiswqsj')

    msg = MIMEMultipart()  # Create a message

    code = generate_code()

    message = f"Olá {username}\n\nAqui está seu código de verificação:\n\t{code}"

    # setup the parameters of the message

    msg['From'] = 'appostman.noreply@gmail.com'
    msg['To'] = email
    msg['Subject'] = "Código de verificação"

    # add in the message body

    msg.attach(MIMEText(message, 'plain'))

    smtp.send_message(msg)

    del msg
    return code


if __name__ == '__main__':
    send_verify_code('teste', 'ryan.henrique.silva.antonio@gmail.com')