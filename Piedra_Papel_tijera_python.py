import random
#Mi primer juego en Python
#Player 1 = computadora
#Player 2 = usuario - digitar en consola

#Objetivo: jugar piedra papel o tijera con el computador
# Primera opción: piedra gana a tijera
# Segunda opción: tijera gana a papel
# Tercera opción: papel gana a piedra
# Empate: piedra con piedra
# Empate: piedra con piedra
# Empate: tijera con tijera
# Empate: papel con papel
# Número de intentos 10
# el valor del computador debe ser ramdom

#Únicas opciones posibles
opciones = ['piedra', 'papel', 'tijera']
print("**Programa que es el juego Piedra,Papel o Tijera**")
# Contador de intentos
intentos = 4

# Función para determinar el ganador
def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'tijera' and computadora == 'papel') or \
         (usuario == 'papel' and computadora == 'piedra'):
        return "Usuario gana"
    else:
        return "Computadora gana"

for intento in range(intentos):
    # Elección del usuario
    usuario = input("Elige piedra, papel o tijera: ").lower()
    # Validar la entrada del usuario
    while usuario not in opciones:
        print("Entrada no válida. Por favor elige piedra, papel o tijera.")
        usuario = input("Elige piedra, papel o tijera: ").lower()
    
    # Elección de la computadora
    computadora = random.choice(opciones)
    
    # Impresión de las elecciones
    print("Usuario eligió:",usuario)
    print("Computadora eligió:",computadora)
    
    # Imprime el ganador
    resultado = determinar_ganador(usuario, computadora)
    print(resultado)
    #División de los intentos
    print('*'*20)