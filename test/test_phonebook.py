from src.phonebook import Phonebook
from src.phonebook import valid_name
from src.phonebook import valid_number


class TestPhonebook:

    def test_add_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = 'Numero adicionado'

        # Chamada
        resposta = phonebook.add("Talita", "24988281352")

        # Avaliação
        assert resposta_esperada == resposta

    def test_valid_name(self):
        # Setup
        resposta_esperada = 'Nome invalido'

        # Chamada
        resposta = valid_name('#' or '@' or '!' or '$' or '$')

        # Avaliação
        assert resposta_esperada == resposta

    def test_valid_name_none(self):
        # Setup
        resposta_esperada = 'Nome invalido'

        # Chamada
        resposta = valid_name(None)

        # Avaliação
        assert resposta_esperada == resposta

    def test_valid_numer(self):
        # Setup
        resposta_esperada = 'Numero invalido'

        # Chamada
        resposta = valid_number('-2')

        # Avaliação
        assert resposta_esperada == resposta

    def test_valid_numer_none(self):
        # Setup
        resposta_esperada = 'Numero invalido'

        # Chamada
        resposta = valid_number(None)

        # Avaliação
        assert resposta_esperada == resposta

    def test_lookup_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = '190'

        # Chamada
        resposta = phonebook.lookup('POLICIA')

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_names_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = ['POLICIA']

        # Chamada
        resposta = list(phonebook.get_names())

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_name_vazio(self):
        # Setup
        phonebook = Phonebook()
        phonebook.clear()
        resposta_esperada = 'Nao possui registro'

        # Chamada
        resposta = phonebook.get_names()

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_numbers_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = ['190']

        # Chamada
        resposta = list(phonebook.get_numbers())

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_number_vazio(self):
        # Setup
        phonebook = Phonebook()
        phonebook.clear()
        resposta_esperada = 'Nao possui registro'

        # Chamada
        resposta = phonebook.get_numbers()

        # Avaliação
        assert resposta_esperada == resposta

    def test_clear_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = 'Phonebook limpado'

        # Chamada
        resposta = phonebook.clear()

        # Avaliação
        assert resposta_esperada == resposta

    def test_search_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = [{'190', 'POLICIA'}]

        # Chamada
        resposta = list(phonebook.search('POLICIA'))

        # Avaliação
        assert resposta_esperada == resposta

    def test_search_nao_encontrado(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = 'Nome não encontrado'

        # Chamada
        resposta = phonebook.search('MEDICO')

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_phonebook_sorted_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = [['POLICIA', '190']]

        # Chamada
        resposta = list(phonebook.get_phonebook_sorted())

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_phonebook_sorted_vazio(self):
        # Setup
        phonebook = Phonebook()
        phonebook.clear()
        resposta_esperada = 'Phonebook vazio'

        # Chamada
        resposta = phonebook.get_phonebook_sorted()

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_phonebook_reverse_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = [['POLICIA', '190']]

        # Chamada
        resposta = list(phonebook.get_phonebook_reverse())

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_phonebook_reverse_vazio(self):
        # Setup
        phonebook = Phonebook()
        phonebook.clear()
        resposta_esperada = 'Phonebook vazio'

        # Chamada
        resposta = phonebook.get_phonebook_reverse()

        # Avaliação
        assert resposta_esperada == resposta

    def test_delete_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = 'Numero deletado'

        # Chamada
        resposta = phonebook.delete('POLICIA')

        # Avaliação
        assert resposta_esperada == resposta

    def test_delete_registro_vazio(self):
        # Setup
        phonebook = Phonebook()
        phonebook.clear()
        resposta_esperada = 'Phonebook vazio'

        # Chamada
        resposta = phonebook.delete('')

        # Avaliação
        assert resposta_esperada == resposta

    def test_delete_registro_nao_encontrado(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = 'Registro nao encontrado'

        # Chamada
        resposta = phonebook.delete('MEDICO')

        # Avaliação
        assert resposta_esperada == resposta

    def test_change_number(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Talita", "(24)2222-3333")
        resposta_esperada = 'Numero de telefone alterado com sucessso'

        # Chamada
        resposta = phonebook.change_number("Talita", "(21)2222-3333")

        # Avaliação
        assert resposta_esperada == resposta

    def test_change_number_vazio(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Talita", None)
        resposta_esperada = 'Nao foi possivel alterar numero'

        # Chamada
        resposta = phonebook.change_number("Talita", None)

        # Avaliação
        assert resposta_esperada == resposta

    def test_change_number_nao_encontrado(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Talita", "(24)1122-3399")
        resposta_esperada = 'Nao foi possivel encontrar o numero'

        # Chamada
        resposta = phonebook.change_number("Roberta", None)

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_name_by_number_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Talita", "(24)1122-3399")
        resposta_esperada = 'Registro encontrado: Talita'

        # Chamada
        resposta = phonebook.get_name_by_number("(24)1122-3399")

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_name_by_number_vazio(self):
        # Setup
        phonebook = Phonebook()
        phonebook.clear()
        resposta_esperada = 'Phonebook vazio'

        # Chamada
        resposta = phonebook.get_name_by_number(None)

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_name_by_number_nao_encontrado(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Talita", "(32)1122-3399")
        resposta_esperada = 'Registro nao encontrado'

        # Chamada
        resposta = phonebook.get_name_by_number("(24)1122-3399")

        # Avaliação
        assert resposta_esperada == resposta
