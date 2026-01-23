#include <Adafruit_NeoPixel.h>

#define LED_PIN    48   // Data pin for built-in RGB
#define NUM_LEDS    1   // Only 1 built-in RGB LED

Adafruit_NeoPixel strip(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

String cmd = "";

void setup() {
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'

  Serial.begin(115200);
  while (!Serial) { delay(10); }

  Serial.println("ESP32-S3 Built-in RGB Ready");
}

// Map finger counts to colors
void setColor(String colorCmd) {
  uint32_t color = strip.Color(0,0,0); // default OFF

  if (colorCmd == "RED") {
    color = strip.Color(255,0,0);
  }
  else if (colorCmd == "GREEN") {
    color = strip.Color(0,255,0);
  }
  else if (colorCmd == "BLUE") {
    color = strip.Color(0,0,255);
  }
  else if (colorCmd == "VIOLET") {
    color = strip.Color(128,0,255);
  }
  else if (colorCmd == "WHITE") {
    color = strip.Color(255,255,255);
  }
  else if (colorCmd == "OFF") {
    color = strip.Color(0,0,0);
  }

  strip.setPixelColor(0, color);
  strip.show();
  Serial.println("LED set to: " + colorCmd);
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();

    if (c == '\n') {
      cmd.trim();
      setColor(cmd);
      cmd = "";
    } else {
      cmd += c;
    }
  }
}
