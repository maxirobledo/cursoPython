try:
    archi = open('/home/maxi/devops/python/diccionarios/words.txt')
except:
    print('Error al abrir el archivo.')
    quit()

diccio = dict()
for linea in archi:
    palabras = linea.split()
    for palabra in palabras:
        diccio[palabra] = diccio.get(palabra,0) + 1
    
cade = input('Ingrese palabra a buscar en el texto: ')
if cade in diccio:
    print('La palabra "',cade,'" se repite',diccio[cade],'veces en el texto.')
else:
    print(cade,'no se encuentra en el texto')