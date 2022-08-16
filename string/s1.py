
print('Iteración con bucle while')
fruit = 'manzana'
count = 0
index = 0
while index < len(fruit):
    letter=fruit[index]
    print('posicion:',index,'letra:',letter)
    if(letter == 'a'):
        count=count+1
    index=index+1
print('Se encontraron',count,'letras a')

print('')
print('Iteración con bucle for')
fruit = 'banana'
count = 0
for letter in fruit:
    print('letra:',letter)
    if(letter == 'a'):
        count=count+1
print('Se encontraron',count,'letras a')
