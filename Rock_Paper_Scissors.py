###Rock Paper Scissors!###
import random

pbr = "Paper beats rock! "
sbp = "Scissors beats paper! "
rbs = "Rock beats scissors! "
win = "You Win!"
lose = "You Lose!"

print("Welcome to Rock, Paper Scissors!")
print()
print("Throw your hand and see what happens!")

print("Type rock for rock, paper for paper, and oh who am I kidding, you know how to play this game!")
print()
repeat = True
while repeat == True:
	user_input = input("What's your choice?: ")
	if user_input.lower() == "rock":
		user_choice = "rock"
	elif user_input.lower() == "paper":
		user_choice = "paper"
	elif user_input.lower() == "scissors":
		user_choice = "scissors"
	elif user_input.lower() == "gun":
		user_choice = "gun"
	elif user_input.lower() == "exit":
		"Thanks for playing!"
		#repeat == False
		break
	else:
		print("Maybe try another.. or spell scissors correctly...")
		continue


	possible_choices = ["rock", "paper", "scissors"]
	computer_choice = random.choice(possible_choices)

	#original
	'''if user_choice == computer_choice:
		print("Draw!")
	if user_choice == "rock" and computer_choice == "paper":
		print("Paper beats rock! You Lose..")
	if user_choice == "paper" and computer_choice == "rock":
		print("Paper beats rock! You Win!")
	if user_choice == "scissors" and computer_choice == "paper":
		print("Scissors beats paper! You Win!")
	if user_choice == "paper" and computer_choice == "scissors":
		print("Scissors beats paper! You Lose..")
	if user_choice == "rock" and computer_choice == "scissors":
		print("Rock beats scissors! You Win!")
	if user_choice == "scissors" and computer_choice == "rock":
		print("Rock beats scissors! You Lose!")'''

	print()
	#8.1 Revised strings
	print("Shoot!")
	print()
	if user_choice == computer_choice:
		print("Your opponent rolled " + str(computer_choice))
		print()
		print("Draw!")
	if user_choice == "rock" and computer_choice == "scissors":
		print("Your opponent rolled scissors!")
		print()
		print(rbs + win)	
	if user_choice == "paper" and computer_choice == "rock":
		print("Your opponent rolled rock!")
		print()
		print(pbr + win)
	if user_choice == "scissors" and computer_choice == "paper":
		print("Your opponent rolled paper!")
		print()
		print(sbp + win)
	if user_choice == "rock" and computer_choice == "paper":
		print("Your opponent rolled paper!")
		print()
		print(pbr + lose)
	if user_choice == "paper" and computer_choice == "scissors":
		print("Your opponent rolled scissors!")
		print()
		print(sbp + lose)
	if user_choice == "scissors" and computer_choice == "rock":
		print("Your opponent rolled rock!")
		print()
		print(rbs + lose)
	elif user_choice == "gun":
		print("Bang!")
		print()
		print(win)
	print("Say \'exit\' to quit")
	print("~~~~~~~~~~~~~~~~~~~~~~~")
	








