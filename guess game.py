#guess the number game
number = 17
print("What's My number? Enter Your Guess.\nYou have total of 9 attempts.")
guess = 9
while guess>0:
    x = int(input())
    if x>number:
        print("Your guess is greater than my number.")
        guess = guess-1
        print("Left attempts:",guess)
        continue
    elif x<number:
        print("Your guess is lesser than my number.")
        guess = guess - 1
        print("Left attempts:", guess)
        continue
    else:
        print("CONGRATULATIONS.\nYou have won the game.")
        break
if guess==0:
    print("You are out of attempts now.\nYou LOST.")