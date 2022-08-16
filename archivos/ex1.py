try:
    archivo = open('/home/maxi/devops/python/archivos/mbox-short.txt')
except:
    print('Imposible abrir archivo.')
    quit()
for line in archivo:
    print(line.upper())