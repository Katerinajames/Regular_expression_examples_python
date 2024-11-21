import re 

str=input("Enter a string:\t")



if re.fullmatch("[A-Z][a-z]+",str):
	print("The string %s is valid"%(str))
else:
	print("The string %s is not valid"%(str)) 
   


   
	  
 
     
	
