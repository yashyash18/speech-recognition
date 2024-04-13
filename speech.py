import speech_recognition as sr

from gtts import gTTS
import os


def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)

    try:
        # Use Google Web Speech API to convert speech to text
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))

    tts = gTTS(text)
    output_filename = "output.mp3"
    tts.save(output_filename)
    os.system("start " + output_filename)
    print("Text converted to speech and saved as", output_filename)



if __name__ == "__main__":
    speech_to_text()



