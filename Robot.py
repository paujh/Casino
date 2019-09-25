#Robot que se mueve por el espacio dado
#Haremos una funcion de suma de vectores
def suma(a,b):
  suma = [a[0]+b[0],a[1]+b[1]]
  return suma
#Primero marcamos las dimensiones
X = int(input("¿De cuantas unidades es el largo de su espacio? "))
Y = int(input("¿De cuantas unidades es el ancho de su espacio? "))
print("La dimension de su espacio es (" + str(X) + "," + str(Y) + ")" )
#Empezaremos en la esquina inferior izquierda, que sera nuestra posicion (1,1)
p_actual = [1,1]

seguir = True
while seguir == True:
  mov = input("¿Hacia donde se quiere mover? S(arriba), A(abajo), D(derecha), I(izquierda), E(salir): ")
  if mov == "S":
    m = [1,0]
    p_actual = suma(p_actual,m)
    if p_actual[0]>0 and X>=p_actual[0]: 
      print("Su posicion actual es: " + str(p_actual))
    else: 
      m = [-1,0]
      p_actual = suma(p_actual,m)
      print("No se puede realizar dicho movimiento, su posicion actual es: " + str(p_actual))
  elif mov == "A":
    m = [-1,0]
    p_actual = suma(p_actual,m)
    if p_actual[0]>0 and X>=p_actual[0]: 
      print("Su posicion actual es: " + str(p_actual))
    else: 
      m = [1,0]
      p_actual = suma(p_actual,m)
      print("No se puede realizar dicho movimiento, su posicion actual es: " + str(p_actual))
  elif mov == "D":
    m = [0,1]
    p_actual = suma(p_actual,m)
    if p_actual[1]>0 and Y>=p_actual[1]: 
      print("Su posicion actual es: " + str(p_actual))
    else: 
      m = [0,-1]
      p_actual = suma(p_actual,m)
      print("No se puede realizar dicho movimiento, su posicion actual es: " + str(p_actual))
  elif mov == "I":
    m = [0,-1]
    p_actual = suma(p_actual,m)
    if p_actual[1]>0 and Y>=p_actual[1]: 
      print("Su posicion actual es: " + str(p_actual))
    else: 
      m = [0,1]
      p_actual = suma(p_actual,m)
      print("No se puede realizar dicho movimiento, su posicion actual es: " + str(p_actual))
  elif mov == "E":
    seguir = False 
print("Adios.")
