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
    lucky = random.randint(1,101)
    tries = 0
    while True:
        num = int(input("please pick a number: "))
        tries += 1
        if num < lucky:
            print("lower number")
        elif num > lucky:
            print("higher number")
        else:
            print("bingo")
            break
    print("it took: ",tries, "guesses to user to guess")
  
  
