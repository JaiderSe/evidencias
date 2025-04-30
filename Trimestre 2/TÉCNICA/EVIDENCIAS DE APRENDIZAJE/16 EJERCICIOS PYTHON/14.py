num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))
num3 = int(input("Ingrese tercer número: "))


if num1 == num2:
    print(f"El número 1 ({num1}) es igual al 2 ({num2})")

elif num1 == num3:
    print(f"El número 1 ({num1}) es igual al 3 ({num3})")
    
elif num2 == num3:
    print(f"El número 2 ({num2}) es igual al 3 ({num3})")

elif  num2 < num1 and num3 < num1: 
    print("El número mayor es: ", num1)
    
elif num1 < num3 and num2 < num3: 
    print("El número mayor es: ", num3)
    
elif num1 < num2 and num3 < num2: 
    print("El número mayor es: ", num2)

elif num2 == num1 == num3:
    print("Los tres números son iguales")