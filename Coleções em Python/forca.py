import random

palavras = ["banana", "maca", "goiaba", "amora", "jabuticaba"]

palavra = random.choice(palavras)

resultado = ["_" for _ in palavra]

boneco = [
    "  _______",
    " |/      |",
    " |      \\o/",
    " |       |",
    " |      / \\",
    " |",
    "_|___"
]
erros = 0

while True:
    print("\nPalavra:", " ".join(resultado))
    print("Erros:", erros)
    for i in range(erros):
        print(boneco[i])

    if erros >= len(boneco):
        print("Você perdeu!")
        print("A palavra era:", palavra)
        break

    palpite = input("Digite uma letra: ").lower()

    if len(palpite) != 1 or not palpite.isalpha():
        print("Por favor, digite uma única letra.")
        continue

    if palpite in resultado:
        print("Você já tentou essa letra.")
        continue

    if palpite not in palavra:
        print("Você errou!")
        erros += 1
    else:
        print("Você acertou uma letra!")
        for i, letra in enumerate(palavra):
            if palpite == letra:
                resultado[i] = letra

    if "_" not in resultado:
        print("\nPalavra:", " ".join(resultado))
        print("Parabéns! Você acertou a palavra!")
        break

print("\nFim do jogo.")