import Adafruit_DHT as dht 
import time

sensor = dht.DHT22
pin = 4

for i in range 5:
  hum, temp = dht.read_retry(sensor, pin)
  print("Humidity: " + str(hum) + "; Temeperature: " + str(temp))
  time.sleep(2)
