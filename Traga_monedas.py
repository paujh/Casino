import random as r 
#Traga monedas 
#Primero hacemos una funcion para que gire el traga monedas
def girar():
  l = []
  for i in range (3):
    l.append(r.randint(1,7))
  return l
#Comenzamos con el juego pidiendo al usuario que interactue
C_inicial = float(input("Su cantidad inicial es: "))
seguir = True
#Ahora haremos el juego, tantas veces como el usuario quiera, mientras tenga dinero suficiente.
while seguir == True:
  jugar = input("¿Desea seguir jugando? SI o NO ")
  if jugar == "SI":
    if C_inicial>0.0:
      Apuesta = float(input("Su apuesta es : "))
      C_inicial = C_inicial - Apuesta
      if C_inicial>=0.0:
        A = girar()
        print(A)
        if A[0]==A[1] and A[1]==A[2]:
          if A[0]==1:
            C_inicial = C_inicial + Apuesta
            print("Su cantidad restante es: " +  str(C_inicial))
          if A[0]==2:
            C_inicial = C_inicial + Apuesta + (Apuesta*(1/6))
            print("Su cantidad restante es: " +  str(C_inicial))
          if A[0]==3:
            C_inicial = C_inicial + Apuesta + (Apuesta*(2/6))
            print("Su cantidad restante es: " +  str(C_inicial))
          if A[0]==4:
            C_inicial = C_inicial + Apuesta + (Apuesta*(3/6))
            print("Su cantidad restante es: " +  str(C_inicial))
          if A[0]==5:
            C_inicial = C_inicial + Apuesta + (Apuesta*(4/6))
            print("Su cantidad restante es: " +  str(C_inicial))
          if A[0]==6:
            C_inicial = C_inicial + Apuesta + (Apuesta*(5/6))
            print("Su cantidad restante es: " +  str(C_inicial))
          if A[0]==7:
            C_inicial = C_inicial + (Apuesta*2) 
            print("Su cantidad restante es: " +  str(C_inicial))
        else:
          print("Su cantidad restante es: " + str(C_inicial))
      else:
        print("Su apuesta no puede ser ejecutada.")  
    else: 
      print("Su apuesta no puede ser ejecutada")
      Apuesta = float(input("Su apuesta es : "))
      C_inicial = C_inicial - Apuesta
  elif jugar == "NO":
    seguir = False
print("Fin del juego.")
