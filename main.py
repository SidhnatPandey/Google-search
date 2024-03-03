import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize Text to Speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Take voice input
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Convert voice to text
        query = recognizer.recognize_google(audio)
        print("You said:", query)

        # Perform Google search
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open_new(search_url)
        speak("Opening Google search results for " + query)

    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        speak("Sorry, could not understand audio.")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        speak("Could not request results from Google Speech Recognition service.")

if __name__ == "__main__":
    main()
