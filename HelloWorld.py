import time

print("Hola, bienvenido!")

time.sleep(0.5)

nombre=input("Por favor, ingresá tu nombre >>>")
print("Hola " + nombre)

time.sleep(0.5)

print("Ahora ingresá tu edad ")
edad=input("Ingrese su edad >>>")
edad=int(edad)

if edad<18:
    print("Eres Menor de edad " + nombre)
if edad>=18:
    print("Eres mayor de edad " + nombre)

time.sleep(1.5)

print("Fin")