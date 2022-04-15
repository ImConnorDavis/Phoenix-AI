import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
#9, 14
engine.setProperty('voice', voices[61].id)
engine.say("Hello sir")
engine.say("How can I help")
engine.runAndWait()
