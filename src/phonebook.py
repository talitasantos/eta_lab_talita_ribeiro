def valid_name(name):
    if isinstance(name, str) and name.isalpha():
        return True
    else:
        return 'Nome invalido'
    # special_chars = ['#', '@', '!', '$', '%']
    # for i in special_chars:
    #     if i in name:
    #         return 'Nome invalido'
    # return True


def valid_number(number):
    if isinstance(number, str) and number.isdigit() and int(number) >= 0:
        return True
    else:
        return 'Numero invalido'


class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """

        """
        Código muito repetivo e mensagens erradas.
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nme invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalio'
        if '%' in name:
            return 'Nome invalido'
        """
        # Método para validar se um nome é válido e uma string
        valid_name(name)

        # Método para validar se umm nome é string, um digito e maior que zero
        valid_number(number)

        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """

        """
        Código muito repetivo e mensagens erradas.
        if '#' in name:
            return 'Nome invaldo'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nme invalido' #bug: deveria ser Nome invalido
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome nvalido' #bug: deveria ser Nome invalido
        """

        # Método para validar se um nome é válido
        valid_name(name)

        return self.entries[name]

    def get_names(self):
        """
MELHORAR A PARTIR DAQUI!
        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return self.entries.values()

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            # Tem que retornar a lista do que da match com o termo de busca
            # if search_name not in name:
            if search_name in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        return self.entries

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return self.entries

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'
