#Las preguntas que te irá haciendo la esfinge corresponden a los print de esta plantilla
#Por favor completa cada reto

#Clase 1 Proyecto: Definidendo la aventura

#Reto 1 - Pon tu respuesta después del print
print("Define el equipamiento para una aventura de trekking y su valor en trekjuls (moneda del juego):")

mapa = 70.67
botas = 120.23
bateria = 11.69
linterna = 28
radio = 28
pilas = 10.6
agua = 73
botella = 20.5
snacks = 8.8
cuchillo = 10.4
brujula = 60.99
cuerdas = 90.5

objetos = [
  mapa,
  botas,
  bateria,
  linterna,
  radio,
  pilas,
  agua,
  botella,
  snacks,
  cuchillo,
  brujula,
  cuerdas,
]

# Ordenamos la lista objetos de menor a mayor
objetos.sort()

#Reto 2 - Pon tu respuesta después de cada print
print("Lista tres objetos del equipamiento: Nombre y valor")

print('cantinplora:', botella)
print('radio:', radio)
print('bateria:', bateria)



print("¿Puedes combinar elementos de tu equipo para prepararte mejor?")

radio_funcional = radio + pilas
linterna_funcional = linterna + bateria
agua_embotellada = botella + agua





print("¿El precio del agua en botella es menor al de la linterna funcional?")
print(agua_embotellada < linterna_funcional)



print("¿Cuanto valdría comprar unos snacks y una brujula?")
print(snacks + brujula)





print("¿Si tienes 100 puntos, te alcanza para comprar unas botas?")
print(botas <= 100)





#Clase 2 Proyecto: Tomando decisiones

#Reto 3 - Pon tu respuesta después del print
print("La esfinge te dice: No debes colocar más de 5 objetos en tu mochila, y tampoco pasarte de 200 trekjuls: ¿Cuales elementos colocarías?")


lista_cinco = []
precio_5_objetos = 0

for i in range(0, 5, 1):
  precio_5_objetos += objetos[i]
  lista_cinco.append(objetos[i])

if precio_5_objetos <= 200:
  print('')
  print(f'Los precios de los 5 elemntos son: ', lista_cinco)
  print(f'Las suma de los precios es: {precio_5_objetos}')
  print('')
else:
  print('')
  print('No es posible elegir 5 elementos y que la suma de sus precios sea menor o igual a 200')
  print('')





#Reto 4 - Pon tu respuesta después del print
print ("Es tu dia de suerte! Te voy a dar otra mochila, pero solo puedes agregarle agua en botella")

####### Por si se quiere búscar en el arreglo
objetos.append(agua_embotellada)
objetos.sort()

agua_embotellada = 93.5

mochila_dos = 0

while mochila_dos <= 200:
  mochila_dos += agua_embotellada

if mochila_dos <= 0:
  print('----------------')
  print('Una sola agua embotellada cuesta mas de 200')
  print('----------------')
else:
  mochila_dos -= agua_embotellada
  print('----------------')
  print('Mochila dos: ', mochila_dos)
  print('----------------')


#Clase 3 Proyecto: Almacenando equipamimento

#Reto 4 - Pon tu respuesta después del segundo print
print("Le hice una actualización a tu mochila te dice la esfinge, porque solo podias conocer el valor de los objetos que tenias")
print("Ahora sabrás el objeto que tienes, la cantidad y su valor unitario, pero tu debes volverla a llenarla")



mochila_actualizada = {
  'radio_funcional': {'cantidad': 1, 'valor_unitario': radio_funcional},
  'linterna_funcional': {'cantidad': 1, 'valor_unitario': linterna_funcional},
  'agua_embotellada': {'cantidad': 1, 'valor_unitario': agua_embotellada}
}

mochila_dos_actualizada = {
  'agua_embotellada' : {'cantidad': 2, 'valor_unitario': agua_embotellada}
}





#Reto 5 - Pon tu respuesta después del print
print("Ahora, en esta aventura te van a acompañar 8 integrantes más, y te voy a pedir que les armes una mochila igual a la tuya y la coloques en el compartimiento de tu vehiculo")


compartimiento = []

for comp in range(1, 9, 1):
  compartimiento.extend(mochila_actualizada)
  
print('---------------------------')
print(compartimiento)
print('---------------------------')


#Clase 4 Proyecto: Organizandonos un poco

#Reto 6 - Pon tu respuesta después del segundo print
print("Te pido que para cuatro integrantes recolectes 3 elementos sin importar las cantidades que quieras adicionarles, y te da las siguientes opciones: brujula, linterna_funcional, snacks y agua_en_botella")
print("Pero necesito que calcules el total de elementos que hay en tu equipo")


integrantes = [
  {
    'agua_embotellada': 5,
    'snacks': 3,
    'linterna_funcional': 1
  },
  {
    'agua_embotellada': 4,
    'snacks': 2,
    'linterna_funcional': 2
  },
  {
    'agua_embotellada': 3,
    'snacks': 1,
    'linterna_funcional': 2
  },
  {
    'agua_embotellada': 1,
    'snacks': 1,
    'linterna_funcional': 1
  }
]

def funcionCuatroInte(integrantes):
  lista_valores = []
  contador_elementos = 0

  for integrante in integrantes:
    lista_valores.extend(integrante.values())

  for ele in lista_valores:
    contador_elementos += ele
  
  print('##########')
  print('La suma de elemtos de los 4 integrantes es: ', contador_elementos)
  print('##########')

funcionCuatroInte(integrantes)



