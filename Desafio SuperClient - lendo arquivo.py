from Desafio_SuperClient import*
nome_arquivo = str(input('Informe o nome do arquivo: (exemplo entrada_1.txt)  '))
arq = open(nome_arquivo, 'r')
texto = arq.read().split('\n')
n=len(texto)
i=1
a=0
while i < n:
    if texto[a].isalpha()==False  :
        a=a+1
    else:
        p = Desafios.xls2Dec(texto[a])
        print(texto[a], '=', p)
        i = i + 1
        a=a+1


arq.close()
