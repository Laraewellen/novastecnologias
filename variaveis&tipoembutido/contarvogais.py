frase = input("Digite uma frase: ").upper() #convertendo tudo para maiúsculo

print(f"Na frase {frase}" " tem:\n",
    f"Qtd de A: {frase.count("A")}\n",
    f"Qtd de E: {frase.count("E")}\n",
    f"Qtd de I: {frase.count("I")}\n",
    f"Qtd de O: {frase.count("O")}\n",
    f"Qtd de U: {frase.count("U")}\n")