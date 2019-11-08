#Hallamos el área del rombo

#INPUT
diagonal_mayor= float(input("ingrese DM: "))
diagonal_menor= float(input("ingrese Dm: "))
#PROCESSING
area= (diagonal_mayor*diagonal_menor)/2

#VERIFICACION
verificador_area_rombo= (area>45.8)

#OUTPUT
print("el area es",area)
print("el area es mayor a 45.8?", verificador_area_rombo)
