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
print(parrot[6:])
print(parrot[-4:-2]) #cannot do parrot[-4:2]
print(parrot[0:6:2]) #Starts from index 0 to 6 then extract char skipping 2
print(parrot[0:6:3]) #Starts from index 0 to 6 then extract char skipping 3

number = "9,223,372,036,855,775,899"
print(number[1::4])
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])
string1 = "he's "
string2 = "probably "
print(string1 + string2)
print("he's probably pining")
print("ello" * 5)

#print("Hello" * 5 + 4) TypeError: must be str, not int

print("Hello" * 5 + "\t4")

today = "friday"
print("day" in today) #Return Boolean Value: True
print("fri" in today) #Return Boolean Value: True
print("thur" in today) #Return Boolean Value: False
print("parrot" in today)#Return Boolean Value: True