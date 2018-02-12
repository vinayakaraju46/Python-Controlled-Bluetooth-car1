//My bluetooth controlled car. 
//declare global variables
char state ;
const int motorP1 = 5;
const int motorP2 = 6;
const int motorQ1 = 9;
const int motorQ2 = 10;
void setup() {
  // put your setup code here, to run once:
// declare all the motors as output
pinMode(motorP1 , OUTPUT);
pinMode(motorP2 , OUTPUT);
pinMode(motorQ1 , OUTPUT);
pinMode(motorQ2 , OUTPUT);
Serial.begin(9600);   //begin streaming serial data from the bluetooth module
}

void loop() {
  // put your main code here, to run repeatedly:
// if receiving data from bluetooth module, assign a variable to the streaming data
if(Serial.available() > 0) {
  state = Serial.read();
}

//IF STATE IS "F" , MOVE FORWARD
if (state == '1'){
  digitalWrite(motorP1, HIGH);
  digitalWrite(motorP2, LOW);
  digitalWrite(motorQ1 , HIGH);
  digitalWrite(motorQ2 , LOW);
}
//IF STATE IS "S", STOP
if (state == '9') {
  digitalWrite(motorP1 , LOW);
  digitalWrite(motorP2 , LOW);
  digitalWrite(motorQ1 , LOW);
  digitalWrite(motorQ2 , LOW);
}
//IF STATE IS "B", moves BACKWARDS
if (state == '0'){
  digitalWrite(motorP1 , LOW);
  digitalWrite(motorP2 , HIGH);
  digitalWrite(motorQ1 , LOW);
  digitalWrite(motorQ2 , HIGH);
}
//IF STATE IS "R", takes HARD RIGHT
if (state == '4'){
  digitalWrite(motorP1 , HIGH);
  digitalWrite(motorP2 , LOW);
  digitalWrite(motorQ1 , LOW);
  digitalWrite(motorQ2 , HIGH);
}
//IF STATE IS "L" , takes HARD LEFT
if (state == '5'){
  digitalWrite(motorP1 , LOW);
  digitalWrite(motorP2 , HIGH);
  digitalWrite(motorQ1 , HIGH);
  digitalWrite(motorQ2 , LOW);
}
//IF STATE IS "G" , takes FORWARD LEFT
if (state == '3'){
  digitalWrite(motorP1, LOW);
  digitalWrite(motorP2, LOW);
  digitalWrite(motorQ1, HIGH);
  digitalWrite(motorQ2, LOW);
}
//IF STATE IS "I" , takes FORWARD RIGHT
if (state == '2'){
  digitalWrite(motorP1, HIGH);
  digitalWrite(motorP2, LOW);
  digitalWrite(motorQ1, LOW);
  digitalWrite(motorQ2, LOW);
}
//IF STATE IS "J" , takes BACKWARD LEFT
if (state == '7'){
  digitalWrite(motorP1, LOW);
  digitalWrite(motorP2, LOW);
  digitalWrite(motorQ1, LOW);
  digitalWrite(motorQ2, HIGH);
}
//IF STATE IS "H", takes BACKWARD RIGHT
if (state == '6'){
  digitalWrite(motorP1, LOW);
  digitalWrite(motorP2, HIGH);
  digitalWrite(motorQ1, LOW);
  digitalWrite(motorQ2, LOW);
}
}
//written by Rahul MK
