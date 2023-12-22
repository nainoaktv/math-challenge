import random

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


for i in range(TOTAL_PROBLEMS):
  expression, answer = generate_problem()
  while True:
    guess = input("Problem #" + str(i + 1) + ": " + expression + " = ")
    if guess == str(answer):
      break