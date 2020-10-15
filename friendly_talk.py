from comtypes.client import CreateObject
from comtypes.gen import SpeechLib

text="Hi there, how are you?"
engine = CreateObject("SAPI.SpVoice")
stream = CreateObject("SAPI.SpFileStream")
stream.Open('audio.mp3', SpeechLib.SSFMCreateForWrite)
engine.AudioOutputStream = stream
engine.speak(text)
stream.Close()

# # Import the required module for text
# # to speech conversion
# import pyttsx3
#
# # init function to get an engine instance for the speech synthesis
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)  # <--- voice id can be male(0) or female(1)
#
# speech = input("Say Something: ")
#
# # # say method on the engine that passing input text to be spoken
# engine.say(speech)
#
# # # run and wait method, it processes the voice commands.
# engine.runAndWait()
