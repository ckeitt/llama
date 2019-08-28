#include "Adafruit_FONA.h"
#include <SoftwareSerial.h>

#define FONA_TX 2
#define FONA_RX 3
#define FONA_RST 9

SoftwareSerial fonaSS = SoftwareSerial(FONA_TX, FONA_RX);
SoftwareSerial *fonaSerial = &fonaSS;

char replybuffer[255];
bool active;

Adafruit_FONA_3G fona = Adafruit_FONA_3G(FONA_RST);

void setup() {
  while (!Serial);

  Serial.begin(115200);
  Serial.println(F("Device Manager engage."));

  fonaSerial->begin(4800);
  fona.begin(*fonaSerial);

  active = false;
  pinMode(A0, OUTPUT);
  digitalWrite(A0, LOW);
  
  (fona.sendCheckReply(F("AT+CPSI?"), F("OK")));
  
  while (!(fona.sendCheckReply(F("AT+CREG=2"), F("OK")))) {
    delay(1000);
    flushInput();
  }

  while (!(fona.sendCheckReply(F("ATS0=3"), F("OK")))) {
    delay(1000);
    flushInput();
  }
  while (!(fona.sendCheckReply(F("AT+CGATT=1"), F("OK")))) {
    delay(1000);
    flushInput();
  }

  while (!(fona.sendCheckReply(F("AT+CGSOCKCONT=1, \"IP\", \"APN\""), F("OK")))) {
    delay (1000);
    flushInput();
  }

  while (!(fona.sendCheckReply(F("AT+CSOCKSETPN=1"), F("OK")))) {
    delay (1000);
    flushInput();
  }
  
  while (!(fona.sendCheckReply(F("AT+CIPMODE=1"), F("OK")))) {
    delay (1000);
    flushInput();
  }

  while (!(fona.sendCheckReply(F("AT+CIPRXGET=1"), F("OK")))) {
    delay (1000);
    flushInput();
  }

  while (!(fona.sendCheckReply(F("AT+CIPHEAD=1"), F("OK")))) {
    delay (1000);
    flushInput();
  }

  while (!(fona.sendCheckReply(F("AT+CIPSRIP=1"), F("OK")))) {
    delay (1000);
    flushInput();
  }

  while (!(fona.sendCheckReply(F("AT+CIPCCFG=10,0,0,1,1,0,500"), F("OK")))) {
    delay (1000);
    flushInput();
  }

  (fona.sendCheckReply(F("AT+NETOPEN"), F("OK")));
  delay (5000);
  flushInput();

  while (!(fona.sendCheckReply(F("AT&E0"), F("OK")))) {
    delay (1000);
    flushInput();
  }

  fona.sendCheckReply(F("AT+SERVERSTART=8080,0"), F("AT"));
}

void loop() {
    if (fona.sendCheckReply(F("AT+CIPRXGET=2,1,1500"), F("0"))) {
      if (active == false) {
        digitalWrite(A0, HIGH);
        active = true;  
      } else {
        digitalWrite(A0, LOW);
        active = false;
      }
    }
    
    delay(10);
}

uint8_t readline(uint16_t timeout, boolean multiline, char * rbuffer) {
  uint16_t replyidx = 0;

  while (timeout--) {
    if (replyidx >= 254) {
      //DEBUG_PRINTLN(F("SPACE"));
      break;
    }

    while (fonaSerial->available()) {
      char c =  fonaSerial->read();
      if (c == '\r') continue;
      if (c == 0xA) {
        if (replyidx == 0)   // the first 0x0A is ignored
          continue;

        if (!multiline) {
          timeout = 0;         // the second 0x0A is the end of the line
          break;
        }
      }
      rbuffer[replyidx] = c;
      replyidx++;
    }

    if (timeout == 0) {
      //DEBUG_PRINTLN(F("TIMEOUT"));
      break;
    }
    delay(1);
  }
  rbuffer[replyidx] = 0;  // null term
  return replyidx;
}

void flushInput() {
  // Read all available serial input to flush pending data.
  uint16_t timeoutloop = 0;
  while (timeoutloop++ < 40) {
    while (fonaSerial->available()) {
      fonaSerial->read();
      timeoutloop = 0;  // If char was received reset the timer
    }
    delay(1);
  }
}
