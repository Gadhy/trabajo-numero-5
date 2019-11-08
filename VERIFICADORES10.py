#Hallamos la aceleración centrípeta

#INPUT
velocidad= float(input("ingrese velocidad: "))
radio= float(input("ingrese radio: "))

#PROCESSIING
aceleracion_centripeta= (velocidad**2)/radio

#VERIFICACION
verificador_aceleración_centrípeta= (aceleracion_centripeta==230)

#OUTPUT}
print("la aceleracion centripeta es", aceleracion_centripeta)
print("la aceleracion centripeta es 230?", verificador_aceleración_centrípeta)
