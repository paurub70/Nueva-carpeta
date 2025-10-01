# 6 Pedimos un número al usuario
numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    
    
    #7 Pedimos un número al usuario
numero = int(input("Ingrese un número para iniciar la cuenta regresiva: "))

while numero >= 0:
    print(numero)
    numero -= 1
    
    
#8 Definimos la contraseña correcta
contraseña_correcta = "1234"


while True:
    contraseña = input("Ingrese la contraseña: ")
    
    if contraseña == contraseña_correcta:
        print("Acceso concedido.")
        break  
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
        
        
#9 Sumador acumulativo
suma = 0

while True:
    numero = int(input("Ingrese un número para sumar (0 para salir): "))
    
    if numero == 0:
        break  
    
    suma += numero  
    print(f"Suma actual: {suma}")
