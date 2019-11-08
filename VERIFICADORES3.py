#Hallamos la cantidad de movimiento

#INPUT
masa= float(input("ingrese masa: "))
velocidad= float(input("ingrese velocidad: "))

#PROCESSING
cantidad_de_movimiento= masa*velocidad

#VERIFICACION
verificador_cantidad_de_movimiento= (cantidad_de_movimiento<20)

#OUTPUT
print("la cantidad de movimiento es", cantidad_de_movimiento)
print("la cantidad de movimiento es la requerida?",verificador_cantidad_de_movimiento)
