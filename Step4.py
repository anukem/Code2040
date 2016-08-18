import requests
import json
#Set key values
data = {
	"token": "7fa0189d76ec2f2e1107a119c6c2f614",
}

#Make the request
apiRequest = requests.post("http://challenge.code2040.org/api/prefix", data )

#Save necessary values
prefix = dict(apiRequest.json())["prefix"]  
words = dict(apiRequest.json())["array"]

answer = []
print prefix

print words
#Find the non prefix words
for i in range(0, len(words)):
	if(words[i][0:len(prefix)] != prefix):
		answer.append(str(words[i]))


#Send it back 
sentData = {
	
	"token": "7fa0189d76ec2f2e1107a119c6c2f614",
	"array": answer
}  


newApiRequest = requests.post("http://challenge.code2040.org/api/prefix/validate", sentData )

#Check if complete
print newApiRequest.text