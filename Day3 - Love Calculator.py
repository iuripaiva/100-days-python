print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
combined_names = name1.lower() + name2.lower()

true_count = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")
love_count = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")

final_score = str(true_count)+str(love_count)
final_score = int(final_score)

if final_score < 10 or final_score > 90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score <=50 and final_score >= 40:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")
