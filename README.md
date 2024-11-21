first_regular_expression.py

import re  :python standard regular expression library 

string="Hello"  

if re.fullmatch(string ,"H  ello"):fullmatch is a function that  examines if the first argument matches exaclty the second argument 
    print ("Match")
else:
	 print (" No Match") 



  
validating_a_zipcode.py
import re 

z="23458"

if re.fullmatch(r"\d{5}",z): \d  represents a digit between between 0 and 9 ,  {5}  is a quantifier that repeats \d 5 times  to match 5 CONSECUTIVE DIGITS 
	   print("It is valid")
else:
	  print ("It is not valid")


   

custom_character_classes.py

import re 

str=input("Enter a string:\t")

print("The string you have just entered is :%s"%(str))

if re.fullmatch("[A-Z][a-z]*", str):   A custom character class is defined by square brackets   which matches a single character .In our example we ensurwe that the string we will entere begins with an upper case letter followed by lower case 
	print("The string is valid")   letters
else:
     print("The string is not  valid")    The * quantifier means zero or more occurrences 


custom_character_classes2.py


str=input("Enter a string:\t")

print("The string you have just entered is :%s"%(str))

if re.fullmatch("[^a-z][a-z]*", str):  The string is valid  if it DOES NOT START WITH A LOWER CASE LETTER 
	print("The string is valid")
else:
     print("The string is not  valid")

     

custom_character_classes4.py

import re 

str=input("Enter a string:\t")



if re.fullmatch("[A-Z][a-z]+",str):  Our string must have AT LEAST ONE LOWERCASE LETTER 
	print("The string %s is valid"%(str))
else:
	print("The string %s is not valid"%(str)) 









