// IMPORT LIBRARIES
#include <SoftwareSerial.h>

// PIN CONFIGUATION - SERIAL BUS
#define SerialRX 10            // Serial Receive pin
#define SerialTX 11            // Serial Transmit pin
#define RecieveEnable 4        // RS485 Direction control
#define DataEnable 3           // RS485 Direction control
#define RS485Transmit HIGH
#define RS485Receive LOW
#define Pin13LED 13

// DECLARE OBJECTS
SoftwareSerial RS485Serial(SerialRX, SerialTX); // RX, TX

// DECLARE VARIABLES
int AddressReceived;

// PIN CONFIGURATION - VIBRATION SENSOR
int GroundPin= A0;
int sensePin= A1;

void setup() {
  Serial.begin(9600);
  
  // SERIAL BUS SETUP
  pinMode(RecieveEnable, OUTPUT);
  pinMode(DataEnable, OUTPUT);
  digitalWrite(RecieveEnable, LOW);  // Initialize TX_controller
  digitalWrite(DataEnable, LOW);
  RS485Serial.begin(9600); // Start the software serial port & set the data rate 
  
  // SENSOR SETUP
  pinMode(GroundPin, OUTPUT);
  digitalWrite(GroundPin, LOW);
}

void loop() {
  
  if (RS485Serial.available()) 
  {
    // READ SERIAL BUS
    AddressReceived = RS485Serial.read();
    Serial.println(AddressReceived);
    // If the recieved value and device address dosen't match
    // Then continue the loop 
    if (AddressReceived != 001){
      return;
    }
    
    // If the recieved value and device address matches
    // Then read the sensor value and transmit it
    
    // INDICATE ACTIVITY - LED Blink
    digitalWrite(Pin13LED, HIGH);
    delay(10);              
    digitalWrite(Pin13LED, LOW);  
    
    // READ SENSOR VALUES
    int SemsorReading = analogRead(sensePin);
    Serial.println(SemsorReading);
    
    // TRABSMIT DATA
    digitalWrite(RecieveEnable, HIGH);   // Enable RS485 Transmit  
    digitalWrite(DataEnable, HIGH);  
    RS485Serial.write(SemsorReading);      // Send the byte back
    delay(10);     // Delay
    digitalWrite(RecieveEnable, LOW);
    digitalWrite(DataEnable, LOW);    // Disable RS485 Transmit   
  }
  
  //int reading= analogRead(sensePin);
  //Serial.println(reading);
  //delay(100);
  
}
