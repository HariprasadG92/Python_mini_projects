print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

leve1 = input("Enter the directin you want to go left or right ? ")
lc_leve1 = leve1.lower()
if lc_leve1 == "left":
    print("You have ended up near a lake")
else:
    print("You have fell into a hole and died \n   !!!!! GAME OVER !!!!!")
leve2 = input("Do you want to swim or wait for a boat ? ")
lc_leve2 = leve2.lower()
if lc_leve2 == "wait":
        print("You have successfully crossed the lake ")
else:
        print("You have been eaten by the crocodiles \n   !!!!! GAME OVER !!!!!")
leve3 = input("You have to choose a color from VIBGYOR (Violet-Indigo-Blue-Green-Yellow-Orange-Red) for the final level ")
lc_leve3 = leve3.lower()
if lc_leve3 == "yellow":
    print(" !!!! COONGRATULATIONS\n\n      YOU WON THE GAME\n")
elif lc_leve3 == "indigo":
    print("You fell into snake pit\n !!! GAME OVER !!!\n")
elif lc_leve3 == "blue":
    print("You got poisoned\n !!! GAME OVER !!!\n")
elif lc_leve3 == "red":
    print("You fell into lava \n !!! GAME OVER !!!\n")
elif lc_leve3 == "orange":
    print("You fell into a fire pit\n !!! GAME OVER !!!\n")
elif lc_leve3 == "green":
    print("You got killed by spikes\n !!! GAME OVER !!!")
elif lc_leve3 == "violet":
    print("You were killed by a ghost\n !!! GAME OVER !!!")
else:
    print("WRONG CHOICE \n    !!! GAME OVER !!!")