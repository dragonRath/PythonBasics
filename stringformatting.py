#The following will illustrate the basic string formatting techniques used in python
age = 24
#print("My age is " + str(age) + " years\n")

print("My age is {0} years".format(age)) #{} Replacement brackets

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "January", "March", "May", "July", "August", "October", "December"))

print("""January: {2}
Feburary: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
Septemeber: {1}
October: {2}
November: {1}
December: {2}""". format(28, 30, 31))

print("\nGrael Knight said: 'Hello'" + " Avi")
print("\nMy age is %d years" %age)
print("\nMy age is %d %s, %d %s" %(age, "years", 6, "months")) #%d is int, %s is string; this replacement stands for all the variables

for i in range(1, 12): # ** means to the power of. %d = integer, %s = String, %f = Float
    print("Number %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3)) #The 2 or 4 before the %d is for allocating space. String formating.

print ("Pi is approximately %12f" %(22 / 7)) #Default float precision
print ("Pi is approximately %12.50f" %(22 / 7)) #50 decimal point precision
print ("Pi is approximately %0.50f" %(22 / 7)) #50 decimal point precision without giving extra space to the float.

for i in range(1, 12): #In {:}, the first no. is the replacement field whereas the second one is the width of the field. Don't put space between the colons. Gives an error.
    print("Number {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3)) #Don't put space between the colons. Gives an error.

for i in range(1, 12): #The < symbol justifies the left hand side, ie, it starts from the left instead of allocation from the right.
    print("Number {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print ("Pi is approximately {0:12.50}".format(22 / 7)) #Using replacement fields syntax

print("January: {2}, Feburary: {0}, March: {2}, April: {1}, May: {2}, June: {1}, July: {2}, August: {2}, Septemeber: {1}, October: {2}, November: {1}, December: {2}".format(28, 30, 31))

for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))