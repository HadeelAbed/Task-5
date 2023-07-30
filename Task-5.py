#1)
name=input("Enter your name: ")
age=input("Enter your age: ")
street=input("Enter your street: ")
city=input("Enter your city: ")
country=input("Enter your country: ")

#2)
print( f"\t\t\"Name :{name}\"\n\t\t\"age :{age}\"\n\"Address :{street},{city},{country}\"\n ")

#3)
age=int(age)-5
print(f"\"Hello {{{name}}} Your age is {age} Years Old , Your Address is {street}, {city}, {country}.\"")

#4)
print(f"{type(name)} {type(age)}\n{type(street)} {type(city)}\n\t\t{type(country)}")


#5)
print(f"\" Hello \'{name}\', How Are You? \\ \"\"\" Your Age Is \"{age}\"\"\n+\ And Your Country Is:{country}")

#6)
print(f'''Hello \'{name}\' , How Are You? \\
\"\"\" Your Age Is \"{age}\"\" + And
 Your City is : {city}''')

#7)
name = 'Doaa Reem'
print(f'''
First Letter Is {name[0]}
Third Letter Is {name[2]}
Last Letter Is {name[-1]}''')

#8)
print(f'''{name[6:]}
{name[0:4]}
{name[2].upper()}{name[3]}{name[4:7]}
{name[-1:-5:-1]}
{name[0:3:2]}{name[4:7:1]}''')

#9)
name = "$&$&Mohammed$&$&"
print(name.strip('$&'))

#10)
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace('%7',"love"))

#Bonus (+2 Marks)
#11)
ex="hello , world "
print(ex.title())#returns a string  which has first letter in each word is uppercase and all remaining letter are lowercase
print(ex.capitalize())#returns a string  that has first letter of the first word in uppercase and all remaining letter are lowercase

#12):
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
#The zfill() method adds zeros (0) at the beginning of the string
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))

#13)
first_name = "Hadeel"
# string * num = repeating strings to a certain length.
stars = "*" * 11

print(stars,first_name)
print(stars,first_name,stars)
print(first_name,stars)

#14)

name_one = "HaLA"
name_two = "shaHD"
print(f'''{name_one[0].lower()}{name_one[1].upper()}{name_one[2:].lower()}
{name_two[0:3].upper()}{name_two[3:].lower()}
{name_one.lower()}
{name_two.upper()}
''')
#15)

if name_one.isupper() and name_two.islower():
    print(f"name_one contains Only Upper Case letters, and name_two contains Only Lower Case letters?")
else:
    print("name_one does not contain only uppercase letters && name_two does not contain only lowercase letters.")

#16)

if name_one[0]=='S':
    print("name_one starts with (S)")
else:
    print("Not")
if name_two[-1]=='D' and name_two[-2]=='H':
    print("name_two ends with (HD) letters")
else:
    print("Not")
#17)

msg = "I Love Python And Although I Love GSG with Zakaria"
print(f"The word (Love) appears {msg.count('Love')} times, and the letter (t) {msg.count('t')} times ")

#18)

name = "Zakaria"
print(f"the position of the letter ( r ) {name.index('r')}")

#19)

msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7","Love",1))
