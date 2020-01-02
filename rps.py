from random import randint
computer_wins = 0
player_wins = 0
winning_score = int(input("How many winning matches to win a game?: "))

while player_wins < winning_score and computer_wins < winning_score:
	print(f"Player Score: {player_wins} Computer Score: {computer_wins}\n")
	print("Rock...")
	print("Paper...")
	print("Scissors...\n")

	player = input("Player_1: ")
	player = player.lower()
	if player == "quit" or player == "q":
		break

	computer_plays = randint(1,3)

	if computer_plays == 1:
		computer_plays = "rock"
	elif computer_plays == 2:
		computer_plays = "paper"
	else:
		computer_plays = "scissors"

	if player not in ["rock", "paper", "scissors", "r", "s", "p"]:
		print("You have to choose rock, paper or scissors!")	
	else:
		print(f"Computer plays: {computer_plays}")


	if player[0] == computer_plays[0]:
		print("It's a tie!")
	elif player[0] == "r":
		if computer_plays == "scissors":
			print("Player wins!")
			player_wins += 1
		else:
			print("Computer wins!")
			computer_wins += 1
	elif player[0] == "p":
		if computer_plays == "rock":
			print("Player wins!")
			player_wins += 1
		else:
			print("Computer wins!")
			computer_wins += 1
	elif player[0] == "s":
		if computer_plays == "paper":
			print("Player wins!")
			player_wins += 1
		else:
			print("Computer wins!")
			computer_wins += 1	

if computer_wins > player_wins:
	print(f"Computer won {computer_wins}:{player_wins}")
elif computer_wins < player_wins:
	print(f"Player won {player_wins}:{computer_wins}")
else:
	print(f"It's a Tie {player_wins}:{computer_wins}")
