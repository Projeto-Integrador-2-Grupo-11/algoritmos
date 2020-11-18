# Código para contagem das laranjas boas sem manchas classificadas por diâmetro (pequena, média e grande)

#Importando as bibliotecas necessárias
import RPi.GPIO as GPIO #Biblioteca que possibilita controlar e interagir com os pinos do GPIO (Entradas e saídas)
import time #Biblioteca que permite controlar funções que utilizam o tempo

#Variáveis para armazenar o valor da contagem
laranja_pequena  = 0
laranja_media = 0
laranja_grande = 0

#Variáveis para armazenar o valor da distância
distancia_pequena = 0
distancia_media = 0
distancia_grande = 0

#GPIO.BOARD configura os pinos na forma de contagem física.
GPIO.setmode(GPIO.BOARD) 

#Conexão física dos pinos
PIN_TRIGGER1 = 29 #Sensor laranja_pequena
PIN_ECHO1 = 11 #Sensor laranja_pequena
PIN_TRIGGER2 = 31 #Sensor laranja_média
PIN_ECHO2 = 13 #Sensor laranja_média
PIN_TRIGGER3 = 37 #Sensor laranja_grande
PIN_ECHO3 = 15 #Sensor laranja_grande
  
#Configurando os pinos como saída e entrada
GPIO.setup(PIN_TRIGGER1, GPIO.OUT) #Sensor laranja_pequena
GPIO.setup(PIN_ECHO1, GPIO.IN) #Sensor laranja_pequena
GPIO.setup(PIN_TRIGGER2, GPIO.OUT) #Sensor laranja_média
GPIO.setup(PIN_ECHO2, GPIO.IN) #Sensor laranja_média
GPIO.setup(PIN_TRIGGER3, GPIO.OUT) #Sensor laranja_grande
GPIO.setup(PIN_ECHO3, GPIO.IN) #Sensor laranja_grande

while True:

    #Gerando um pulso de 1ns no Trigger para acionamento do sensor ultrassônico
    GPIO.output(PIN_TRIGGER1, GPIO.HIGH)
    GPIO.output(PIN_TRIGGER2, GPIO.HIGH)
    GPIO.output(PIN_TRIGGER3, GPIO.HIGH)

    time.sleep(0.00001) #espera 
      
    #Voltando para o nível lóggico baixo
    GPIO.output(PIN_TRIGGER1, GPIO.LOW)
    GPIO.output(PIN_TRIGGER2, GPIO.LOW)
    GPIO.output(PIN_TRIGGER3, GPIO.LOW)
    
    #Variáveis para guardar o tempo de início do pulso e fim do pulso
    tempo_inicio_pulso1 = time.time()
    tempo_inicio_pulso2 = time.time()
    tempo_inicio_pulso3 = time.time()
    
    tempo_fim_pulso1 = time.time()
    tempo_fim_pulso2 = time.time()
    tempo_fim_pulso3 = time.time()

    #Tempo para o sensor estabilizar
    time.sleep(0.2)
      
    #Verifica se o PIN_ECHO está em nível lógico alto ou baixo e seta o tempo de início do pulso e fim do pulso com o tempo atual.
    while (GPIO.input(PIN_ECHO1)==0 and GPIO.input(PIN_ECHO2)==0 and GPIO.input(PIN_ECHO3)==0):
        tempo_inicio_pulso1 = time.time()
        tempo_inicio_pulso2 = time.time()
        tempo_inicio_pulso3 = time.time()
    while (GPIO.input(PIN_ECHO1)==1 or GPIO.input(PIN_ECHO2)==1 or GPIO.input(PIN_ECHO3)==1):
        if(GPIO.input(PIN_ECHO1)==1):
            tempo_fim_pulso1 = time.time()
        elif GPIO.input(PIN_ECHO2)==1:
            tempo_fim_pulso2 = time.time()
        elif GPIO.input(PIN_ECHO3)==1:
            tempo_fim_pulso3 = time.time()     
        
    #Calculando as distâncias
    # A duração do pulso é a diferença entre o fim do pulso e início do pulso
    # Distância = (duração do pulso * velocidade do som) / 2
    # Convertendo de metros para centímetros
    
    #Distância para laranjas pequenas
    duracao_pulso1 = tempo_fim_pulso1 - tempo_inicio_pulso1 
    distancia_pequena = round((duracao_pulso1 * 34300)/2, 2) 
    distancia_pequena = distancia_pequena/100 
    
    #Distância para laranjas médias  
    duracao_pulso2 = tempo_fim_pulso2 - tempo_inicio_pulso2
    distancia_media = round((duracao_pulso2 * 34300)/2, 2)
    distancia_media = distancia_media/100
     
    #Distância para laranjas grandes 
    duracao_pulso3 = tempo_fim_pulso3 - tempo_inicio_pulso3
    distancia_grande = round((duracao_pulso3 * 34300)/2, 2)
    distancia_grande = distancia_grande/100
    
    #Atualizando a contagem e  armazenando os valores nas variáveis de contagem
    if distancia_pequena <= 50 and distancia_pequena > 0:
        laranja_pequena = laranja_pequena + 1
    if distancia_media <= 50 and distancia_media > 0:
        laranja_media = laranja_media + 1
    if distancia_grande <= 50 and distancia_grande >0:
        laranja_grande = laranja_grande + 1
    else:
        laranja_pequena = laranja_pequena
        laranja_media = laranja_media
        laranja_grande = laranja_grande

    #Apresentando os resultados da contagem
    print('Laranja Pequena:',laranja_pequena)
    print('Laranja Média:',laranja_media)
    print('Laranja Grande:',laranja_grande)