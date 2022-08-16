# inp = input("Ingrese un número: ")
# try:
#     num = int(inp)
# except:
#     num = -1
# if num > 0:
#     print("Ha ingresado un número")
# else:
#     print("No ha ingresado un número.")


temp = "5"
cel = 0
try:
    fahr = float(temp)
except:
    fahr = -1
if fahr > 0:
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel,"grados celsius")
else:
    print("Error. Valor fahr mal iungresado.")
