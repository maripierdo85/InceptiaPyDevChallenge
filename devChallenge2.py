#Se importan la slibrerias a utilizar
import pandas as pd
import re

#Se crea estructura de dato Dataframe
_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate",
"Granizado", "Limon", "Dulce de Leche"], "quantity":
[3,10,0,5]})

#Se inicializa variable respuesta
respuesta = [False,"Control de Stock"]

#Se define la función is_product_available
def is_product_available(product_name, quantity):
	#Se busca el producto dentro del dataframe
	existeProducto =  _PRODUCT_DF[(_PRODUCT_DF["product_name"]==product_name)]

	if len(existeProducto)>0:
		#Se verifica si existe stock para ese producto
		existeStock = _PRODUCT_DF[(_PRODUCT_DF["quantity"]>=quantity)]
		if len(existeStock) > 0:
			respuesta = [True,"Stock Disponible para el producto %s"%(product_name)]
		else:
			respuesta = [False,"Stock No Disponible para el producto %s"%(product_name)]
	else:
		respuesta = [False,"Producto '%s' Inexistente"%(product_name)]
	#Retorna el resultado de la función
	return respuesta

#Inicializ ala ejecución del programa
print(respuesta[1])
#Ejecuta el procedimiento mientras la variable respuesta sea Falsa
while respuesta[0]==False:
	banderaEsNro=False
	while banderaEsNro == False:
		#Se solicita el ingreso de datos al usuario
		product_name = input("Por favor ingrese el nombre de un producto: ")
		quantity = input("Por favor ingrese la cantidad que necesita: ")
		#Verifica que la cantidad ingresada sea un dato numérico, sino se la vuelve a solicitar
		num_format = re.compile(r'^\-?[1-9][0-9]*$')
		esNumero = re.match(num_format,quantity)
		if esNumero != None: 
			banderaEsNro=True
		else: 
			banderaEsNro=False
			print("Ingrese un valor numérico para la cantidad")
	#Verifica que el usuario haya ingresado un nombre y un cantidad
	if product_name != "" and int(quantity) != 0:
		#Ejecuta la función y espera la respuesta
		respuesta = (is_product_available(product_name, int(quantity)))
		print(respuesta[1])
		#Para darle solución al punto 2.2 se implementa esta parte del código
		#Si no existe stock se le consulta al usuario si quiere ingresar un nuevo producto 
		if respuesta[0] == False:
			bandera=""
			#Mientras la respuesta sea si el programa seguirá solicitando al usuario que ingrese
			#nuevos productos.
			#Si la respuesta del usuario es no, el programa se da por temrinado.
			while bandera != "Si" or bandera != "No":
				nvoProd = input("Desea ingresar un nuevo producto (Si/No): ")
				if nvoProd == "Si":
					bandera = "Si"
					respuesta[0] = False
					break
				elif nvoProd == "No":
					bandera = "No"
					break
				else:
					bandera=""
					print("Por favor ingrese Si o No")
			if bandera == "No":
				break
		

