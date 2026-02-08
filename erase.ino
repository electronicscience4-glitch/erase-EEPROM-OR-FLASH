#include <EEPROM.h>
void setup() {
   EEPROM.begin(512);
for (int i = 0; i < 512; i++) {
  EEPROM.write(i, 0);
}
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
  EEPROM.commit();
  EEPROM.end();
}
void loop() {
}
