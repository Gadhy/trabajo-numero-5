#Hallamos la variación de energía interna

#INPUT
cantidad_de_calor= float(input("ingrese c. de calor: "))
trabajo= float(input("ingrese trabajo: "))

#PROCESSING
variacion_de_energia_interna= cantidad_de_calor*trabajo

#VERIFICADOR
verificador_variación_de_energía_interna= (variacion_de_energia_interna>100)

#OUTPUT
print("la variacion de la energia interna es",variacion_de_energia_interna)
print("la variacion es mayor a 100?",verificador_variación_de_energía_interna)
