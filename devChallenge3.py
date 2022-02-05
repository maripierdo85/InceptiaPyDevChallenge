_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021",
"Navidad2x1", "heladoFrozen"]
respuesta = [False,"Código de Descuento"]
def validate_discount_code(discount_code):
	#Recorre lista inicial 
	for i in range(len(_AVAILABLE_DISCOUNT_CODES)):
		#Se definen variables
		diferencia = 0
		listaLetra=[]
		listaLetra2=[]

		#Se toma el código en cada iteracion del for
		codigoDisponible = _AVAILABLE_DISCOUNT_CODES[i]
		
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

print(respuesta[1])
while respuesta[0]==False:
	#Se solicita al usuario que ingrese un código
	discount_code = input("Por favor ingrese su código de descuento: ")
	
	#Verifica que el usuario haya ingresado un nombre y un cantidad
	if discount_code != "":
		#Se ejecuta función y se recibe el resultado
		respuesta = validate_discount_code(discount_code)
		print(respuesta[1])
		#Si no existe la diferencia especificada se le consulta al usuario 
		#si quiere ingresar un nuevo producto 
		if respuesta[0] == False:
			bandera=""
			#Mientras la respuesta sea si el programa seguirá solicitando al usuario que ingrese
			#nuevos códigos.
			#Si la respuesta del usuario es no, el programa se da por temrinado.
			while bandera != "Si" or bandera != "No":
				nvoCod = input("Desea ingresar un nuevo código de descuento (Si/No): ")
				if nvoCod == "Si":
					bandera = "Si"
					respuesta[0] = False
					break
				elif nvoCod == "No":
					bandera = "No"
					break
				else:
					bandera=""
					print("Por favor ingrese Si o No")
			if bandera == "No":
				break


"""
Ejemplo:
"primavera2021" deberia devolver True, ya que al compararlo:
vs "Primavera2021" = 2 caracteres de diferencia ("p" y "P")
vs "Verano2021" = 7 caracteres de diferencia ('i', 'n', 'o',
'm', 'V', 'p', 'v')
vs "Navidad2x1" = 8 caracteres de diferencia ('N', 'm', '0',
'x', 'e', 'd', 'p', 'r')
vs "heladoFrozen" = 14 caracteres de diferencia ('z', 'i',
'v', 'n', 'o', 'm', '2', '0', 'd', 'p', '1', 'F', 'h', 'l')
"""
