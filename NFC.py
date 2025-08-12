#Importo las librerías necesarias
from machine import Pin
import time
from nfc import NDEF, PN532_I2C


# Configuración I2C
i2c = machine.I2C(0, scl=Pin(22), sda=Pin(21), frec=100000)
nfc = PN532_I2C(i2c)


#Verificación de coincidencia entre los datos leidos con el sensor NFC y los datos almacenados en la DB
def if_match_data():
  
  #Acá iría la lectura de los datos de la base de datos
  #####################################################
  user_ids = [] #Coleccion donde se almacenarán todos los ids habilitados que la base de datos contenga sobre el usuario
  
  #Para cada id en la coleccion previamente definida
  for id in users_ids
  
    #Si el id coincide con la información leida en la tarjeta NFC
    if id == data:
      
      #Algoritmo de apertura de puertas
      ##################################
      

#Leo la tarjeta NFC NDEF. Tras leer reviso si la data recibida coincide con la base de datos
def read_ndef_message():
  
    #Espero por una tarjeta NFC, con un timeout de 0.5 segundos
    uid = nfc.read_passive_target(timeout=0.5)
    
    #Si se detectan tarjetas NFC:
    if uid:
       
       #Leo la tarjeta completa y lo almaceno en la variable msg 
        msg = nfc.read_ndef_message()
        
        #Tras Leer el mensaje
        if msg:
          
            #Para cada registro en los registros de la tarjeta NDEF
            for record in msg.records:
                
                #Si hay un registro de tipo texto
                if record.type == 'text':
                    
                    #Retorno como valor de la función el texto
                    data = record.text
                    if_match_data() #Llamo a la funcion que se encarga de comprobar que los datos coincidan con la DB


#Bucle de revisión de tarjeta NFC
while True:
  
  #Leo esperando una tarjeta NFC
  read_ndef_message()