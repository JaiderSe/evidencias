#1
nombre = input("Ingrese su nombre:")
print("Hola",nombre,("bienvenido al sena :D"))
print("")

#2
n1 = float(input("Ingrese un numero: "))
n2 = float(input("Ingrese un numero: "))
suma = n1 + n2
print("La suma de los numeros es ",suma)
print("")

#3
a= float(input("Ingrese la temperatura en grados celsius: "))
b=a*1.8+32
print("la temperatura de ",a, "Celcius a fahrenheit es",int(b))
print("")

#4
a=float(input("Ingrese el radio de un circulo: "))
pi=3.1416
b= pi*(a**2) 
print("el area de un circulo de radio ",a,"es: ", "%.2F"%b)
print("")

#5
n1 = int(input("Ingrese su calificacion:"))
n2 = int(input("Ingrese su calificacion:"))
n3 = int(input("Ingrese su calificacion:"))
promedio = (n1 + n2 + n3) / 3
print("El promedio de tus tres calificaciones es: ",promedio)
print("")

#6
metros = int(input("Ingrese una cantidad de metros que desea pasar a centimetros: "))
print (metros,"metros son",metros * 100, "centimetros")
print("")

#7
num = int(input("Ingrese un numero:"))
cuadrado = num **2
print("El numero al cuadrado es",cuadrado)
print("")

#8
precio=float(input("Ingrese el precio del producto:"))
porcentaje_iva=float(input("Ingrese el precio del iva:"))
iva=precio*(porcentaje_iva/100)
precio_final= precio+iva
print("el precio del producto mas su iba es:",precio_final)
print("")

#9
a=float(input("Ingrese la base del triangulo:"))
b=float(input("Ingrese la altura del triangulo:"))
area=a*b/2
print("el area es ", area)
L1=int(input("Ingrese la medida del lado 1 en centimetros:"))
L2=int(input("Ingrese la medida del lado 2 en centimetros:"))

print("el perimetro es ",L1+L2+a)


#10
