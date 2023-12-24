import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
  left = random.randint(MIN_OPERAND, MAX_OPERAND)
  right = random.randint(MIN_OPERAND, MAX_OPERAND)
  operator = random.choice(OPERATORS)

  expression = str(left) + " " + operator + " " + str(right)
  answer = eval(expression)
  return expression, answer


input("Press enter to begin!")
print("-------------------------------")

wrong = 0
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
  expression, answer = generate_problem()
  while True:
    guess = input("Problem #" + str(i + 1) + ": " + expression + " = ")
    if guess == str(answer):
      break

end_time = time.time()
total_time = end_time - start_time


print("-------------------------------")
print("Great Job! Your total time is", round(total_time, 2), " seconds!")