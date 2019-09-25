#Programa que calcula el interes compuesto 
#Primero le pediremos todos los datos necesarios al usuario
Capital = float(input("Ingrese el capital con el que cuenta: "))
Tiempo = int(input("Ingrese los años que tendra invertido el capital: "))
i_anual = float(input("Ingrese el interes que usara, en porcentaje: "))
#Ahora haremos que se calcule el interes por año y que muestre la ganancia, año por año.
interes = 0.0
for i in range (Tiempo+1):
  interes = Capital*((1+(i_anual/100))**i)
  print("\nSu dinero total en el año " + str(i) + " sera de $" + str(interes) + ", mientras que su ganancia con respecto a su capital inicial sera de $" + str(interes-Capital))
