#Hallamos el empuje

#INPUT
densidad= float(input("ingrese densidad: "))
aceleracion_por_la_gravedad= float(input("ingrese aceleracion: "))
volumen_del_liquido_desplazado= float(input("ingrese volumen: "))

#PROCESSING
empuje= (densidad*aceleracion_por_la_gravedad)*volumen_del_liquido_desplazado

#VERIFICACION
verificador_empuje= (empuje>35)

#OUTPUT
print("el empuje es", empuje)
print("el empuje es mayor a 35?", verificador_empuje)
