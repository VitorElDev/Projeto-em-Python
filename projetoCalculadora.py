def Main(ListaDeOperacaoSoma, ListaDeOperacaoSub, ListaDeOperacaoMult, ListaDeOperacaoDiv):
    print("\n################# Calculadora #################\n")
    
    operacao = int(input("Digite o código da operação:\n0 - somar\n1 - dividir\n2 - multiplicar\n3 - subtrair\n4 - ver histórico\n5 - limpar histórico \n6 - sair\n"))
    
    if operacao in [0, 1, 2, 3]:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))

        if operacao == 0:
            resultado = Somar(numero1, numero2)
            ListaDeOperacaoSoma.append(f"{numero1} + {numero2} = {resultado}")
        elif operacao == 1:
            if numero2 == 0:
                print("Erro: divisão por zero!")
                Main(HistoricoSoma,HistoricoSub,HistoricoMult,HistoricoDiv)
                return
            resultado = Dividir(numero1, numero2)
            ListaDeOperacaoDiv.append(f"{numero1} / {numero2} = {resultado}")
        elif operacao == 2:
            resultado = Multiplicar(numero1, numero2)
            ListaDeOperacaoMult.append(f"{numero1} * {numero2} = {resultado}")
        elif operacao == 3:
            resultado = Subtrair(numero1, numero2)
            ListaDeOperacaoSub.append(f"{numero1} - {numero2} = {resultado}")
        
        print("Resultado da operação:", resultado)
    
    elif operacao == 4:
        print("##### Histórico de Operações #####\n")
        print("SOMA: \n")
        if(len(HistoricoSoma)<=0):
            print("Não há históricos de Soma")
        for item in HistoricoSoma:
            print(item)
            
        print("\nSUBTRAÇÃO: \n")
        if(len(HistoricoSub)<=0):
            print("Não há históricos de subtração")
        for item in HistoricoSub:
            print(item)    
        print("\nMULTIPLICAÇÃO: \n")
        if(len(HistoricoMult)<=0):
            print("Não há históricos de Multiplicação")
        for item in HistoricoMult:
            print(item)  
        print("\nDIVISÃO: \n")
        if(len(HistoricoDiv)<=0):
            print("Não há históricos de Divisão\n")
        for item in HistoricoDiv:
            print(item)
    elif operacao == 5:
        print("Limpando histórico...")
        HistoricoDiv.clear()
        HistoricoMult.clear()
        HistoricoSoma.clear()
        HistoricoSub.clear()
        print("Histórico limpo com sucesso.")          
    elif operacao == 6:
        print("Encerrando...")
        return
    Main(HistoricoSoma,HistoricoSub,HistoricoMult,HistoricoDiv)


def Somar(a, b):
    return a + b

def Subtrair(a, b):
    return a - b

def Multiplicar(a, b):
    return a * b

def Dividir(a, b):
    return a / b



HistoricoSoma = []
HistoricoSub = []
HistoricoMult = []
HistoricoDiv = []
Main(HistoricoSoma,HistoricoSub,HistoricoMult,HistoricoDiv)
