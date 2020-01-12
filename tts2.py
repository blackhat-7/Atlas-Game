from pydub import AudioSegment
from gtts import gTTS
import os
def speak(reply):
	tts=gTTS(reply)
	tts.save("good.mp3")

	sound=AudioSegment.from_mp3("good.mp3")
	sound.export("good.wav", format="wav")

	os.system("aplay -q good.wav")
