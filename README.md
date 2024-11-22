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

replace_strings2.py

import re 

str="I like regular expressions"


k=re.sub("s","x",str) :we call the function sub and we relace  s with x in string str 

print ("Our string after the repacement of s with  x")

print(k)



split_function.py


import re 

txt = "Hello	there"
x = re.split(" \t", txt) The split function splits the string by the the occurrences of the regular expression pattern 
print(x)




search_function.py


import re 

str="Python is a fascinating programming language"

result=re.search("is", str)   Function search  looks in a given string for the FIRST occurrence of a regular expression 

if result:
       print(result.group())
else:
	 print ("The specific word was not found") 


metacharacters_restrict_matches.py


import re 

string="I like maths"

result=re.search("^I",string)  The ^ metacharacter at the beginning of a regular expression  indicates that the expression matches only the beginning of a string 
	 
if result:
	 
	 print ("The  word that matches our regular expression is %s" %(result.group()) )

else:
	print ("There is no match")













  









