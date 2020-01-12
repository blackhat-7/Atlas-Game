import speech_recognition as sr 
import city

def get_place():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio)
			if text.lower() == "i give up":
				return "exit"
			else:
				query =city.valid(text,city.response())
				if query:
					return text
				else:
					return None
		except:
			return None
