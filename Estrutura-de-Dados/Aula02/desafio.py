def soma_valores(n):
    total = 0
    for i in range(1, n + 1):
        total += i

    print(f"Na iteração {i}, o total é {total}")


soma_valores(5)


def soma2(n):
    soma = n * (n + 1) / 2

    return soma


soma2(5)
