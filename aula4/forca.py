palavras = ["dia"]
palavra = palavras[0]  # A palavra a ser adivinhada
resultado = ["_" for _ in palavra]  # Inicializa o resultado com underscores

# Partes do bonequinho da forca (a ordem das partes conforme solicitado)
boneco = ["O", "/|", "/|\\", "/ ", "/ \\"]
erros = 0  # Contador de erros

# Função para imprimir o boneco a cada erro
def imprimir_boneco(erros):
    if erros == 1:
        print("  " + boneco[0])  # Cabeça
    elif erros == 2:
        print("  " + boneco[0])  # Cabeça
        print(" " + boneco[1])   # Braço esquerdo
    elif erros == 3:
        print("  " + boneco[0])  # Cabeça
        print(" " + boneco[1])   # Braço esquerdo
        print(" " + boneco[2])   # Braço direito
    elif erros == 4:
        print("  " + boneco[0])  # Cabeça
        print(" " + boneco[1])   # Braço esquerdo
        print(" " + boneco[2])   # Braço direito
        print(" " + boneco[3])   # Perna esquerda
    elif erros == 5:
        print("  " + boneco[0])  # Cabeça
        print(" " + boneco[1])   # Braço esquerdo
        print(" " + boneco[2])   # Braço direito
        print(" " + boneco[3])   # Perna esquerda
        print(" " + boneco[4])   # Perna direita

# Função principal do jogo
while True:
    # Exibe o estado atual da palavra
    print(" ".join(resultado))
    
    # Solicita o palpite do jogador
    palpite = input("Digite uma letra: ").lower()

    # Verifica se o palpite não está na palavra
    if palpite not in palavra:
        erros += 1
        imprimir_boneco(erros)  # Imprime a parte do boneco

    # Atualiza o resultado com a letra correta
    for i, letra in enumerate(palavra):
        if palpite == letra:
            resultado[i] = letra

    # Verifica se o jogador acertou a palavra
    if resultado == list(palavra):
        print("Boa! Você acertou a palavra:", palavra)
        break

    # Verifica se o jogador perdeu
    if erros >= 5:
        print(f"Você perdeu! A palavra era: {palavra}")
        break
