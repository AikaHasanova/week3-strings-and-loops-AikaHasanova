
num1= int(input("Enter first number : "))
num2= int(input("Enter second number : "))
num3= int(input("Enter third number : "))
num4= int(input("Enter fourth number : "))

numlist=[num1, num2, num3, num4]

even_count = 0
odd_count = 0

#increase even count else increase odd count.

for number in numlist:
    if number % 2 == 0:
        even_count+=1
    else:
     odd_count+=1

print("Even numbers :", even_count)
print("Odd numbers : ", odd_count)