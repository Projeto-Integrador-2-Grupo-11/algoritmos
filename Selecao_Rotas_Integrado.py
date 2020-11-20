# Bibliotecas
import RPi.GPIO as GPIO
import time
import socket

HOST = '127.0.0.1'
PORT = 8082

# Colocar GPIO no modo de números
GPIO.setmode(GPIO.BOARD)

# Setar os pinos 18 e 22 como saídas e definir o PWM dos servos
GPIO.setup(18,GPIO.OUT)
# Pino 18 para o servo1
servo1 = GPIO.PWM(18,50) 
# Pino 22 para o servo2
GPIO.setup(22,GPIO.OUT)
servo2 = GPIO.PWM(22,50)

# Iniciar PWM  dos servos com o valor 0º (pulse off)
# Os servos são inicializados na posição da seguinte rota: fruto bom e sem mancha
servo1.start(0)
servo2.start(0)

# Iniciar seleção de rotas 

# Comunicação com software através de socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            #Variáveis recebidas pelo software de processamento de imagem
            data = conn.recv(1024)

            if data == 'BOA COM MANCHAS':
                # Colocar servo1 em 0º
                servo1.ChangeDutyCycle(0)
                time.sleep(0.5)
                servo1.ChangeDutyCycle(0)
                # Colocar servo2 em 60º
                servo2.ChangeDutyCycle(5)
                time.sleep(0.5)
                servo2.ChangeDutyCycle(5)
                print("Laranja boa com mancha")

            elif data == 'BOA SEM MANCHAS':
                # Colocar servo1 em 0º
                servo1.ChangeDutyCycle(0)
                time.sleep(0.5)
                servo1.ChangeDutyCycle(0)
                # Colocar servo2 em 0º
                servo2.ChangeDutyCycle(0)
                time.sleep(0.5)
                servo2.ChangeDutyCycle(0)
                print("Laranja boa e sem mancha")

            elif data == 'RUIM':
                # Colocar servo1 em 60º
                servo1.ChangeDutyCycle(5)
                time.sleep(0.5)
                servo1.ChangeDutyCycle(5)
                print("Laranja podre")
                    
                
#Limpar variáveis e finalizar o módulo
servo1.stop()
servo2.stop()
GPIO.cleanup()
