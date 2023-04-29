import random
from stages import stage, logo
from word_list import words

print(logo)

word = random.choice(words)
wrd_len = len(word)
lives = 6
print(word)

dis = []
for i in range(wrd_len):
    dis += "_"
print(f"{' '.join(dis)}")

end_of_game = False

while not end_of_game:
    guess = input("Enter letter to guess: ")
    
    if guess in dis:
        print(f"You have already gussed the letter {guess}")
    for pos in range(wrd_len):
        letter = word[pos]
        if letter == guess:
            dis[pos] = letter
            
    if guess not in word:
        print((f"You have gusses {guess}, that's not in the word, you lose a life"))
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost all your life\n!! YOU LOSE !!")
            
    print(f"{' '.join(dis)}")
     
    print(stage[lives])
      
    if "_" not in dis:
        end_of_game = True
        print("!!! YOU WiN !!!")
        
    
