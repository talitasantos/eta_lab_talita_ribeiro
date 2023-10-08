"""
Escopo:
● 1 – Escrever testes unitários
● 2 – Achar bugs
● 3 – Melhorar código
● 4- Corrigir bugs
● 5 – Usar TDD para adicionar o método:
○ change_number(self, name, number)
● 6 – Usar TDD para adicionar o método:
○ get_name_by_number(self, number)

"""


def valid_name(name):
    if isinstance(name, str) and name.isalpha() and name is not None:
        return True
    else:
        return 'Nome invalido'


def valid_number(number):
    if isinstance(number, str) and number.isdigit() and number is not None:
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

        # Método para validar se um nome é válido e uma string
        valid_name(name)

        # Método para validar se um numero é string e um digito
        valid_number(number)

        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """

        # Método para validar se um nome é válido e uma string
        valid_name(name)

        return self.entries[name]

    def get_names(self):
        """
        :return: return all names in phonebook
        """
        if self.entries == {}:
            return "Nao possui registro"
        else:
            names = []
            for key in self.entries.keys():
                names.append(key)
            return names

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        if self.entries == {}:
            return "Nao possui registro"
        else:
            values = []
            for value in self.entries.values():
                values.append(value)
            return values

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        if self.entries == {}:
            return 'O Phonebook vazio'
        else:
            self.entries = {}
            return 'Phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            # Tem que retornar a lista do que da match com o termo de busca
            if search_name in name:
                result.append({name, number})
            else:
                return 'Nome não encontrado'
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        if self.entries == {}:
            return "Phonebook vazio"
        else:
            lista = []
            for name, number in self.entries.items():
                lista.append([name, number])
            lista.sort()
            return lista

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        if self.entries == {}:
            return "Phonebook vazio"
        else:
            lista = []
            for name, number in self.entries.items():
                lista.append([name, number])
            lista.sort(reverse=True)
            return lista

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        if self.entries != {}:
            if name in self.entries:
                self.entries.pop(name)
                return "Numero deletado"
            return "Registro nao encontrado"
        return "Phonebook vazio"

    def change_number(self, name, new_number):
        if name in self.entries:
            if new_number is not None:
                self.entries[new_number] = self.entries.pop(name)
                return "Numero de telefone alterado com sucessso"
            return "Nao foi possivel alterar numero"
        return "Nao foi possivel encontrar o numero"

    def get_name_by_number(self, search_number):
        if self.entries != {}:
            for name, number in self.entries.items():
                if search_number == number:
                    return f"Registro encontrado: {name}"
            return "Registro nao encontrado"
        return "Phonebook vazio"
