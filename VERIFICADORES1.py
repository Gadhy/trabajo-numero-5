#Hallamos la energía potencial elástica

#INPUT
constante_elastica_del_resorte= float(input("ingrese constante: "))
deformacion_del_resorte= float(input("ingrese deformacion: "))

#PROCESSING
energia_potencial_elastica= (1/2*constante_elastica_del_resorte)*deformacion_del_resorte**2

#VERIFICADOR
verificador_energía_potencial_elástica=(energia_potencial_elastica==40)

#OUTPUT
print("la energia potencial elastica es",energia_potencial_elastica)
print("la energia potencial elastica es igual a 40? ",verificador_energía_potencial_elástica)






