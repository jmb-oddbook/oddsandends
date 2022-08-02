
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

dir1 = input("Which way do you want to go? Type 'left' or 'right'" ).lower()

if dir1 == "left":
  print("You have reached a river.")
  dir1 = input("Do you want to 'swim' or 'wait'? ").lower()
  if dir1 == "wait":
    print("While waiting three doors appear magically.")
    dir1 = input("Which door do you choose? 'Red', 'yellow', or 'blue'?").lower()
    if dir1 == "red":
      print("You open the red door. A huge gout of flames surges out. Crispy critter. Game Over.")
    elif dir1 == "blue":
      print("You open the blue door. The protesting hinges attract wildebeests, you are very tasty. Game Over.")
    elif dir1 == "yellow":
      print("Well done you. You survived. Game Won.")
    else: # did not enter either red, blue, or yellow
      print("You stand in the woods and can't decide which door to open. Slowly you grow older. \n\
Moss settles on your legs, a spider builds its web beneath your nose, birds nest in your hair. \n\
A tree gently places a branch over your shoulder. Somewhere, the hooting of an owl. Game Over.")
  else: # chose swim
    print("You jump into the river and are attacked and eaten by trout. Game Over.")
else: # chose right
  print("Fall into a hole. Game Over.")