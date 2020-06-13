# How does Speech recognition work?
# Speech (audio file or through microphone) => Converting Physical sound into electrical signal
# Convert the signal into digital data with analog-to-digital converter => Once digitized, model can be used
# to transcribed the audio into text

# Hidden Markov Model (HMM), deep neural network models are used to convert the audio into text. To convert speech to
# text using Python it can be done with the help of the “Speech Recognition” API and “PyAudio” library.

# Import Speech recognition library
import speech_recognition as sr
from gtts import gTTS
import os


class SpeechRecognition:
    def __init__(self):
        # Initialize recognizer class (for recognizing the speech)
        self.recognizer = sr.Recognizer()

    def play_audio(self):
        text = "Good Morning I am speaking now, please listen."
        language = "en"
        speech = gTTS(text=text, lang=language, slow=False)
        speech.save("text.mp3")
        os.system("start text.mp3")

    def read_audio_file(self):
        # Reading Audio file as source
        # listening the audio file and store in audio_text variable
        with sr.AudioFile("") as source:
            audio_text = self.recognizer.listen(source)
            self.print_text(audio_text)

    def listen_audio(self):
        # Reading Microphone as source
        # listening the speech and store in audio_text variable
        with sr.Microphone() as source:
            print("Talk")
            audio_text = self.recognizer.listen(source)
            print("Time over, thanks")
            self.print_text(audio_text)

    def print_text(self, p_audio_text):
        # recognize() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            text = self.recognizer.recognize_google(p_audio_text, language="fr-FR")
            print('Converting audio transcripts into text ...')
            print(text)
        except:
            print('Sorry.. run again...')


speech_recognition = SpeechRecognition()
speech_recognition.play_audio()
