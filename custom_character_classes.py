import re 

str=input("Enter a string:\t")

print("The string you have just entered is :%s"%(str))

if re.fullmatch("[A-Z][a-z]*", str):
	print("The string is valid")
else:
     print("The string is not  valid")
   
	  
 
     
	
