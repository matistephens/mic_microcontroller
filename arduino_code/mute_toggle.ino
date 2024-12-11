const int buttonPin = 2; // Pin connected to the button
int lastButtonState = HIGH; // Last known state of the button
bool buttonWasPressed = false; // Tracks if the button was pressed and released

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
  Serial.println("System Initialized");
}

void loop() {
  int currentButtonState = digitalRead(buttonPin); // Read the button state

  // Detect when the button is pressed
  if (currentButtonState == LOW && lastButtonState == HIGH) {
    buttonWasPressed = true;
    Serial.println("Button Pressed");
  }

  // Detect when the button is released
  if (currentButtonState == HIGH && lastButtonState == LOW && buttonWasPressed) {
    Serial.println("Button Released");
    Serial.println("TOGGLE_MUTE");
    buttonWasPressed = false; // Reset for the next cycle
  }

  // Update the last button state
  lastButtonState = currentButtonState;
}