# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1.lower() + name2.lower()

love_score_1 = name.count("t")
love_score_1 += name.count("r")
love_score_1 += name.count("u")
love_score_1 += name.count("e")

love_score_2 = name.count("l")
love_score_2 += name.count("o")
love_score_2 += name.count("v")
love_score_2 += name.count("e")

love_score = str(love_score_1) + str(love_score_2)

love_score = int(love_score)

if love_score < 10 or love_score > 90:
  print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
  print(f"Your love score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")