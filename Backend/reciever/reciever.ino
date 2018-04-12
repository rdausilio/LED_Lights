//goddard-bot/goddard-base - recievers
#include <Adafruit_NeoPixel.h>

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 10);
const uint64_t pipe = 0xE6E6E6E6E6E6; //needs to be the same

#define PIN 6
#define NUM_LEDS 30
#define BRIGHTNESS 40
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRBW + NEO_KHZ800);
int recievedMessage[4] = {0, 0, 0, 0};

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(1, pipe);
  radio.startListening();

  strip.setBrightness(BRIGHTNESS);
  strip.begin();
  strip.show();
}
void loop() {
  while (radio.available()) {
    radio.read(recievedMessage, sizeof(int) * 4);
    for (int j = 0; j < NUM_LEDS; j++)
      strip.setPixelColor(j, strip.Color(recievedMessage[0], recievedMessage[1], recievedMessage[2], recievedMessage[3]));
    strip.show();
    delay(100);
  }
}
