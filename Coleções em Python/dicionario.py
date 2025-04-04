frase = list (input("Digite uma frase: ") .lower())

mapa = {}

for letra in frase:
    if letra in mapa:
        mapa [letra] = mapa.get(letra, 0) + 1
    else:
        mapa[letra] = 1

for chave, valor in mapa.items():
    print(f"{chave} -> {valor}")
    