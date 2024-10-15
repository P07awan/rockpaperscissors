import random
options=("rock","paper","scissors")
player=None
computer=random.choices(options)
while player not in options:
  player=input("User inputs:(rock,paper,scissors)")
print(f"player:{player}")
print(f"computer:{computer}")
if player==computer:
    print('draw!')
elif player=="paper"and computer =="stone": 
    print("user wins!")
else :
    print('user lost!')     

