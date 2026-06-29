""" Print """
print("hello, world!!")


" Input "
print("Insert name")
"""var = input('>')
print(var) """


age = 19
price = 99999999.45
first_name = 'Milton'
surname = 'Rodriguez'
is_online = True

print(first_name.upper())
print(first_name.lower())
print(first_name)


""" Search """
character = 'M'
print(f"Search {character}, is in position: {first_name.find(character)}")
print(f"Is Mil on firstname?: {"Mil" in first_name}")



""" Operators """
print("Operators")
print(4 + 4)
print(4 - 4)
print(4 / 4)
print(4 * 4)
print(10 // 3)
print(10 % 3)
print(True and True and True)
print(True or False)
print(10 ** 3)
print("")

x = 10
y = 15
x = x + 1
y = y + 2
print(x)
print(y)
x = x + y * 3
print(x)

print("Proposition")
proposition = 1 > 2
print(proposition)

print(str(age) + " " + first_name + " xd")



weight = input('Insert weight>')
unit = input('(K)g  or  (L)b?>')
try:
    weight = float(weight)
    unit = unit.upper()

    if unit == 'K':
        print(f"You have {weight * 2.20462} pounds")
    elif unit == 'L':
        print(f"You have {round(weight * 0.453592, 2)} kilograms")
    else:
        print("Put K or L as character.")

except:
    print('Input has to be a number')
i = -5

while i<5:
    print(i)
    i = i + 1


""" Lists """
names = ["Pedro", "Juan", "Salchicha", "Your mother again here she goes", "Hola"]
names[0] = "Hola no soy pedrooo"

print(names)
names.append("El weso")

for name in names:
    print(name)
