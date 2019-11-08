#Hallamos la cantidad de calor

#INPUT
masa= float(input("ingrese masa: "))
calor_latente= float(input("ingrese fuerza: "))

#PROCESSING
cantidad_de_calor= masa*calor_latente

#VERIFICACION
verificador_cantidad_calor= (cantidad_de_calor==321)

#OUTPUT
print("la cantidad de calor es", cantidad_de_calor)
print("la cantidad de calor es igual a 321?", verificador_cantidad_calor)
