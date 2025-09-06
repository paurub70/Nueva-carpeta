print("calculadora simple\n")

operacion= input(" elige la operacion que desea realizar (SUMA, RESTA, MULTIPLICACION,DIVISION):")

if operacion == "SUMA":
    numero_1 = float (input(" Ingresa el primer numero:"))
    numero_2 = float (input (" Ingresa el segundo numero:"))
    
    resultado = numero_1 + numero_2

    print (f"El resultado de la suma es: {resultado}")

elif operacion == "RESTA":
      numero_3 = float ( input("Ingresa el primer numero:"))
      numero_4 = float (input ("Ingresa el segundo numero:"))

      resultado_2 = numero_3 - numero_4

      print (f"El resultado de la resta es: {resultado_2}")

elif operacion == "MULTIPLICACION":
     numero_5 = float (input ("Ingresa el primer numero:"))    
     numero_6 = float ( input (" Ingresa el segundo numero:"))
    
     resultado_3 = numero_5 * numero_6
   
     print (f"El resultado de la multiplicacion es: {resultado_3}")

elif  operacion == "DIVISION":
     numero_7 = float (input("Ingresa el primer numero:"))
     numero_8 = float (input("Ingresa el segundo numero:"))
      
     resultado_4 = numero_7 / numero_8
      
     print (f"El resultado de la division es: {resultado_4}")
        
