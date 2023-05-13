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


# set up the SMTP server
def auth(smtp_server:str, port_:str, email_address:str, email_password:str):
    s = smtplib.SMTP(host=smtp_server, port=port_)
    s.starttls()
    s.login(email_address, email_password)

    return s



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
    smtp = auth('smtp.gmail.com', '587', 'appostman.noreply@gmail.com', 'itsfjeqvrkiswqsj')

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
    print(generate_code())