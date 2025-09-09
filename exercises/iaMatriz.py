"""
Considerando a estrutura de dados matricial em python, crie uma matriz 3x3  que recebe 9 dados de entrada e segue inserindo esses valores na matriz iniciando na primeira linha da matriz e da esquerda para direita.

Por exemplo, inserir 9 valores nessa ordem: 1,2,3,4,E,5,6,7,8. Considere que um caracter 'E' será inserido também.
"""

def criamatriz():
    i = 0
    vetEntrada = []
    while i < 9:
        entrada = input()
        if entrada.isdigit():
            entrada = int(entrada)
        vetEntrada.append(entrada)
        i += 1

    matriz = []

    # percorre linhas
    for i in range(3):
        linhaMatriz = []

        # percorre as 3 colunas
        for  j in range(3):
            linhaMatriz.append(vetEntrada[i*3 + j])
        matriz.append(linhaMatriz)

    return matriz


m = criamatriz()
print(m)

"""
Dada uma matriz de entrada, crie uma função de nome movimenta, que recebe uma matriz 3x3 como no exercício anterior e uma ação desejada (E - Esquerda, D - Direita, C - Cima ou B - Baixa) movimente a peça de caracter 'E' para a localsição correta de acordo com a ação desejada e retorne a matriz atualizada.

Sua função deve ser:

def movimenta(matriz, D): # Movimentar a peça 'E' da matriz para D (direita)

# ... código
# ... retorna a matriz atualizada
"""

def movimenta(matriz, acao):
    localE = (-1, -1)
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == 'E':
                localE = (i, j)
                break
        if localE != (-1, -1):
            break

    iE, jE = localE

    if acao == 'D' and jE < 2:  # mover para direita
        matriz[iE][jE], matriz[iE][jE + 1] = matriz[iE][jE + 1], matriz[iE][jE]
    elif acao == 'E' and jE > 0:  # mover para esquerda
        matriz[iE][jE], matriz[iE][jE - 1] = matriz[iE][jE - 1], matriz[iE][jE]
    elif acao == 'C' and iE > 0:  # mover para cima
        matriz[iE][jE], matriz[iE - 1][jE] = matriz[iE - 1][jE], matriz[iE][jE]
    elif acao == 'B' and iE < 2:  # mover para baixo
        matriz[iE][jE], matriz[iE + 1][jE] = matriz[iE + 1][jE], matriz[iE][jE]

    return matriz       

acao = input("Digite a ação de movimento sobre a peça E (E, D, C, B): ")
movimenta(m, acao)
print("Matriz atualizada:")
print(m)