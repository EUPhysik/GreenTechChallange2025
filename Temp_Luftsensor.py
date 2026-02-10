import time #zyklische darstellung der Parameter (Pausen zwischen den Messungen) für time.sleep()
import smbus2 #wird benötigt um mit dem Sensor über I2C zu sprechen.
import bme280 #enthält die informationen des Sensors (interpretation,Kalibrierung etc.)
from datetime import datetime #Datum und Uhrzeit zu den Messungen hinzufügen

###
#ist die Addresse des Sensors, ohne Adresse kan Raspberry Pi keine Anfrage erhalten oder senden.
adresse = 0x76

#der I2C bus wird aktiviert, um mit dem Sensor sprechen zu können.
bus = smbus2.SMBus(1)

#lädt interne daten des Sensors bzw. Werksdaten des Sensors.
#darin sind Berechnungen enthalten auf die zugegriffen wird.
#bme280 ist die Bibliothek des Sensors
#load_calibration_params lädt interne Kalibrierungen und Funktionen
#bus und addresss sind wichtig für load_calibration_params, damit die richtige Zuweisung stattfindet.
Sensor280 = bme280.load_calibration_params(bus, adresse)
###
# Intervallabfrage
zyklus = 1

#Grenzen für Messungen
temp_min = 10
temp_max = 35
hum_min = 40
hum_max = 60

while True:
    try:
#Zeitstempel
        now = datetime.now()
        Datum = now.strftime("%d-%m-%Y")
        Uhrzeit = now.strftime("%H:%M:%S")
        print("Datum:", Datum,"|", "Uhrzeit", Uhrzeit)
       
        
#Sensor Daten
        #Liest Sensor daten
        data = bme280.sample(bus, adresse, Sensor280)

        # definieren folgende Parameter zum auslesen
        temperatur_celsius = data.temperature
        druck = data.pressure
        Luftfeuchtigkeit = data.humidity

        # Gibt die Messungen aus 
        print("Temperatur: {:.2f} °C".format(temperatur_celsius))
        
        #Meldung bei Grenzwertüberschreitung (Temperatur)
        if temperatur_celsius < temp_min:
            print("Die Temperatur ist zu niedrig")
        elif temperatur_celsius > temp_max:
            print("Temperatur ist zu hoch")
        
        print("Druck: {:.2f} hPa".format(druck))
        
        print("Luftfeuchtigkeit: {:.2f} %".format(Luftfeuchtigkeit))
        
        #Meldung bei Grenzwertüberschreitung (Luftfeuchtigkeit)
        if Luftfeuchtigkeit < hum_min:
            print("Die Luftfeuchtigkeit ist zu niedrig")
        elif Luftfeuchtigkeit > hum_max:
            print("Luftfeuchtigkeit ist zu hoch")
        
    
        # Leitet einen Zyklische abfrage ein bzw. gibt vor, in welchen Takt sich die schleife wiederholt.
        time.sleep(zyklus)

    except KeyboardInterrupt:
        print('Programm stoppt')
        break
    except Exception as e:
        print('Fehler ist aufgetaucht:', str(e))
        break
