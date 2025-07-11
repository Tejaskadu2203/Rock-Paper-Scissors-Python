from playsound import playsound
import random
user1=input("Please select what you want Rock,Paper or Scissor: ").lower().strip()
select=["rock","paper","scissor"]
user2= random.choice(select).lower().strip()
print("Computer Chose: ",user2)
if user1=="rock" and user2=="paper":
        print("You Lose")
        playsound("youlose.mp3")    
elif user1=="paper" and user2=="rock":
        print("You Won")
        playsound("sound.mp3")
elif user1=="scissor" and user2=="paper":
        print("You Won")
        playsound('sound.mp3')
elif user1=='rock' and user2=="scissor":
        print('You Won')
        playsound('sound.mp3')
elif user1=='rock' and user2=='rock':
        print('Match Draw')
elif user1=="paper" and user2=="scissor":
        print("You Lose")
        playsound('youlose.mp3')
elif user1=="paper" and user2=="paper":
        print("Match Draw")
elif user1=="scissor" and user2=="rock":
        print("You Lose")
        playsound('youlose.mp3')
elif user1=="scissor" and user2=="scissor":
        print("Match Draw")