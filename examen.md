base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
area = base * altura
print(f"El área del rectángulo es: {area}")

celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C es igual a {fahrenheit}°F")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nombre_completo = nombre + " " + apellido
print(f"Su nombre completo es: {nombre_completo}")

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es elegible para votar")
else:
    print("Usted no es elegible para votar")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num1} es menor que {num2}")
else:
    print(f"{num1} y {num2} son iguales")

numero = int(input("Ingrese un número: "))
if numero >= 10 and numero <= 20:
    print(f"{numero} está entre 10 y 20")
else:
    print(f"{numero} no está entre 10 y 20")

contraseña = "mi_contraseña"
intento = input("Ingrese la contraseña: ")
if intento == contraseña:
    print("Acceso concedido")
else:
    print("Acceso denegado")


numero = float(input("Ingrese un número: "))
if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print(f"{numero} es cero")

año = int(input("Ingrese un año: "))
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print(f"{año} es bisiesto")
else:
    print(f"{año} no es bisiesto")

nota = float(input("Ingrese la nota: "))
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")

letra = input("Ingrese una letra: ").lower()
if letra in "aeiou":
    print(f"{letra} es una vocal")
else:
    print(f"{letra} es una consonante")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
if num1 >= num2 and num1 >= num3:
    print(f"{num1} es el mayor")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} es el mayor")
else:
    print(f"{num3} es el mayor")

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f"Su IMC es {imc:.2f}, usted tiene bajo peso")
elif imc < 25:
    print(f"Su IMC es {imc:.2f}, usted tiene peso normal")
elif imc < 30:
    print(f"Su IMC es {imc:.2f}, usted tiene sobrepeso")
else:
    print(f"Su IMC es {imc:.2f}, usted tiene obesidad")

peso = float(input("Ingrese el peso del paquete en kg: "))
zona = input("Ingrese la zona de destino (A, B o C): ")
if zona == "A":
    costo = 10 + (peso * 2)
elif zona == "B":
    costo = 15 + (peso * 3)
elif zona == "C":
    costo = 20 + (peso * 4)
else:
    print("Zona inválida")
    costo = 0
print(f"El costo de envío es {costo}")

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))
discriminante = b ** 2 - 4 * a * c
if discriminante > 0:
    raiz1 = (-b + discriminante ** 0.5) / (2 * a)
    raiz2 = (-b - discriminante ** 0.5) / (2 * a)
    print(f"Las raíces son {raiz1} y {raiz2}")
elif discriminante == 0:
    raiz = -b / (2 * a)
    print(f"La raíz es {raiz}")
else:
    print("No hay raíces reales")

jugador1 = input("Ingrese la jugada del jugador 1 (piedra, papel o tijera): ").lower()
jugador2 = input("Ingrese la jugada del jugador 2
