# These are the rules of the FizzBuzz game:
# The program will print each number from 1 to 100 in turn and include number 100.
# When the number is divisible by 3 then instead of printing the number it will print "Fizz".
# When the number is divisible by 5, then instead of printing the number it will print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it will print "FizzBuzz"

for number in range (1, 101):
  if number % 3 == 0 and number % 5 == 0: # If the number is divisible by both 3 and 5
    print("FizzBuzz")
  elif number % 3 == 0: # If the number is divisible by 3
    print("Fizz")
  elif number % 5 == 0: # If the number is divisible by 5
    print("Buzz")
  else:
    print(number)
