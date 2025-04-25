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

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def datanasc(self):
        return self._datanasc

    @datanasc.setter
    def datanasc(self, datanasc):
        self._datanasc = datanasc

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
