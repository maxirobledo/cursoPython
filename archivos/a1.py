try:
    archi = open('/home/maxi/devops/python/archivos/test.txt')
except:
    print('Error, archivo inexistente.')
    quit()
for linea in archi:
    print(linea)