#Bingo
import random as r
#Primero le pedimos al usuario que llene su carta, supondremos que hara caso a las indicaciones de poner los numeros entre 1 y 50
carta_u = []
for i in range(9):
    i = int(input("Ingresa un número del 1 al 50 (NO repitas números): "))
    carta_u.append(i)
print("Tu carta es: " +str(carta_u))
#Ahora llenamos la carta de la Computadora
carta_c = []
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
ele = 0
for i in range (9):
  carta_c.append(r.choice(numeros))
  ele = carta_c[len(carta_c)-1] 
  numeros.remove(ele)
print("La carta de la computadora es: " + str(carta_c))
#Haremos una lista con los 50 números, y una lista donde se irán agregando los numeros que ya salieron
numeros2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
numeros_s = []
#comparación de el primer número de la lista números con los datos de las cartas del usuario y máquina
d = 0
p = 0
jugar = True
elemento = 0
while jugar == True:
  seguir = input("¿Deseas seguir jugando? SI o NO ")
  if seguir == "SI":  
    numeros_s.append(r.choice(numeros2))
    print("Han salido los numeros" + str(numeros_s))
    elemento = numeros_s[len(numeros_s)-1]
    numeros2.remove(elemento)
    for i in range(len(carta_u)-1):
      if elemento == carta_u[i]:
        carta_u.remove(elemento)
        p = p + 1
        print("Ahora tienes " + str(p) + " puntos")
      else:
        pass
    for j in range(len(carta_c)-1):
      if elemento == carta_c[j]:
        carta_c.remove(elemento)
        d = d + 1
        print("Ahora la computadora tiene " + str(d) + " puntos")
      else:
        pass
    if d<p and p == 9:
      print("¡Ganaste!")
      jugar = False
    elif p<d and d == 9:
      print("Gana la computadora.")
      jugar = False  
  elif jugar == "NO":
    jugar = False    
print("Fin del juego.")
