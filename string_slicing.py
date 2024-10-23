# Strings are immutable
a="Shubham is genius"
print(len(a)) #to find length of string
print(a.upper()) #to upper case
print(a.lower()) # to lower case
print(a.capitalize()) # 1st letter becomes capital
print(a.swapcase()) # to swap case
print(a.title()) # to capitalize first letter of each words
print(a.center(150)) #Return a centered string of length width.Padding is done using the specified fill character (default is a space).
print(a.casefold()) #Return a version of the string suitable for caseless comparisons.
  #return true or false
str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.
str1 = "Welcome"
print(str1.isalpha()) # A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

str1 = "hello world"
print(str1.islower()) #A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable()) #A string is printable if all of its characters are considered printable in repr() or if it is empty.
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is")) # Return -1 on failure. Return lowest index if success

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))
print(str1.replace("Python", "ruby"))

#Fstring 
var="Shubham"
print(f"My Name is {var}")

#doc string
def text(var):
    '''Testing F-string'''
    print(f"My name is {var}")

text(var)
print(text.__doc__)

nvar='''this is    
multi line 
text'''             # multi line string
print(nvar)