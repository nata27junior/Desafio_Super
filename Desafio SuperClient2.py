#ord() caracterer em int
#chr() int em caracter


dic = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
soma=0
letra = str(input('digite '))
for i in range(len(letra)):
    if len(letra)==1:
        soma =dic[letra[i]]
        elif len(letra)>=2:
            soma=soma + (dic[letra[i]]*13.5)
    #soma = soma+ (len(letra)-1)
        
        

print (int(soma))



print('a ', Desafios.xls2Dec('a'))
print('A ', Desafios.xls2Dec('A'))
print('z ', Desafios.xls2Dec('z'))
print('aa ', Desafios.xls2Dec('aa'))
print('az ', Desafios.xls2Dec('az'))
print('zz ', Desafios.xls2Dec('zz'))

print(Desafios.xls2Dec('fd'))
print(Desafios.xls2Dec('aaa'))
print(Desafios.xls2Dec('xfd'))  # 16384
print(Desafios.xls2Dec('xer'))  # 16372
