# development from Wokwi.com to implement the SIMPLEST iteration of a temperature humidity sensor
# 11.09.2023  REV0


from machine import Pin
from time import sleep
import dht


sensor = dht.DHT22(Pin(15))

while True: 
  try:
    sensor.measure()
    temp_dht = sensor.temperature()
    humid_dht = sensor.humidity()
    print(f'Temperature is {temp_dht:.1f} and Humidity is {humid_dht:.1f}.')
    sleep(3)

  except OSError as err:
    print("Error in measurement")
