#define slaveAddress 9

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);//Led Connected
  pinMode(3, OUTPUT);//DE/RE Controling pin of RS-485
}

void loop() {
  // put your main code here, to run repeatedly:
  char getdata='c';

  digitalWrite(13,LOW);//Led OFF
  digitalWrite(3,LOW);//DE/RE=LOW Receive Enabled

   if(Serial.available()){
    getdata=Serial.read();
    //Serial.print(getdata);
    //delay(100);
    }
    
   if(getdata='9'){
      digitalWrite(3,HIGH);//DE/RE=HIGH Transmit Enabled 
      Serial.print(5);
      //digitalWrite(3,LOW);//DE/RE=LOW Receive Enabled
    }
    
  delay(20);
  digitalWrite(13,HIGH);//Led ON
  delay(20);
}
