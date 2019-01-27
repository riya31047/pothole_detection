#include <SoftwareSerial.h>
SoftwareSerial ESPserial(2, 3); // RX | TX

void setup() 
{
  Serial.begin(9600);
  ESPserial.begin(115200);
  ESPserial.println("AT+IPR=9600");
  delay(1000);
  ESPserial.end();
  // Start the software serial for communication with the ESP8266
  ESPserial.begin(9600);

  Serial.println("Ready");
  ESPserial.println("AT+GMR");
}

void loop() 
{
    // listen for communication from the ESP8266 and then write it to the serial monitor
    if ( ESPserial.available() )   {  Serial.write( ESPserial.read() );  }

    // listen for user input and send it to the ESP8266
    if ( Serial.available() )       {  ESPserial.write( Serial.read() );  }
}
