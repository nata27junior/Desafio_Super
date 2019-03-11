from Desafio_SuperClient import *


def ler_arq(arq):
    texto = arq.read().split('\n')
    n = len(texto)
    i = 1
    a = 0
    while i < n:
        if texto[a].isalpha() == False:
            a = a + 1
        else:
            p = Desafios.xls2Dec(texto[a])
            print(texto[a], '=', p)
            i = i + 1
            a = a + 1
    arq.close()


opcao = 0
while opcao != 5:
    opcao = int(input('''\n[ 1 ] entrada_1\n[ 2 ] entrada_2\n[ 3 ] entrada_3\n[ 4 ] entrada_4\n[ 5 ] sair do 
    programa\nDigite um opção: '''))
    if opcao == 1:
        arq = open('entrada_1.txt', 'r')
        ler_arq(arq)
    elif opcao == 2:
        arq = open('entrada_2.txt', 'r')
        ler_arq(arq)
    elif opcao == 3:
        arq = open('entrada_3.txt', 'r')
        ler_arq(arq)
    elif opcao == 4:
        arq = open('entrada_4.txt', 'r')
        ler_arq(arq)
    elif opcao == 5:
        print('Finalizando ...')
    else:
        print("opção invalida tente novamente")
        print('=-=' * 10)
