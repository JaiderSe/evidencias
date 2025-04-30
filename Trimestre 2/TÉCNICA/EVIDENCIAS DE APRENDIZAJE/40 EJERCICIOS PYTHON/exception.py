while True:
    try:
        # Solicitar dos números al usuario
        num1 = float(input("Introduce el primer número  "))
        num2 = float(input("Introduce el segundo número "))
 

         # Intentamos realizar la división
        resultado = num1 / num2
        
    except Exception as e:
        # Captura cualquier otro tipo de error inesperado
        print(f"ingrese un numero valido: {e}")
        
    else:
        # Si no hubo excepciones, mostrar el resultado
        print(f"El resultado de la división es: {"%.1f"%resultado}")


    finally:
        # Este bloque siempre se ejecuta
        salir = input("¿Quieres intentar otra vez? (s/n): ")
        if salir.lower() != 's':
            print("¡Adiós!")
            break  # Salir del bucle si el usuario no desea continuar






