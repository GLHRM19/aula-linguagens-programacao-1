notas=[]
i = 1
nota=float(input("nota[0]:"))
while nota != -1:
    notas.append(nota)
    nota = float(input('nota['+str(i)+']:'))
    i+=1

media=sum(notas)/len(notas)

if media>=7:
    print('Aprovado')
else:
    print('Reprovado')