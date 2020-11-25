# Bibliotecas

import time

import FakeRPi.GPIO as GPIO

# Colocar GPIO no modo de números
GPIO.setmode(GPIO.BOARD)

# Setar os pinos 18 e 22 como saídas e definir o PWM dos servos
GPIO.setup(18,GPIO.OUT)
# Pino 18 para o servo1
servo1 = GPIO.PWM(18,50) 
# Pino 22 para o servo2
GPIO.setup(22,GPIO.OUT)
servo2 = GPIO.PWM(22,50)

 

#Variáveis recebidas pelo software de processamento de imagem
qualidade_laranja = 0 # 0 - laranjas boas / 1 - laranjas podres
mancha_laranja = 1 # 0 - sem manchas / 1 - com manchas
 

# Iniciar PWM  dos servos com o valor 0º (pulse off)
# Os servos são inicializados na posição da seguinte rota: fruto bom e sem mancha
servo1.start(0)
servo2.start(0)

#Iniciar seleção de rotas 

while True:
    if qualidade_laranja==0:
        # Colocar servo1 em 0º
        servo1.ChangeDutyCycle(0)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
        if mancha_laranja==0:
            # Colocar servo2 em 0º
            servo2.ChangeDutyCycle(0)
            time.sleep(0.5)
            servo2.ChangeDutyCycle(0)
            print("Laranja boa e sem mancha")
        else:
            # Colocar servo2 em 60º
            servo2.ChangeDutyCycle(5)
            time.sleep(0.5)
            servo2.ChangeDutyCycle(5)
            print("Laranja boa com mancha")
    else:
        # Colocar servo1 em 60º
        servo1.ChangeDutyCycle(5)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(5)
        print("Laranja podre")
 
#Limpar variáveis e finalizar o módulo
servo1.stop()
servo2.stop()
GPIO.cleanup()
