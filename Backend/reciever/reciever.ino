//goddard-bot/goddard-base - recievers
#include <Adafruit_NeoPixel.h>

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define PIN 6

#define NUM_LEDS 30

#define BRIGHTNESS 40

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRBW + NEO_KHZ800);
int i;

RF24 radio(9, 10); // CE, CSN
const byte address[6] = "00001";
void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();

  strip.setBrightness(BRIGHTNESS);
  strip.begin();
  strip.show();
  i = 0;
}
void loop() {
  if (radio.available()) {
    char text[32] = "";
    radio.read(&text, sizeof(text));
    Serial.println(text);
  }

  for (int j = 0; j < NUM_LEDS; j++)
    strip.setPixelColor(j, strip.Color(0, 0, 0, 15));
  strip.setPixelColor(i, strip.Color(66, 164, 244, 0));
  strip.setPixelColor(i + 1, strip.Color(188, 33, 160, 0));
  strip.setPixelColor(i + 2, strip.Color(66, 164, 244, 0));

  strip.show();
  delay(100);
  if (++i >= NUM_LEDS)
    i = 0;

}
