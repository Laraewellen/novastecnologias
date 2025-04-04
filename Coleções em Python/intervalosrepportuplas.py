intervalos =  [(1,4), (2,5), (7,9)]

intervalos.sort()
novo_intervalo = [intervalos[0]]

for inicio, fim in intervalos[1:]:
    ultimo_inicio, ultimo_fim = novo_intervalo[-1]
    
    if inicio <= ultimo_fim:
        novo_intervalo [-1] = (ultimo_inicio, max(ultimo_fim, fim))
    else:
        novo_intervalo.append((inicio,fim))

print(novo_intervalo)