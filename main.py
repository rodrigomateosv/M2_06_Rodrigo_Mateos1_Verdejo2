#EJERCICIO1
# PARTE 1 


import math
def area_circulo():
     Radio = float(input("Introduca el radio del circulo:\n")) 
     Area = math.pi*(Radio*Radio)
     return 'El área de un circulo de radio {} es de {} unidades cuadradas.'.format(Radio, Area)

print (area_circulo())
#EJERCICIO2


def lee_numero():
    return int(input("Introduzca un numero:"))
 
def mayor(a,b,c):
    if a>b and a>c:
        return a
    if b>c:
        return b
    return c
 
valores=[]
for i in range(3):
    valores.append(lee_numero())
 
print(f"El valor máximo es el {mayor(valores[0], valores[1],valores[2])}")

#EJERCICIO3


def imc(peso, altura):
    IMC = peso / (altura*altura)
 
    if IMC<18.5:
        return "Bajo Peso"
    elif IMC>=18.5 and IMC<=25:
        return "Peso Saludable"
    elif IMC>=30:
        return "Obesidad"
    return "Sobrepeso"
 
print("CÁLCULO DEL ÍNDICE DE MASA CORPORAL (IMC)")
peso = float(input("¿Cuántos kg pesa? "))
altura = float(input("¿Cuánto mide en metros? "))
print(imc(peso, altura))