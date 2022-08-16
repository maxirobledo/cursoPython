import optparse


def computepay(hours,rate):
    if hours > 40:
        reg = hours * rate
        otp = (hours - 40.00) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    return pay
in1 = input("Ingrese horas trabajadas: ")
in2 = input("Ingrese tarifa: ")

try:
    horas = float(in1)
    tarifa = float(in2)
except:
    print("Error, no se han ingresado datos válidos")
    quit()

pago = computepay(horas,tarifa)

print("Pago por horas extras tabajadas =",pago)
