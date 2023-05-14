from main import FunctionsInCommon

def get_contacts(filename) -> tuple:
    """
    Lê um arquivo csv de (nome,email) e retorna uma tupla com uma lista com os nomes e uma com os emails.
    """
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        index = 0
        for a_contact in contacts_file:
            index += 1
            names.append(a_contact.split(',')[0].replace('\n', ''))

            fc = FunctionsInCommon()

            email = a_contact.split(',')[1].replace('\n', '')

            if fc.validate_email(email):
                emails.append(email)
            else:
                return f"Encontrado um e-mail inválido na linha {index}, por favor corrija o arquivo e tente novamente."

    return names, emails