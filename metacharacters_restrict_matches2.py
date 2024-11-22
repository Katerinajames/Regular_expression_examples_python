import re 

string="Programming can be an  extremely challenging task"

result=re.search("task$",string)
	 
if result:
	 
	 print ("The  word that matches our regular expression is %s" %(result.group()) )

else:
	print ("There is no match")	
