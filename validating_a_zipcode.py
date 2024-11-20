import re 
z="23458"
if re.fullmatch(r"\d{5}",z):
	   print("It is valid")
else:
	  print ("It is not valid")
