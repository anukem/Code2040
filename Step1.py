import requests

#Set key values
data = {
	"token": "7fa0189d76ec2f2e1107a119c6c2f614",
	"github": "https://github.com/johnanukem/Code2040"
}

#Make the request
apiRequest = requests.post("http://challenge.code2040.org/api/register", data )

#Check the response
print apiRequest.text
