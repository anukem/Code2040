require "unirest"

#get response
response = Unirest.post "http://challenge.code2040.org/api/prefix",
						parameters:{:token => "7fa0189d76ec2f2e1107a119c6c2f614"}

#save necessary info
prefix = response.body["prefix"]
array = response.body["array"]

answer = Array.new()

#Find all non prefix words
array.each do |word|
	
	if !word.start_with? prefix
		answer.push(word)
	end

end

#post the answer
newResponse = Unirest.post "http://challenge.code2040.org/api/prefix/validate", 
							parameters:{:token => "7fa0189d76ec2f2e1107a119c6c2f614", :array => answer}

puts answer
#check the answer
print newResponse.body
