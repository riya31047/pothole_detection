int IRvalue;  //Initialize InfraRed proximity sensor

int flexValue; //Initialize Flex sensor

void setup(){ 
   Serial.begin(9600) 
}   //Begin serial communication between computer and Arduino microcontroller keeping a Baud rate of 9600

void loop(){ 
//Start a loop
)
    IRvalue=analogRead(A0);
    //Take input from port A0 of Arduino, through which IR sensor is connected
    Serial.println(IRvalue);
    //Print the sensor values obtained from IR senskr
    flexValue=analogRead(A1); 
    //Take input from port A1 of Arduino, through which flex sensor is connected
     Serial.println(flexValue); 
     //Print the senaor values obtained from flex sensor
     
} 

int IRValues;
int flexValue;
void setup(){
  Serial.begin(9600);
  
}
void loop(){
  IRValue=analogRead(A0);
if(IRValue<600)
  Serial.println(IRValue);
  flexValue=analogRead(A1);
if(flexValue<40)
  Serial.println(flexValue);
 
}//Terminate the code
