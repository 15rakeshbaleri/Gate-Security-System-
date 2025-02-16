import speech_recognition as sr
import pyttsx3
import csv
from datetime import datetime
import os

# Initialize Text-to-Speech Engine
try:
    engine = pyttsx3.init()
except Exception as e:
    print(f"Error initializing pyttsx3: {e}")
    engine = None  # Allow script to continue even if TTS fails


def speak(text):
    """Convert text to speech"""
    if engine:
        engine.say(text)
        engine.runAndWait()
    else:
        print(f"SPEAK: {text}")  # Fallback if TTS is unavailable


def recognize_speech(prompt, timeout=5, retries=3):
    """Recognize speech from the microphone and return cleaned text"""
    recognizer = sr.Recognizer()

    for attempt in range(retries):
        with sr.Microphone() as source:
            speak(prompt)
            print(prompt + " (Speak now...)")
            recognizer.adjust_for_ambient_noise(source)

            try:
                audio = recognizer.listen(source, timeout=timeout)
                text = recognizer.recognize_google(audio).strip()
                print(f"Recognized: {text}")
                return text
            except sr.WaitTimeoutError:
                print("No speech detected. Please try again.")
            except sr.UnknownValueError:
                print("Could not understand the audio. Please try again.")
            except sr.RequestError:
                print("Speech Recognition service unavailable.")
                return "error"

    speak("Too many failed attempts. Moving to the next step.")
    return "error"


# Collecting user details
name = recognize_speech("Please say your name")
purpose = recognize_speech("Please say your purpose")
phone_number = recognize_speech("Please say your phone number")  # No validation

# Get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Confirmation via Console Input
while True:
    speak("Type yes to confirm and no to reject.")
    confirmation = input("Would you like to confirm? Type 'yes' to confirm or 'no' to cancel: ").strip().lower()

    if confirmation in {"yes", "y"}:
        speak(f"Thank you. Your form has been recorded on {current_datetime}")
        print("\n✅ Form successfully submitted!")

        # Display recorded details
        print("\n📋 **Submitted Details:**")
        print(f"📝 Name      : {name}")
        print(f"🎯 Purpose   : {purpose}")
        print(f"📞 Phone No  : {phone_number}")
        print(f"📅 Timestamp : {current_datetime}\n")

        # Save data to CSV
        csv_file = "visitor_data.csv"
        file_exists = os.path.isfile(csv_file)

        with open(csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Name", "Purpose", "Phone Number", "Timestamp"])
            writer.writerow([name, purpose, phone_number, current_datetime])

        print("✅ Data successfully saved to CSV.")
        break

    elif confirmation in {"no", "n"}:
        speak("Form submission canceled. Restart if you want to try again.")
        print("\n❌ Form not submitted.")
        break

    else:
        print("Invalid input. Please type 'yes' or 'no'.")
