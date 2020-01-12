import audio
import city
import store
import tts2

score = 0
isPlaying = 0
name = input("Enter your name: \n")
reply_ending = 'A'
prompt = 'Tell a city or a country starting with A'
content = city.response()
dnrtries = 0
typed = False
while isPlaying<3:
	print(prompt)
	if dnrtries<3:
		current_city = audio.get_place()
		if current_city=="exit":
			print("I Give up.")
			break
		typed = False
	else:
		current_city = input("Type a city or a country starting with "+reply_ending.upper()+ ":\n")
		typed = True
	if current_city == None:
		prompt = 'Did not recognize, Try again' + "\n"
		dnrtries += 1
	else:
		dnrtries = 0
		if not typed:
			print(current_city + "...\n")
		if content.upper().find(current_city.upper())==-1:
			if typed:
				prompt = "This place does not exist, please type again" + "\n"
			else:
				prompt = "You may have already told this, please try again" + "\n"
			isPlaying +=1
		elif reply_ending.upper()!=current_city[:1].upper():
			prompt = "It is not starting with " + reply_ending.upper() + ", try again" + "\n"
			isPlaying +=1
		else:
			score += 10
			content = content.replace(current_city,'')
			ending = current_city[-1:]
			reply = city.get_city(ending,content)
			tts2.speak(reply)
			content = content.replace(reply,'')
			print("Computer replies with " + reply + "...\n")
			reply_ending = reply[-1:]
			prompt = 'Tell a city or a country starting with ' + reply_ending.upper() + "\n"

store.save(score,name)
leaderboard = store.leader()
if(leaderboard['1st'][1]>score):
	tts2.speak("Don't worry, Not everyone is a computer")
else:
	tts2.speak("Go get a life, Nerd!")
	
print("\n 1st : " + leaderboard['1st'][0] + " - " + str(leaderboard['1st'][1]) + "\n 2nd : " + leaderboard['2nd'][0] + " - " + str(leaderboard['2nd'][1]) + "\n 3rd : " + leaderboard['3rd'][0] + " - " + str(leaderboard['3rd'][1]) + "\n")
print("Game Over!! Your score is: " + str(score))
