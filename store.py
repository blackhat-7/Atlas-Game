import pickle
def save(point,user):
	# data = {'1st': ['computer',0],'2nd':['computer',0] , '3rd' :['computer',0]}
	# pickle.dump(data,open('data.dat','wb'))
	data = pickle.load(open('data.dat','rb'))
	if(point>data['1st'][1]):
		data['3rd'] = data['2nd']
		data['2nd'] = data['1st']
		data['1st'] = [user,point]
	elif(point>data['2nd'][1]):
		data['3rd'] = data['2nd']
		data['2nd'] = [user,point]
	elif(point>data['3rd'][1]):
		data['3rd'] = [user,point]
	pickle.dump(data,open('data.dat','wb'))

def leader():
	lead = pickle.load(open('data.dat','rb'))
	return(lead)

