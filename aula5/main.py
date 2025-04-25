from agenda import Contato
import datetime

print("""
    *******************************
    * Bem vindo ao Sistema agenda *
    *******************************
""")

# Definindo o primeiro contato
nome = "Fernanda"
telefone = "61993552745"
datanasc = datetime.date(2000, 9, 12)
email = "Fernanda.G@gmail.com"

contato1 = Contato(nome, telefone, datanasc, email)

# Definindo o segundo contato
contato2 = Contato(nome="Maria", telefone="61882445965", datanasc=datetime.date(2004, 7, 19), email="Maria.G@gmail.com")

# Exibindo os contatos
print(f"Contato 1: {contato1.nome}, {contato1.telefone}, {contato1.datanasc}, {contato1.email}")
print(f"Contato 2: {contato2.nome}, {contato2.telefone}, {contato2.datanasc}, {contato2.email}")
