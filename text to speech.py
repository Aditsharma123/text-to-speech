import pyttsx3
engine = pyttsx3.init()
def say(audio):
  engine.say(audio)
  engine.runAndWait()

say("hello world")
