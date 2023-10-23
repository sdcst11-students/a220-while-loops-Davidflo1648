#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
inputNum = float(input("Enter a number: "))

is_even = False

while inputNum > 0:
  if inputNum != int(inputNum):
    break
  if inputNum % 2 == 0:
    is_even = True
    break
  inputNum = inputNum / 10

if is_even:
  print("The number is an even integer.")
else:
  print("The number is not an even integer.")

