import requests

#Set key values
data = {
	"token": "7fa0189d76ec2f2e1107a119c6c2f614",
}

#Make the request
apiRequest = requests.post("http://challenge.code2040.org/api/haystack", data )

#Save necessary values
needle = dict(apiRequest.json())["needle"]  
haystack = dict(apiRequest.json())["haystack"]

answer = 0

#Find the needle 
for i, hay in enumerate(haystack):
	if hay == needle:
		answer = i

#Send it back 
sentData = {
	
	"token": "7fa0189d76ec2f2e1107a119c6c2f614",
	"needle": answer 
}  

newApiRequest = requests.post("http://challenge.code2040.org/api/haystack/validate", sentData )

#Check if complete
print newApiRequest.text
