#include "Adafruit_FONA.h"
#include <SoftwareSerial.h>

#define FONA_TX 2
#define FONA_RX 3
#define FONA_RST 9

SoftwareSerial fonaSS = SoftwareSerial(FONA_TX, FONA_RX);
SoftwareSerial *fonaSerial = &fonaSS;

char replybuffer[255];
char tcpbuffer[255];
String address;
String tcp_connection;
bool active;
FONAFlashStringPtr response;

Adafruit_FONA_3G fona = Adafruit_FONA_3G(FONA_RST);

void setup() {
  while (!Serial);

  Serial.begin(115200);
  Serial.println(F("Device Manager engage."));

  fonaSerial->begin(4800);
  fona.begin(*fonaSerial);

  //  fona.setGPRSNetworkSettings(F("TM"));
  //  fona.getNetworkStatus();
  //
  //  while (!fona.enableGPRS(true));
  
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

  while (!(fona.sendCheckReply(F("AT+CGSOCKCONT=1, \"IP\", \"JTFIXEDPUBLIC\""), F("OK")))) {
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
//
//  DEBUG_PRINT(F("\t---> ")); DEBUG_PRINTLN("AT+IPADDR");
//  fona.println("AT+IPADDR");
//  uint8_t l = readline(5000, 1, replybuffer);
//
//  for (int i = 0; i < strlen(replybuffer); i++) {
//    if (i > 8 && replybuffer[i] != '\n' && replybuffer[i] != 'O' && replybuffer[i] != 'K') {
//      address = address + replybuffer[i];
//    }
//  }
//  replybuffer[0] = '\0';
//
//  flushInput();
  //  tcp_connection = "AT+CIPOPEN=0, \"TCP\", \"" + address + "\", 8080";
//  tcp_connection = "AT+CIPOPEN=0, \"TCP\", \"91.229.188.21\", 8080";
  //  Serial.println(tcp_connection);
//  flushInput();

  fona.sendCheckReply(F("AT+CREG?"), F("AT"));
  fona.sendCheckReply(F("AT+CGSOCKCONT=?"), F("AT"));
  fona.sendCheckReply(F("AT+NETOPEN?"), F("AT"));
  //  fona.sendCheckReply(F("AT+CIPOPEN=0, \"TCP\", \"192.168.1.71\", 5000"), F("OK"));
  //  fonaSerial->read();
  fona.sendCheckReply(F("AT+SERVERSTART?"), F("AT"));
  fona.sendCheckReply(F("AT+SERVERSTART=8080,0"), F("AT"));
  
  fona.sendCheckReply(F("AT+SERVERSTART?"), F("AT"));

//  DEBUG_PRINT(F("\t---> ")); DEBUG_PRINTLN(tcp_connection);
//  fona.println(tcp_connection);
//  uint8_t k = readline(5000, 1, tcpbuffer);
//  DEBUG_PRINT (F("\t<--- ")); DEBUG_PRINTLN(tcpbuffer);
//  fona.sendCheckReply(F("AT+CIPOPEN?"), F("AT"));

}

void loop() {
//    flushInput();
//    fona.println("AT+CIPRXGET=2,1,1024");
    fona.sendCheckReply(F("AT+CIPRXGET=2,1,1024"), F("AT"));
    delay(1000);
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
