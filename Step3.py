import requests

#Set key values
data = {
	"token": "7fa0189d76ec2f2e1107a119c6c2f614",
}

#Make the request
apiRequest = requests.post("http://challenge.code2040.org/api/haystack", data )

needle = dict(apiRequest.json())["needle"]  
haystack = dict(apiRequest.json())["haystack"]

answer = 0
for i, hay in enumerate(haystack):
	if hay == needle:
		answer = i

sentData = {
	
	"token": "7fa0189d76ec2f2e1107a119c6c2f614",
	"needle": answer 
}  

newApiRequest = requests.post("http://challenge.code2040.org/api/haystack/validate", sentData )
print newApiRequest.text
