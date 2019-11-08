#INPUT
constante_elastica_del_resorte= float(input("CONSTANTE ELASTICA DEL RESORTE: "))
deformacion_del_resorte= float(input("DEFORMACION DEL RESORTE: "))

#PROCESSING
fuerza_elastica= constante_elastica_del_resorte*deformacion_del_resorte

#OUTPUT
print("===================================================================================")
print("============================= FUERZA ELASTICA =====================================")
print("===================================================================================")
print("=============== constante elastica del resorte:", constante_elastica_del_resorte,"==============")
print("=============== deformacion del resorte:", deformacion_del_resorte,"============================")
print("=============== fuerza elastica:", fuerza_elastica,"===============================================")
print("===================================================================================")
