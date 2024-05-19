def calculadora():
    # Solicitar el primer número al usuario
    num1 = float(input("Introduce el primer número: "))
    
    # Solicitar el segundo número al usuario
    num2 = float(input("Introduce el segundo número: ")) 
    
    # Realizar la operación correspondiente
    resultado = num1 + num2

    # Mostrar el resultado
    print(f"El resultado de {num1} + {num2} es: {resultado}")

# Llamar a la función calculadora
calculadora()