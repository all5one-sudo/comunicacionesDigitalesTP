#include <SoftwareSerial.h>

SoftwareSerial GPS(10, 11); // RX, TX

void setup() {
  Serial.begin(9600);    // Inicializa el puerto serie
  GPS.begin(9600);       // Inicializa el puerto serie para el GPS
  GPS.println("$PMTK220,1000*1F"); // Configura el GPS para enviar datos NMEA cada segundo
}

void loop() {
  if (GPS.available()) {
    String NMEA = GPS.readStringUntil('\n'); // Lee la sentencia NMEA del GPS
    if (NMEA.startsWith("$GPGGA")) {  // Analiza la sentencia NMEA para obtener información de ubicación
      Serial.println(NMEA);  // Imprime la sentencia NMEA para depuración
    }
  }
}
