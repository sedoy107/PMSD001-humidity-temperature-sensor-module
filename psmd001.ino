#include <Wire.h>

// https://www.silabs.com/documents/public/data-sheets/Si7021-A20.pdf
#define I2C_ADDRESS 0x40
#define TEMP_REG 0xE3
#define HUMIDITY_REG 0xE5

void setup() {
  Wire.begin();
  Serial.begin(112500);
}

int get_data(int addr, int reg) {
  Wire.beginTransmission(addr);
  Wire.write(reg);
  Wire.endTransmission();

  Wire.requestFrom(addr, 2);
  while(!Wire.available());
  return (((int(Wire.read()) & 0xff) << 8) | (int(Wire.read()) & 0xff));
}

double get_temperature() {
  return ((175.72 * get_data(I2C_ADDRESS, TEMP_REG)) / 65536) - 46.85;
}

double get_humidity() {
  return ((125.0 * get_data(I2C_ADDRESS, HUMIDITY_REG)) / 65536) - 6;
}

void loop() {
  Serial.print("Temperature: "); Serial.println(get_temperature());
  Serial.print("Humidity: "); Serial.println(get_humidity());
  delay(2000);
}
