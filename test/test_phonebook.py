from src.phonebook import Phonebook
from src.phonebook import valid_name
from src.phonebook import valid_number

class TestPhonebook:

    def test_add(self):
        assert False

    # Main Flow
    def test_add_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = 'Numero adicionado'

        # Chamada
        resposta = phonebook.add("Talita", "24988281352")

        # Avaliação
        assert resposta_esperada == resposta

    def test_add_numero_menor_zero(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = 'Numero invalido'

        # Chamada
        resposta = phonebook.add("Talita", "-2")

        # Avaliação
        assert resposta_esperada == resposta

    def test_valid_name(self):
        # Setup
        resposta_esperada = 'Nome invalido'

        # Chamada
        resposta = valid_name('#' or '@' or '!' or '$' or '$')

        # Avaliação
        assert resposta_esperada == resposta

    def test_valid_numer(self):
        # Setup
        resposta_esperada = 'Numero invalido'

        # Chamada
        resposta = valid_number('-2')

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

    def test_get_numbers_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = ['190']

        # Chamada
        resposta = list(phonebook.get_numbers())

        # Avaliação
        assert resposta_esperada == resposta

    def test_clear_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = 'phonebook limpado'

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

    def test_get_phonebook_sorted_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = ['POLICIA']

        # Chamada
        resposta = list(phonebook.get_phonebook_sorted())

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_phonebook_reverse_com_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resposta_esperada = ['POLICIA']

        # Chamada
        resposta = list(phonebook.get_phonebook_reverse())

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

