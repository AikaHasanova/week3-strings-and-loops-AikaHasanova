data=input("Enter the data :")
digit_count=0
letter_count=0

for n in data:
    if n.isdigit():
        digit_count=digit_count+1
    elif n.isalpha():
        letter_count=letter_count+1

print("Letter", letter_count,"numbers", digit_count)


