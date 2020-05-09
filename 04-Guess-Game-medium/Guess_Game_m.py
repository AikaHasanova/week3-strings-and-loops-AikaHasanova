print("Welcome to Guessing Game!")
num = 5
iterator = 0
#is_win = False
while iterator < 3:
  iterator+=1
  guess_num=int(input("guess the num "))
  if guess_num==num:
    print("Well guessed!")
    break
  else:
    print("invalid input:")
  #if is_win==True:
 #  print("Well guessed")
else:
   print("The game over")
