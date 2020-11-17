# Bibliotecas
import RPi.GPIO as GPIO
import time

# Colocar GPIO no modo de números
GPIO.setmode(GPIO.BOARD)

# Setar os pinos 11 e 12 como saídas e definir o PWM dos servos
GPIO.setup(11,GPIO.OUT)
# Pino 11 para o servo1
servo1 = GPIO.PWM(11,50) 
# Pino 12 para o servo2
GPIO.setup(12,GPIO.OUT)
servo2 = GPIO.PWM(12,50)

 

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
        # Colocar servo1 em 90º
        servo1.ChangeDutyCycle(7)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(7)
        if mancha_laranja==0:
            # Colocar servo2 em 90º
            servo2.ChangeDutyCycle(7)
            time.sleep(0.5)
            servo2.ChangeDutyCycle(7)
            print("boa e sem mancha")
        else:
            # Colocar servo2 em 180º
            servo2.ChangeDutyCycle(12)
            time.sleep(0.5)
            servo2.ChangeDutyCycle(7)
            print("boa com mancha")
    else:
        # Colocar servo1 em 180º
        servo1.ChangeDutyCycle(12)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(7)
        print("TA PODREEEEE")
 

#Limpar variáveis e finalizar o módulo
servo1.stop()
servo2.stop()
GPIO.cleanup()