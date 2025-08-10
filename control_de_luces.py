#Importo librerias
from machine import PWM, Pin #Importo los elementos de la libreria correspondientes para utilizar pines y PWM
from time import sleep #Importo el modulo sleep para poder utilizar delays en el programa


#Defino las variables necesarias
brightness = 0 #Defino el porcentaje de brillo de la luz
brightness_prev = 0 #Defino porcentaje de brillo anterior
step = 5 #Defino la cantidad de pasos para alcanzar el brillo deseado
pin_light_number = 12 #Defino el pin en el que se encuentra conectada la luz


#Defino parametros del PWM (Pulso con modulacion)
frec = 5000 #cantidad de pulsos por segundo, se utiliza 5kHz por un estandar


#Creo el Pin
pinLuz = Pin(pin_light_number, Pin.OUT)


#Creo funciones para manipular el duty de forma porcentual
def percent_to_duty(percent): #Convierte los porcentajes a valor duty
    
    #Primero, evito valores negativos y superiores al 100%
    if percent <= 0:
        percent = 0
    elif percent >= 100:
        percent = 100
    
    #Retorno el valor convertido en un valor duty
    return int((percent * 65535) / 100)


def duty_to_percent(duty): #convierte valores duty en valores porcentuales
    
    #Primero, evito valores negativos y superiores al 100%
    if duty < 0:
        duty = 0
    elif duty > 65535:
        duty = 65535

    #Retorno el valor convertido en un valor porcentual
    return int((duty * 100) / 65535)


#Configuracion inicial del PWM
pwm = PWM(pinLuz)
pwm.freq(frec)


#Defino una funcion para controlar el brillo de la luz
def change_brightness(percent):
    duty = percent_to_duty(percent)
    pwm.duty_u16(duty)


# Función para hacer un cambio suave de brillo
def fade_brightness(start_percent, end_percent, duration_seconds):
    steps = 50  # Cantidad de pasos para hacer el cambio
    delay = duration_seconds / steps  # Tiempo entre cada paso
    
    # Calcula el cambio por paso
    step_change = (end_percent - start_percent) / steps
    
    # Realiza el cambio gradual
    for i in range(steps + 1):
        current_brightness = start_percent + (step_change * i)
        change_brightness(int(current_brightness))
        sleep(delay)


#Bucle infinito
while True:

    #Realiza un cambio suave del brillo
    if not brightness  == brightness_prev:        
        fade_brightness(brightness_prev, brightness, step)

    