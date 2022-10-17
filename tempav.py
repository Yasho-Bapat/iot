import Adafruit_DHT as dht
import time
sensor = dht.DHT22
pin = 4

temp_list = list()
for i in range(25):
    hum, temp = dht.read_retry(sensor, pin)
    temp_list.append(temp)

print("average temperature over 25 readings = " + str(sum(temp_list)/len(temp_list)))
