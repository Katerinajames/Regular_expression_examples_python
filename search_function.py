import re 

str="Python is a fascinating programming language"

result=re.search("is", str)

if result:
       print(result.group())
else:
	 print ("The specific word was not found")    
	
