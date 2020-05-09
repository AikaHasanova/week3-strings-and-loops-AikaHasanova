
word = input("enter any word : ")
length =len(word)

if length > 2:
    print ("Result:", word[0]+word[1]+word[-2]+word[-1])
else:
    print("String is empty")