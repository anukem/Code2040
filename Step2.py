import requests

#Set key values
data = {
	"token": "7fa0189d76ec2f2e1107a119c6c2f614",
}

#Make the request
apiRequest = requests.post("http://challenge.code2040.org/api/reverse", data )

#Flip the response
reversedWord = apiRequest.text[::-1]

#See if it worked
print(apiRequest.text)
print(reversedWord)

newData = {
	
	"token": "7fa0189d76ec2f2e1107a119c6c2f614",
	"string": reversedWord 
}
#Send it back
newApiRequest = requests.post("http://challenge.code2040.org/api/reverse/validate", newData)

print newApiRequest.text
