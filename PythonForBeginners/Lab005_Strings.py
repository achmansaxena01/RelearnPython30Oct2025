s = "Hi !! My name is Achman ||*||"
sd = 'anubhav'
print(s)
print(sd)
sa = '''you are the 
creator of your destiny'''
s1 = 'asdfghjk'
s2 = "   * This is the actual information.     "

print(sa)
print(s[0]) # to print the first character from starting
print(s*3)  #to print it 3 times
print(len(s))  # to print length of string

print(s[0:20])  #to print the characters between this including the lower limit and (n-1)
print(s[:8])  #to print from starting till (n-1)th position
print(s[7:])  #to print from lower limit till end
print(s1[-4:])   #to print from lower limit till end
print(s1[-4:-1])   #to print from lower limit till end
print(s1[0:9:2])   #to print from lower limit till end with a step value
print(s[9::-2])   #to print from lower limit till end with a step value

print(s[::-1]) # reverse a string
print(s2.strip())   # to strip the extra spaces from bot sides.
print(s2.lstrip())  # to strip spaces from left
print(s2.rstrip())  # to strip spaces from right
print(s2.find("a",0, len(s2)))  # to find substring with in a string
print(s2.count("a"))    # to count the number of ties that string is present.
print(s2.replace("a","(new)")) # to replace  the string with new

print(s2.upper())   # to see the uppercase version of the string
print(s2.lower())   # to see the lowercase version of the string
print(s2.title())   # to see the titlecase version of the string

