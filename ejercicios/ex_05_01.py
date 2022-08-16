# Ejercicio 1: escriba un programa que lea números repetidamente hasta que el usuario ingrese "listo". 
# Una vez que haya ingresado "listo", imprima el total, el conteo y el promedio de los números. 
# Si el usuario ingresa algo que no sea un número, detecte su error usando try y except e imprima un mensaje de error y salte al siguiente número.
# https://books.trinket.io/pfe/05-iterations.html

count = 0
total = 0
media = 0
while True:
    val = input('Ingrese un número: ')
    if val == 'listo':
        break
    try:
        val = float(val)
    except: 
        print("No ha ingresado un numero.")
        continue
    count = count + 1
    total = total + val
media = total / count
print("Cantidad = ",count,"Total = ", total,"Promedia = ",media)