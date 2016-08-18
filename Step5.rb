require "unirest"
require "date"
#get response
response = Unirest.post "http://challenge.code2040.org/api/dating",
						parameters:{:token => "7fa0189d76ec2f2e1107a119c6c2f614"}

#save necessary info
datestamp = response.body["datestamp"]
interval = response.body["interval"]

datestamp = datestamp.to_s

#Compute new time
time = Time.new(datestamp[0..3].to_i, datestamp[5..6].to_i, 
				  datestamp[8..9].to_i, datestamp[11..12].to_i, 
				  datestamp[14..15].to_i, datestamp[17..18].to_i )
updatedTime = (time + interval).to_s
newanswer = updatedTime[0..updatedTime.size - 7] + "Z" 
finalAnswer = newanswer[0..9] + "T" + newanswer[11..newanswer.size]

#post the answer
newResponse = Unirest.post "http://challenge.code2040.org/api/dating/validate", 
							parameters:{:token => "7fa0189d76ec2f2e1107a119c6c2f614", :datestamp => finalAnswer}


#check the answer
print newResponse.body