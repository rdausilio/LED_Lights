//goddard-bot/goddard-bot - transmitter

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

int val;

RF24 radio(9, 10); // CE, CSN

const uint64_t pipe = 0xE6E6E6E6E6E6; //needs to be the same

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(pipe);
}

void loop() {
  int text[4] = {130, 179, 155, 0};
  radio.write(&text, sizeof(text));
  delay(100);

}
