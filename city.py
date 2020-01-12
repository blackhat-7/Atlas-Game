import urllib.request
import urllib.parse
def response():
	url = 'https://pkgstore.datahub.io/core/world-cities/world-cities_json/data/5b3dd46ad10990bca47b04b4739a02ba/world-cities_json.json'
	response = urllib.request.urlopen(url)
	content = str(response.read().decode()) 
	return(content)
def valid(text,json):
	a = json.find(text)
	if(a==-1):
		return False
	else:
		return True

def get_city(start,content):
	i1 = content.find('"country": "'+start.upper())
	i2 = content.find('"name": "'+start.upper())
	temp = content
	if i1>i2:
		temp = temp[i1+12:]
		i3 = temp.find('"')
		return temp[:i3]
	else:
		temp = temp[i2+9:]
		i3 = temp.find('"')
		#print(content[::-1],i3)
		return temp[:i3]
#print(get_city('n'))