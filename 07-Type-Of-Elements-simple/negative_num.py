#Write a program that prints the negative numbers and
#their indexes in the list.
#Our list consists of negative and positive numbers


list = [1,2,3,4,-1,-2,-3,-4]
for num in list:
     if num < 0:
         print("Negative numbers:", num)
         print(f"index {num} is {list.index(num)}")




