import random as r
#Dados. Usuario vs Computadora
#Pedimos la apuesta al usuario.
#Recordemos que un dado tiene 6 caras, y se tiraran 2 dados
#Definiremos dos listas, una sera el tiro del usuario y otra el tiro de la computadora. Asi como tambien dos sumas, que seran los puntos totales tanto del usuario como de la maquina
tiro_u = []
suma_u = 0
tiro_c = []
suma_c = 0
jugar = True
while jugar == True:
  apuesta = float(input("Ingrese su apuesta: "))
  if apuesta > 0.0:
    for i in range (2):
      tiro_u.append(r.randint(1,6))
    suma_u = tiro_u[0] + tiro_u[1]  
    for i in range (2):
      tiro_c.append(r.randint(1,6))
    suma_c = tiro_c[0] + tiro_c[1]
    print("Su tiro fue igual a: " + str(tiro_u))
    print("El tiro de la computadora fue igual a: " + str(tiro_c))
    if suma_u>suma_c:
      print("Tu ganas, ahora tienes " + str(apuesta*2))
    elif suma_u==suma_c:
      print("Empate, recuperas tu dinero.")
    else:
      print("Pierdes.")
    seguir = input("Deseas seguir jugando? SI o NO ")
    if seguir == "NO":
      jugar = False
  else: 
    print("Error al ingresar su apuesta, intente de nuevo")
print("Fin del juego.")
