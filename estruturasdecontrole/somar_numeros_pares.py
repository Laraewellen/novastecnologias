n = int(input("Digite um número: "))

soma = 0

for num in range (0,n+1,2):
    soma +=num

print(f"De 1 ate {n}, a soma é {soma}")