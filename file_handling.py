
def get_contacts(filename) -> tuple:
    """
    Lê um arquivo csv de (nome,email) e retorna uma tupla com uma lista com os nomes e uma com os emails.
    """
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split(',')[0].replace('\n', ''))
            emails.append(a_contact.split(',')[1].replace('\n', ''))
    return names, emails