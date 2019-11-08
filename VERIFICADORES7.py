#Hallamos la fuerza de fricción

#INPUT
coeficiente_de_roce= float(input("ingrese coeficiente: "))
fuerza_normal= float(input("ingrese fuerza: "))

#PROCESSING
fuerza_de_friccion= coeficiente_de_roce*fuerza_normal

#VERIFICACION
verificador_fuerza_friccion= (fuerza_de_friccion<120)

#OUTPUT
print("la fuerza de friccion es", fuerza_de_friccion)
print("la fuerza de fricion es menor a 120?", verificador_fuerza_friccion)
