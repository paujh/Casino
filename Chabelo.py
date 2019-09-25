#Chabelo
import random as r
#Primero, el usuario tiene que ingresar la cantidad que quiere apostar
a_inicial = float(input("¿Cuanto es tu apuesta?  " ))
#Esta sera la lista de lo que puede sacar el juego
arreglo = [1,2,3,4,5,"x"]
#Haremos una lista vacia para que sea lo que vaya sacando el usuario
l = []
#Tendra 3 vidas, ya que solo puede sacar 3 "x"
vidas = 3
#Comenzamos el juego, con un elemento que sera el que sacara por vez, y con un switch que cambiara cuando ya no quiera jugar o cuando pierda.
elemento = 0.0
jugar = True 
while jugar == True:
  seguir = input("¿Deseas seguir jugando? SI o NO  ")
  if seguir == "SI":
    if a_inicial>0.0:
      l.append(r.choice(arreglo))
      print(l)
      elemento = l[len(l)-1]
      if elemento == "x":
        print("Pierdes una vida.")
        vidas = vidas - 1
        if vidas > 0:
          print("Puedes seguir jugando")
        else: 
          jugar = False
      else: 
        arreglo.remove(elemento)
        if arreglo[0] == "x":
          print("Ganaste. Ahora tienes " + str(a_inicial*2))
          jugar = False
    else: 
      jugar = False
  else: 
    jugar = False
print("Fin del juego.")
