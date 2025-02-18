from smbus2 import SMBus

# https://www.silabs.com/documents/public/data-sheets/Si7021-A20.pdf

BUS = 1
I2C_ADDRESS = 0x40

TEMP_FROM_PREV_HUMIDITY_MEASUREMENT = 0xE0
TEMPERATURE = 0xE3
HUMIDITY = 0xE5

def swapWordBytes(word):
  return ((word>>8)&0xff) + ((word&0xff)<<8)

def calculateTemperature(temperature):
  return ((175.72 * temperature) / 65536) - 46.85

def getTemperature(bus):
  temperature = bus.read_word_data(I2C_ADDRESS, TEMPERATURE)
  temperature = swapWordBytes(temperature)
  return calculateTemperature(temperature)

def calculateHumidity(humidity):
  return ((125 * humidity) / 65536) - 6

def getHumidity(bus):
  humidity = bus.read_word_data(I2C_ADDRESS, HUMIDITY)
  humidity = swapWordBytes(humidity)
  return calculateHumidity(humidity)

try:
  bus = SMBus(BUS)
  temperature = getTemperature(bus)
  humidity = getHumidity(bus)
except:
  bus = None
  temperature = -100
  humidity = -100

if bus is not None:
  bus.close()


if __name__ == '__main__':
  import json, sys, time

  data = {
    "host": "Raspberri Pi2",
    "sourcetype": "pmsd001",
    "time": time.time(),
    "event": {
      "temperature": format(temperature, '.2f'),
      "humidity": format(humidity, '.2f')
    }
  }

  print(json.dumps(data))
