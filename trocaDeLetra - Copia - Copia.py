usuario = input('Informe seu nome: ')
x = int(input('posição da letra: '))-1
if usuario[x]=='r':
   print(usuario[:x],'s',usuario[x+1:],sep='')
elif usuario[x]=='m':
    print(usuario[:x], 'n', usuario[x + 1:], sep='')
else:
    print(usuario[:x], usuario[x + 1:], sep='')


