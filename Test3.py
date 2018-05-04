a: int = 12
b: int = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)  #By default Python returns float numbers for division
print(a // b) #Returns whole number(integer) as a result
print(a % b)

for i in range(1, a//b):
    print(i)

print(a + b / 3 -4 * 12) #-35 because of operator precedence [b/3, -4 * 12, a - 48]
print(8 / 2 * 3)
print(8 *3 / 2)

print((( (a+b) / 3) -4) * 12)