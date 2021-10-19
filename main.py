targil 1:
  
def printnums():
    for i in range(1,101):
        print(i)
        
targil 2:
  
def prints():
  x = 10
  for i in range(0,x+1):
      print(i)
        
targil 3:
  
import random

def luckynum():
    lucky = random.randint(1,100)
    tries = 0
    while True:
        num = int(input("please pick a number: "))
        tries += 1
        if num < lucky:
            print("too low")
        elif num > lucky:
            print("too high")
        else:
            print("bingo")
            break
    print("it took: ",tries, "guesses to user to guess")
  
  
targil 4:

  
import random

def luckynum():
    lucky = random.randint(1,100)
    tries = 0
    while True:
        num = int(input("please pick a number: "))
        tries += 1
        if num < lucky:
            print("too low")
        elif num > lucky:
            print("too high")
        else:
            print("bingo")
            break
    return tries


for i in range(0,3):
    result = luckynum()
    if i == 0:
        min_tries = result
    elif result > min_tries:
        min_tries = result

print(f"minimum tries is: {min_tries}")
