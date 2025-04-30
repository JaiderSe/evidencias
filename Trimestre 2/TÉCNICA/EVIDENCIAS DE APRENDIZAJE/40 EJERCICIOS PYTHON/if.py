#2
num = int(input("Ingrese un numero:"))
if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
print("")

#3
num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese otro numero"))
num3 = int(input("Ingrese otro numero"))
 
if num1 > num2 and num1 > num3:
    print("El numero mayor es ",num1)
elif num2 > num1 and num2 > num3:
    print("El numero mayor es ",num2)
else:
    print("El numero mayor es ",num3)
print("")

#4

print("")
      
#7
peso = float(input("Ingrese su peso:"))
altura = float(input("Ingrese su altura:"))
imc = peso / (altura**2)

if imc < 18.5:
    print("Esta bajo de peso")
elif imc >=18.5 and imc < 24.9:
    print("Esta normal de peso")
elif imc >=25.0 and imc < 29.9:
    print("Tiene sobre peso")
elif imc >=30.0:
    print("Tiene obesidad")
print("")

#8
n1 = int(input("Ingrese su calificacion:"))
n2 = int(input("Ingrese su calificacion:"))
n3 = int(input("Ingrese su calificacion:"))
promedio = (n1 + n2 + n3) / 3
if promedio >= 7:
    print("El estudiante aprueba")
else:
    print("El estudiante no aprobo")
print("")

#9
n1 = int(input("Ingrese un numero:"))
n2 = int(input("Ingrese un numero:"))
operacion = input("Que operacion desea realizar?(suma, resta, multiplicacion, division):")

if operacion == "suma":
    print(n1 + n2)
elif operacion == "resta":
    print(n1 - n2)
elif operacion == "multiplicacion":
    print(n1 * n2)
elif operacion == "division":
    print(n1 / n2)
print("")


#10
compra = float(input("Ingrese el monton de su compra:"))

if compra >100 :
    print("su costo sera de", compra - 10%())
else:
    print("Su costo sera de",compra) #no sirve






