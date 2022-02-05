import requests
import json
import datetime
import pandas as pd
import re
class GeoAPI:
	#1
	API_KEY = "d81015613923e3e435231f2740d5610b"
	LAT = "-35.836948753554054"
	LON = "-61.870523905384076"
	
	@classmethod
	#1
	#Función de verificación de temperatura
	def is_hot_in_pehuajo(self,cls):

		if cls > 28:
			respuesta= True
		else:
			respuesta= False
		return respuesta
#2
class Pedido:
	
	#Se crea estructura de dato Dataframe
	_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate",
	"Granizado", "Limon", "Dulce de Leche"], "quantity":
	[3,10,0,5]})
	#Se inicializa variable respuesta
	respuesta = [False,"Control de Stock"]



	@classmethod
	#2
	def is_product_available(self,product_name, quantity):
		#Se busca el producto dentro del dataframe
		existeProducto =  self._PRODUCT_DF[(self._PRODUCT_DF["product_name"]==product_name)]

		if len(existeProducto)>0:
			#Se verifica si existe stock para ese producto
			existeStock = self._PRODUCT_DF[(self._PRODUCT_DF["product_name"]==product_name)&(self._PRODUCT_DF["quantity"]>=quantity)]
			#print(existeStock)
			if len(existeStock) > 0:
				respuesta = [True,"Stock Disponible para el producto %s"%(product_name)]
			else:
				respuesta = [False,"Stock No Disponible para el producto %s"%(product_name)]
		else:
			respuesta = [False,"Producto '%s' Inexistente"%(product_name)]
		#Retorna el resultado de la función
		return respuesta
	
	

#3
class Descuento:

	#3
	_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021",
	"Navidad2x1", "heladoFrozen"]
	respuesta = [False,"Código de Descuento"]

	@classmethod
	#3
	def validate_discount_code(self,discount_code):
		#Recorre lista inicial 
		for i in range(len(self._AVAILABLE_DISCOUNT_CODES)):
			#Se definen variables
			diferencia = 0
			listaLetra=[]
			listaLetra2=[]

			#Se toma el código en cada iteracion del for
			codigoDisponible = self._AVAILABLE_DISCOUNT_CODES[i]
			
			#Se recorre cada letra de cada codigo disponible
			for letra in codigoDisponible:
				#Si no se encuentra letra en el cod ingresado por usuario
				if letra not in(discount_code):
					#Si la letra aun no fue agregada como diferencia
					if letra not in(listaLetra):
						#incrementa en 1 la diferencia
						diferencia = diferencia+1
						#agrega esa letra como ya descontada
						listaLetra.append(letra)

			#Se recorre cada letra del código ingresado por el usuario
			for letra2 in discount_code:
				#Si no se encuentra letra en el cod disponible
				if letra2 not in(codigoDisponible):
					#Si la letra aun no fue agregada como diferencia
					if letra2 not in(listaLetra2):
						#incrementa en 1 la diferencia
						diferencia = diferencia+1
						#agrega esa letra como ya descontada
						listaLetra2.append(letra2)
			
			#print(codigoDisponible,diferencia,listaLetra,listaLetra2,discount_code)
			#Si la diferencia en menor a 3 devuelve true y sale del for sino devuleve false
			#y continua con la proxima iteración.
			if diferencia <3:
				respuesta = [True,"Diferencia menor a 3"]
				break
			else:
				respuesta=[False,"La diferencia no cumple con las condiciones"]
		#la funcion devuelve el resultado
		return respuesta	

try:		
	#1=======================================================================
	print("HELADERIAS FROZEN - Toma de Pedidos")
	geoAPI =  GeoAPI()
	url = "https://api.openweathermap.org/data/2.5/weather"
	querystring = {"lat":geoAPI.LAT,"lon":geoAPI.LON,"appid":geoAPI.API_KEY,"units":"metric"}
	headers = {
	    'Cache-Control': 'no-cache'
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	if response.status_code == 200:
		data = json.loads(response.content)
		cls = data['main']['temp']
		print("Temperatura CLS: %s"%(cls))

		respuesta = geoAPI.is_hot_in_pehuajo(cls)

		if respuesta == True:
			print("Bienvenida 1 - Hoy es un hermoso día para disfrutar de nuestras cremas heladas")
		else:
			print("Bienvenida 2 - La temperatura está fresca aunque ideal para disfrutar de nuestras cremas heladas")
	else:
		print(False)
		print("Error en HTTP request: %s"%(response.status_code))

	#Fin #1========================================================================================

	#2=============================================================================================
	#Inicializa la ejecución del programa
	pedido = Pedido()
	print(pedido.respuesta[1])
	#Ejecuta el procedimiento mientras la variable respuesta sea Falsa
	while pedido.respuesta[0]==False:
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
			respuesta_2 = (pedido.is_product_available(product_name, int(quantity)))
			print(respuesta_2[1])
			pedido.respuesta[0]=respuesta_2[0]
			#Para darle solución al punto 2.2 se implementa esta parte del código
			#Si no existe stock se le consulta al usuario si quiere ingresar un nuevo producto 
			if pedido.respuesta[0] == False:
				bandera=""
				#Mientras la respuesta sea si el programa seguirá solicitando al usuario que ingrese
				#nuevos productos.
				#Si la respuesta del usuario es no, el programa se da por temrinado.
				while bandera != "Si" or bandera != "No":
					nvoProd = input("Desea ingresar un nuevo producto (Si/No): ")
					if nvoProd == "Si":
						bandera = "Si"
						pedido.respuesta[0] = False
						break
					elif nvoProd == "No":
						bandera = "No"
						break
					else:
						bandera=""
						print("Por favor ingrese Si o No")
				if bandera == "No":
					break
	if respuesta_2[0]==True:
		descuento = Descuento()
		print(descuento.respuesta[1])
		while descuento.respuesta[0]==False:
			#Se solicita al usuario que ingrese un código
			discount_code = input("Por favor ingrese su código de descuento: ")
			
			#Verifica que el usuario haya ingresado un nombre y un cantidad
			if discount_code != "":
				#Se ejecuta función y se recibe el resultado
				respuesta_3 = descuento.validate_discount_code(discount_code)
				print(respuesta_3[1])
				descuento.respuesta[0]=respuesta_3[0]
				#Si no existe la diferencia especificada se le consulta al usuario 
				#si quiere ingresar un nuevo producto 
				if descuento.respuesta[0] == False:
					bandera=""
					#Mientras la respuesta sea si el programa seguirá solicitando al usuario que ingrese
					#nuevos códigos.
					#Si la respuesta del usuario es no, el programa se da por temrinado.
					while bandera != "Si" or bandera != "No":
						nvoCod = input("Desea ingresar un nuevo código de descuento (Si/No): ")
						if nvoCod == "Si":
							bandera = "Si"
							descuento.respuesta[0] = False
							break
						elif nvoCod == "No":
							bandera = "No"
							break
						else:
							bandera=""
							print("Por favor ingrese Si o No")
					if bandera == "No":
						break


except Exception as e:
	#print("Except: %s"%(e.message))
	print("Except: %s"%(e.args))