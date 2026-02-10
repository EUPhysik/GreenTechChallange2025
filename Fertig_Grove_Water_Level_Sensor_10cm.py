import time
import smbus2
from collections import Counter
#Adresse des Sensors für I2C
adresse1 = 0x77
adresse2 = 0x78

bus = smbus2.SMBus(1)

#liest die Daten aus, die der Sensor ausgibt

#für die unteteren 8 Pads

while True:
    
    SDA1_roh = [1 if bus.read_byte_data(adresse1, i) > 230 else 0 for i in range(8)] # Range funktion, damit die Pads gleichzeitig ausgelesen werden
    SDA2_roh = [1 if bus.read_byte_data(adresse2, j) > 230 else 0 for j in range(12)]
    ###print(SDA1_roh)
    ###print(SDA2_roh)
    #zählt die nullen und die einsen mit der Counter Funktion
    SDA1 = Counter(SDA1_roh)
    SDA2 = Counter(SDA2_roh)
    #gibt die Anzahl an einsen aus
    ###print(SDA1[1])
    ###print(SDA2[1])
    #Pegelstand für die ersten 8 Pads
    #Anzahl an einsen bestimmt den Pegelstand
    Pegelstand = (SDA1[1] +SDA2[1])*5
    print("Pegelstand bei:",Pegelstand,"%")

    time.sleep(1)
