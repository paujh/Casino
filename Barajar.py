import random as r
#Barajar
#Primero definiremos la lista con todas las cartas de la baraja
#P(picas), C(corazones), D(diamantes), T(treboles)
baraja = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','PJ','PQ','PK','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK','D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK','T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','TJ','TQ','TK']
baraja_revuelta = []
elemento = ""
#Ahora haremos una funcion que anexe un elemento aleatorio de la baraja, a una revuelta, y viceversa, por 7 veces.
for i in range(7):
  if i%2 == 0:
    for j in range(len(baraja)):
      baraja_revuelta.append(r.choice(baraja))
      elemento = baraja_revuelta[len(baraja_revuelta)-1]
      baraja.remove(elemento)
  else:
    for j in range(len(baraja_revuelta)):
      baraja.append(r.choice(baraja_revuelta))
      elemento = baraja[len(baraja)-1]
      baraja_revuelta.remove(elemento)
#Al final sólo queda la baraja revuelta con todos los elementos
print(baraja_revuelta)
