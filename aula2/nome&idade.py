nome = input("Digite seu nome: ")
idade = int(input("digite sua idade: "))
altura = float(input("sua altura: "))
massa = float(input("seu peso: "))

print(f"Nome: {nome}\nIdade: {idade}\nIMC: {massa/altura**2:.2f}")