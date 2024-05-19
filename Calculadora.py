def calculadora():
    # Solicitar el primer número al usuario
    num1 = float(input("Introduce el primer número: "))
    
    # Solicitar el segundo número al usuario
    num2 = float(input("Introduce el segundo número: ")) 

    # Solicitar operacion al usuario
    operacion = input("Que operacion desea realizar: (+, -, *, / ): ")
    
    # Realizar la operación correspondiente
    if operacion == "+":
     resultado = num1 + num2
    elif operacion  == "-": 
     resultado = num1 - num2
    elif operacion == "*":
     resultado = num1 * num2
    else:
     resultado = num1 / num2  
    # Mostrar el resultado
    print(f"El resultado de {num1} {operacion}  {num2} es: {resultado}")

# Llamar a la función calculadora
calculadora()