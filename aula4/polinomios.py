p1 = {2: 3, 1: 2, 0: 1}  # 3x^2 + 2x + 1
p2 = {1: 1, 0: 4}  # x + 4

# (3x^2 + 2x + 1) * (x + 4) = 3x^3 + 12x^2 + 2x^2 + 8x + x + 4 = 3x^3 + 14x^2 + 9x + 4

p_result = {}

for expl, coefl in p1.items():
    for exp2, coef2 in p2.items():
        p_result[expl + exp2] = p_result.get(expl + exp2, 0) + coefl * coef2

print("p1 =", end=" ")
for chave in sorted(p1, reverse=True):
    valor = p1[chave]
    print(f"{valor}x^{chave}", end="")
    if chave != 0 and any(k > chave for k in p1):
        print(" + ", end="")
print()

print("p2 =", end=" ")
for chave in sorted(p2, reverse=True):
    valor = p2[chave]
    print(f"{valor}x^{chave}", end="")
    if chave != 0 and any(k > chave for k in p2):
        print(" + ", end="")
print()

print("(p1 * p2) =", end=" ")
for chave in sorted(p_result, reverse=True):
    valor = p_result[chave]
    print(f"{valor}x^{chave}", end="")
    if chave != 0 and any(k > chave for k in p_result):
        print(" + ", end="")
print()