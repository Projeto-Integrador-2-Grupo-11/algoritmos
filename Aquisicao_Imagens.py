#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Algoritmo do Módulo de Aquisição de Imagens

#Bibliotecas
import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
from os import system

#GPIO.BOARD configura os pinos
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)

#Conexão física do pino
sensor_ir = 23

#Configurando o pino como entrada
GPIO.setup(sensor_ir, GPIO.IN) 

#Configurando as câmeras
camera = PiCamera()
camera.start_preview()

while True:
    if GPIO.input(sensor_ir)==1:
    #Não há fruto na etapa de aquisição de imagem        
        time.sleep(0.1)
        print("Sensor IR:", sensor_ir)
        print("Fruto Não Detectado")
        
    elif GPIO.input(sensor_ir) == 0:
    #Detecção de fruto na etapa de aquisição de imagem 
    
    #Ativação dos módulos de câmera para aquisição de imagem
    #Inicializar câmera A
        i2c = 'i2cset -y 1 0x70 0x00 0x04'
        os.system(i2c)
        capture(1)
   
    #Inicializar câmera B    
        i2c_ = 'i2cset -y 1 0x70 0x00 0x05'
        os.system(i2c_)
        capture(2)
        
        print("Sensor IR:", sensor_ir)
        print("Fruto Detectado. Ativação câmera A. Ativação câmera B.")

#Função de Captura de Imagens        
def capture(cam):
    image_1 = "raspistill -o image_%d.jpg" % cam
    image_2 = "raspistill -o image_%d.jpg" % cam
    os.system(image_1, image_2)
    print("imagens capturadas.")

