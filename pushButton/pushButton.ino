const int buttonPin = 2;
const int ledPin = 13;

int buttonState = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(buttonPin, INPUT);
  Serial.begin(9600); 
    buttonState = digitalRead(buttonPin);


  if (buttonState == HIGH) {
    Serial.print("Pressed");
  } else {
    Serial.print("Off");
  }
  delay(20);
}

void loop() {
  // put your main code here, to run repeatedly:
}
