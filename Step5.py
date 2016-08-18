import requests
import datetime



#Set key values
data = {
	"token": "7fa0189d76ec2f2e1107a119c6c2f614",
}

#Make the request
apiRequest = requests.post("http://challenge.code2040.org/api/dating", data )

#Save necessary values
datestamp = dict(apiRequest.json())["datestamp"]  
interval = dict(apiRequest.json())["interval"]

#Compute answer
answer = datetime.datetime(year=int(datestamp[0:4]), 
						month=int(datestamp[5:7]), 
						hour=int(datestamp[11:13]), 
						day=int(datestamp[8:10])) + datetime.timedelta(seconds=interval)

#Format properly
answer = str(answer)
answer = answer[0:10] + "T" + answer[11:len(answer)] + "Z"

#Send back
newData = {
	
	"token": "7fa0189d76ec2f2e1107a119c6c2f614",
	"datestamp": answer
}

newApiRequest = requests.post("http://challenge.code2040.org/api/dating/validate", newData )


#Check if it worked
print newApiRequest.text