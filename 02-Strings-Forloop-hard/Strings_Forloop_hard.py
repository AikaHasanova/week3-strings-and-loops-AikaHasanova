str= "google.com"
count = {}
for letter in str:
    if letter in count:
        count[letter] += 1
    else:count[letter]=1
print("Count each letter  : ", count)


"""String = "google.com"

for letter in set(string):

    print(letter, " ",string.count(letter))"""
