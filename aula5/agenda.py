class Contato:
    __slots__ = {'_nome', '_telefone', '_datanasc', '_email'}

    def __init__(self, nome, telefone, datanasc, email):
        self._nome = nome
        self._telefone = telefone
        self._datanasc = datanasc
        self._email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

