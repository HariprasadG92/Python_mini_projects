import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_moves = [rock, paper, scissors]
play = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if(play >=3 or play<0):
    print("You typed an invalid number! You lose!")
else:
    print(game_moves[play])

    bot = random.randint(0, 2)
    print("Bot choice:")
    print(game_moves[bot])

    if(play == bot):
        print("It's a Draw")
    elif(play == 2 and bot ==0):
        print("You Lose")
    elif(play == 0 and bot == 2):
        print("You WIN")
    elif(play > bot):
        print("You WIN")
    elif(play < bot):
        print("You Lose")