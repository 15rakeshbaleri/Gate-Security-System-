import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Initialize speech engine
try:
    engine = pyttsx3.init()
except Exception as e:
    print(f"Error initializing pyttsx3: {e}")
    exit(1)


def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()


def recognize_speech(prompt, timeout=5):
    """Recognize speech from microphone and return text"""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak(prompt)
        print(prompt + " (Speak now...)")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=timeout)
        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.")
            return recognize_speech(prompt, timeout)  # Retry if no speech is detected

        try:
            text = recognizer.recognize_google(audio).lower().strip()  # Convert to lowercase and strip spaces
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio. Please try again.")
            return recognize_speech(prompt, timeout)  # Retry if speech is not clear
        except sr.RequestError:
            print("Speech Recognition service unavailable.")
            return "error"


def validate_phone_number(phone_number):
    """Validate if the phone number is numeric and has 10 digits"""
    return phone_number.isdigit() and len(phone_number) == 10


# Asking for inputs
name = recognize_speech("Please say your name")
purpose = recognize_speech("Please say your purpose")

while True:
    phone_number = recognize_speech("Please say your phone number")
    if validate_phone_number(phone_number):
        break
    else:
        speak("Invalid phone number. Please say a 10-digit number.")

# Get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Confirmation Loop (Wait until user gives a valid response)
while True:
    confirmation = recognize_speech("Would you like to confirm? Say yes or no").lower()

    if confirmation in ["yes", "yeah", "confirm", "okay", "s"]:
        speak("Thank you. Your form has been recorded on " + current_datetime)
        print("\n✅ Form successfully submitted!")
        break  # Exit loop on confirmation
    elif confirmation in ["no", "cancel", "not now", "exit", "quit"]:
        speak("Form submission canceled. Restart if you want to try again.")
        print("\n❌ Form not submitted.")
        break  # Exit loop if the user cancels
    else:
        speak("I didn't understand. Please say yes or no.")  # Repeat prompt if unclear