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

print("Grael Knight said: 'Hello'" + " Avi")