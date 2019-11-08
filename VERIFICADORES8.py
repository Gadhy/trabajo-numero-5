#Hallamos el impulso

#INPUT
fuerza=float(input("ingrese fuerza: "))
variacion_del_tiempo=float(input("ingrese variacion: "))

#PROCESSING
impulso= fuerza*variacion_del_tiempo

#VERIFICADOR
verificador_impulso= (impulso>97)

#OUTPUT
print("el impuslo es", impulso)
print("el impuslo es mayor a 97?", verificador_impulso)
