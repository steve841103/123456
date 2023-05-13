import random

number = []

i = 0
while i < 6:
    x = random.randint(1,49)
    if x not in number:
        number.append(x)
        i += 1
sorted(number)
print(number, end = " ")


y= random.randint(1,49)
print(f'特別號為{y}')

