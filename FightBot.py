# Introduction
import random

print("Welcome to FightBot, sponsored by the Canadian House of Pizza and Garbage."
	  "You'll need to select moves to reduce your opponant's health to 0, while not dying yourself! "
	  "Ha. Ha ha. ha ha ha.")
your_name = str(input("Enter the name of your FightBot: "))
your_HP = 100
bot_HP = 100

#function to take the player's move choice, run the turn and return the new HP values
def player_turn(name, botHP, yourHP):
	move_choice = int(input("Enter a number from 1 to 3 to choose a move: "
							"1. House (dm 10-35) "
							"2. Garbage (dm 1-55 "
							"3. Pizza (heal 5-15)"))
	if move_choice == 1:
		print("%s used House" % name)
		dam1 = random.randint(10, 35)
		botHP = botHP - dam1
		print("It dealt %s damage!" % (dam1))
	elif move_choice == 2:
		print("%s used Garbage" % name)
		dam2 = random.randint(1, 55)
		botHP = botHP - dam2
		print("It dealt %s damage!" % (dam2))
	elif move_choice == 3:
		print("%s used Pizza" % name)
		heal1 = random.randint(5, 15)
		yourHP = yourHP + heal1
		print("It healed %s." % (heal1))
	else:
		print("That's not a move")
		player_turn(name, botHP, yourHP)
	return [botHP, yourHP]
#function to run the bot's turn using a random move and return the new HP values
def bot_turn(name, botHP, yourHP):
	move_choice = random.randint(1,3)
	if move_choice == 1:
		print("Opponent used House")
		dam1 = random.randint(10, 35)
		yourHP = yourHP - dam1
		print("It dealt %s damage!" % (dam1))
	elif move_choice == 2:
		print("Opponent used Garbage")
		dam2 = random.randint(1, 55)
		yourHP = yourHP - dam2
		print("It dealt %s damage!" % (dam2))
	elif move_choice == 3:
		print("Opponent used Pizza")
		heal1 = random.randint(5, 15)
		botHP = botHP + heal1
		print("Opponent healed %s." % (heal1))
	return [botHP, yourHP]

#Initialise variables
dead_check = True
turn_check = True
dbry = ['y', 'Y']
#loop to run both turns
while dead_check:
	turn_check1 = True
	turn_check2 = True
	#loop to run the player's turn
	while turn_check1:
		health = player_turn(your_name, bot_HP, your_HP)
		bot_HP = health[0]
		your_HP = health[1]
		if health[0] <=0:
			bot_HP = 0
		if health[1] <=0:
			your_HP = 0
		print("Your HP: %s    Opponent HP: %s" % (your_HP, bot_HP))
		dead_check = ((health[0]) > 0) and ((health[1]) > 0)
		if not dead_check:
			print("Game over!")
			again = str(input('Do you want to play again? Y/N')) in dbry
			dead_check = again
			turn_check2 = False
			your_HP = 100
			bot_HP = 100
		turn_check1 = False
	#loop to run the bot's turn
	while turn_check2:
		health = bot_turn(your_name, bot_HP, your_HP)
		bot_HP = health[0]
		your_HP = health[1]
		if health[0] <=0:
			bot_HP = 0
		if health[1] <=0:
			your_HP = 0
		print("Your HP: %s    Opponent HP: %s" % (your_HP, bot_HP))
		dead_check = ((health[0]) > 0) and ((health[1]) > 0)
		if (not dead_check):
			print("Game over!")
			dead_check = str(input('Do you want to play again? Y/N')) in dbry
			turn_check2 = False
			your_HP = 100
			bot_HP = 100
		turn_check2 = False
#end
print('Thanks for playing FightBot')

