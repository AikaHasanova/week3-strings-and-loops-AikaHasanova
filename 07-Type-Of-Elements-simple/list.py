def square():

 value = []
 num = 0
 while num < 5:
        num += 1
        res =int(input("Enter your number: "))
        value.append(res**2)
 return value

print(square())
