import re 

str=input("Enter a string:\t")

print("The string you have just entered is :%s"%(str))

if re.fullmatch("[^a-z][a-z]*", str):
	print("The string is valid")
else:
     print("The string is not  valid")
   
	  
 
     
	
