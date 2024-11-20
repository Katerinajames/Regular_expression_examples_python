

import re  :python standard regular expression library 

string="Hello"  

if re.fullmatch(string ,"H  ello"):fullmatch is a function that  examines if the first argument matches exaclty the second argument 
    print ("Match")
else:
	 print (" No Match") 


import re 
z="23458"
if re.fullmatch(r"\d{5}",z): \d  represents a digit between between 0 and 9 ,  {5}  is a quantifier that repeats \d 5 times  to match 5 CONSECUTIVE DIGITS 
	   print("It is valid")
else:
	  print ("It is not valid")
