a = 30
b = 5
c = a + b
d = c / 3
e = d - 4
print(e * 20)

parrot = "Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[3])
#print(parrot[14]) out of bounds
print(parrot[-1])
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:]) #Started @ 6 then runs till the end of the variable
print(parrot[-4:-2]) #can't do parrot[-4:2] because it doesn't make sense
print(parrot[0:6:2]) #Starts from index 0 to 6 then skips every 2nd char
print(parrot[0:6:3]) #Starts from index 0 to 6 then skips every 3rd char

number = "9,223,372,036,855,775,899"
print(number[1::4]) #Extracts portions of the string, i.e, it extracts only commas in the 4th place

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3]) #Extracted the no.s only, skipping commas and the whiespaces.

string1 = "he's "
string2 = "probably "
print(string1 + string2)

print("he's probably pining")
print("Hello " * 5)

#print("Hello" * 5 + 4) TypeError: must be str, not int

print("Hello" * 5 + "\t4") #Operator precedence applies to strings also.
print("Hello" * (5 + 4)) #Operator precedence applies to strings also.

today = "friday" #For searching variables used in algortihms
print("day" in today) #Return Boolean Value: True
print("fri" in today) #Return Boolean Value: True
print("thur" in today) #Return Boolean Value: False
print("parrot" in today)#Return Boolean Value: False

print("parrot" in "fjord") #Compare 2 strings