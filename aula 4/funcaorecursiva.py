def sequencia(n, memo = {}):
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        resultado = memo[n]
    else: 
        return sequencia (n-1, memo) + 2*sequencia(n-2, memo)

        memo[n] = resultado

        return
calc = lambda n:sequencia(n)

n = int(input("Entre com posição desejada: "))

print(f"T{n} = {calc(n)}")