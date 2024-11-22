import re 

string="I like maths"

result=re.search("^I",string)
	 
if result:
	 
	 print ("The  word that matches our regular expression is %s" %(result.group()) )

else:
	print ("There is no match")	
