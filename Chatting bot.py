import time

def greet(bot_name, birth_year):
  print(f"Hello! My name is {bot_name}.\nI was created in {birth_year}.")

def remind_name():
  print("Please, remind me your name.")
  name = input()
  print(f"What a great name you have, {name}!")

def guess_age():
  print("Let me guess your age.\nEnter remainders of dividing your age by 3, 5 and 7.")

  rem3 = int(input("Remainder of your age by 3: "))
  rem5 = int(input("Remainder of your age by 5: "))
  rem7 = int(input("Remainder of your age by 7: "))
  age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

  print(f"Your age is {age}; that's a good time to start programming!")

def count():
  print("Now I will prove to you that I can count to any number you want.")

  num = int(input())
  curr = 0
  while curr <= num:
    time.sleep(1)
    print(f"{curr} !")
    curr += 1

def test():
  print(f"Let's test your programming knowledge.\nWhy do we use methods?")
  print("""1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")
  answer = 0
  answer = int(input())
  while answer != 2:
    print("Please, try again.")
    answer = int(input())
  print("Verifying...")
  time.sleep(1)
  print("\nCompleted, have a nice day!")

def end():
  print("Congratulations, have a nice day!")

greet('H3O', '2021')
remind_name()
guess_age()
count()
test()
end()