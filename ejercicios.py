# 1 Pedimos el costo de la cuenta y el porcentaje de propina
costo = float(input("Ingrese el costo de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina: "))

propina = costo * (porcentaje_propina / 100)
total = costo + propina

print(f"Costo de la cuenta: ${costo:.2f}")
print(f"Propina: ${propina:.2f}")
print(f"Total a pagar: ${total:.2f}")

# 2 Pedimos la edad del usuario
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Puedes votar.")
else:
    print("No puedes votar.")

# 3 Suma de numeros pares
N = int(input("Ingrese un número N: "))

suma_pares = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        suma_pares += i

print(f"La suma de los números pares desde 1 hasta {N} es: {suma_pares}")

import random

# 4 Generamos un número secreto entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número secreto (entre 1 y 100): "))
    intentos += 1
    
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
        break

# 5 Pedimos un texto al usuario
texto = input("Ingrese un texto: ")

contador_vocales = 0
vocales = "aeiouAEIOU"

for letra in texto:
    if letra in vocales:
        contador_vocales += 1
print(f"El texto contiene {contador_vocales} vocales.")
