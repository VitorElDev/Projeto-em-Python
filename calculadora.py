def menu():
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

def calcular(opcao, x, y):
    if opcao == 1:
        return x + y
    elif opcao == 2:
        return x - y
    elif opcao == 3:
        return x * y
    elif opcao == 4:
        if y == 0:
            return "Erro: divisão por zero"
        return x / y

while True:
    menu()
    try:
        op = int(input("Escolha uma opção: "))
        if op == 5:
            print("Saindo...")
            break
        if op in [1, 2, 3, 4]:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = calcular(op, a, b)
            print("Resultado:", resultado)
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")
