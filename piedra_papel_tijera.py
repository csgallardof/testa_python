#Mi primer juego en Python 
#Player 1 = computadora 
#Player 2 = usuario - dijitar en consola 


#Objetivo: jugar piedra papel o tijera con el computador 
#Primer opcion: piedra gana tijera
#segunda opcion: tijera gana a papel 
#Tersera opcion: papel gana a piedra
#Numero intentos 10 
# el valor de computador debe ramdom 



import random

opciones = ["Piedra", "Papel", "Tijera"]
intentos = 10

def jugar():
  eleccion_jugador = input("Elige (Piedra, Papel o Tijera): ").lower()
  eleccion_computadora = random.choice(opciones)
  print(f"Tú: {eleccion_jugador} vs Computadora: {eleccion_computadora}")
  

  
def determinar_ganador(eleccion_jugador1, eleccion_computadora):
 
  gana_piedra = "Piedra gana a Tijera"
  gana_papel = "Tijera gana a Papel"
  gana_tijera = "Papel gana a Piedra"

  if eleccion_jugador1 == eleccion_computadora:
    resultado = "Empate!"
  elif eleccion_jugador1 == "Piedra" and eleccion_computadora == random.choice(opciones):
    resultado = gana_piedra 
  elif eleccion_jugador1 == "Papel" and eleccion_computadora == random.choice(opciones):
    resultado = gana_papel
  elif eleccion_jugador1 == "Tijera" and eleccion_computadora == random.choice(opciones):
    resultado = gana_tijera
    return 'ganaste '
  else:
    return 'Perdiste'
    

while intentos:
  jugar()
  intentos -= 1
  print(f"Te quedan {intentos} intentos.")
