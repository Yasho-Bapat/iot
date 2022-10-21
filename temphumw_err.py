import adafruit_dht as dht
import board
import time

sensor = dht.DHT22(board.D4)

for i in range (5):
  try:
    temp = sensor.temperature
    hum = sensor.humidity
    print("humidity: " + str(hum) + "; temperature: " + str(temp))
  except RuntimeError as error:
    print(error.args[0])
    time.sleep(2)
    continue
