import random as r
#Ruleta
#Aqui supondremos que todas las apuestas que ingresen, seran mayores a 0, que el usuario acatara ordenes e ingresara numeros entre 1 y 36
seguir = True
while seguir == True:
  juego = True
  numeros = []
  apuestas = []
  while juego == True:
    numeros.append(int(input("Ingrese número a apostar entre 1 y 36: ")))
    apuestas.append(float(input("Ingrese su apuesta para dicho numero: ")))
    jugar = input("¿Quieres apostar otro numero? SI o NO ")
    if jugar == "SI":
      juego = True
    elif jugar == "NO":
      juego = False
      print("Aposto por los números: " + str(numeros))
    m = len(numeros)
  elemento = r.randint(0,36)
  print("En la ruleta salio el número " + str(elemento))
  for i in range(m):
    if elemento == numeros[i]:
      p = apuestas[i]*2
      print("Tienes un número ganador, el " + str(numeros[i]) + " ganaste: " + str(p))
    else:
      print("El numero "+str(numeros[i])+" no te hizo ganar")
      p=0 
  jugar = input("¿Quiere volver a jugar? SI o NO ")
  if jugar == "SI":
    seguir = True
  elif jugar == "NO":
    seguir = False
print("Fin del juego")
