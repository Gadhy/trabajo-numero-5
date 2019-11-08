#Hallamos la presión

#INPUT
fuerza= float(input("ingrese fuerza: "))
area= float(input("ingrese area: "))

#PROCESSING
presion= fuerza/area

#VERIFICACION
verficiador_presion= (presion<12)

#OUTPUT
print("la presion es", presion)
print("la presion es menor a 12?", verficiador_presion)
