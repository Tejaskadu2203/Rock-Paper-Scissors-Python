from playsound import playsound
import random

# Define game rules
rules = {
    "rock": {"scissor": "win", "paper": "lose"},
    "paper": {"rock": "win", "scissor": "lose"},
    "scissor": {"paper": "win", "rock": "lose"}
}

# User and computer choices
user1 = input("Please select Rock, Paper, or Scissor: ").lower().strip()
select = ["rock", "paper", "scissor"]
user2 = random.choice(select)
print("Computer Chose:", user2)

# Game logic
if user1 == user2:
    print("Match Draw")
elif rules.get(user1) and rules[user1].get(user2) == "win":
    print("You Won")
    playsound("sound.mp3")
elif rules.get(user1) and rules[user1].get(user2) == "lose":
    print("You Lose")
    playsound("youlose.mp3")
else:
    print("Invalid input! Please select Rock, Paper, or Scissor.")
