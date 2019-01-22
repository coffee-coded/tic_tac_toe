from classes.players import player
from classes.players import bcolors
print("""
		1 | 2 | 3
		---------
		4 | 5 | 6
		---------
		7 | 8 | 9

Give these values as input where you want to mark your territory

""")

grid = [[0,0,0],[0,0,0],[0,0,0]]


def show_grid():
	print("\n---------")
	for x in grid:
		print(" ", end="")
		for y in x:
			if(y==0):
				print("- ",end=" ")
			else:
				print(str(y) + "  ", end="")
		print("\n---------")


show_grid()

name1 = input("Player 1 : ")
player1 = player(name1,"x")
name2 = input("Player 2 : ")
player2 = player(name2,"O")

players = [player1,player2]
running = True


def take_input():
	chance = int(input(player.get_name() + " ,please specify where you wanan mark your territory : "))
	print(player.get_name() + " has choosen input as", chance)
	if chance == 1:
		if grid[0][0] != 0:
			print(bcolors.FAIL+bcolors.FAIL+bcolors.BOLD+"\nSorry, already taken!\n"+bcolors.ENDC+bcolors.ENDC)
			take_input()
		else:
			grid[0][0] = player.get_id()
	elif chance == 2:
		if grid[0][1] != 0:
			print(bcolors.FAIL+bcolors.BOLD+"\nSorry, already taken!\n"+bcolors.ENDC)
			take_input()
		else:
			grid[0][1] = player.get_id()
	elif chance == 3:
		if grid[0][2] != 0:
			print(bcolors.FAIL+bcolors.BOLD+"\nSorry, already taken!\n"+bcolors.ENDC)
			take_input()
		else:
			grid[0][2] = player.get_id()
	elif chance == 4:
		if grid[1][0] != 0:
			print(bcolors.FAIL+bcolors.BOLD+"\nSorry, already taken!\n"+bcolors.ENDC)
			take_input()
		else:
			grid[1][0] = player.get_id()
	elif chance == 5:
		if grid[1][1] != 0:
			print(bcolors.FAIL+bcolors.BOLD+"\nSorry, already taken!\n"+bcolors.ENDC)
			take_input()
		else:
			grid[1][1] = player.get_id()
	elif chance == 6:
		if grid[1][2] != 0:
			print(bcolors.FAIL+bcolors.BOLD+"\nSorry, already taken!\n"+bcolors.ENDC)
			take_input()
		else:
			grid[1][2] = player.get_id()
	elif chance == 7:
		if grid[2][0] != 0:
			print(bcolors.FAIL+bcolors.BOLD+"\nSorry, already taken!\n"+bcolors.ENDC)
			take_input()
		else:
			grid[2][0] = player.get_id()
	elif chance == 8:
		if grid[2][1] != 0:
			print(bcolors.FAIL+bcolors.BOLD+"\nSorry, already taken!\n"+bcolors.ENDC)
			take_input()
		else:
			grid[2][1] = player.get_id()
	elif chance == 9:
		if grid[2][2] != 0:
			print(bcolors.FAIL+bcolors.BOLD+"\nSorry, already taken!\n"+bcolors.ENDC)
			take_input()
		else:
			grid[2][2] = player.get_id()


while running:
	for player in players:
		fl = 0

		#horizontal check
		for i in range(2):
			if grid[i][0] == grid [i][1]==grid[i][2]:
				if grid[i][0] == player1.get_id():
					print(bcolors.WARNING+bcolors.BOLD+player1.get_name()+" won the game!"+bcolors.ENDC)
					running = False
					fl=1
					break
				elif grid[i][0] == player2.get_id():
					print(bcolors.WARNING+bcolors.BOLD+player2.get_name()+" won the game!"+bcolors.ENDC)
					running = False
					fl=1
					break

		#vertical check
		for i in range(2):
			if grid[0][i] == grid [1][i]==grid[2][i]:
				if grid[0][i] == player1.get_id():
					print(bcolors.WARNING+bcolors.BOLD+player1.get_name()+" won the game!"+bcolors.ENDC)
					running = False
					fl=1
				elif grid[0][i] == player2.get_id():
					print(bcolors.WARNING+bcolors.BOLD+player2.get_name()+" won the game!"+bcolors.ENDC)
					running = False
					fl=1

		#vertical check
		if grid[0][0] == grid [1][1]==grid[2][2]:
			if grid[1][1] == player1.get_id():
				print(bcolors.WARNING+bcolors.BOLD+player1.get_name()+" won the game!"+bcolors.ENDC)
				running = False
				fl=1
			elif grid[1][1] == player2.get_id():
				print(bcolors.WARNING+bcolors.BOLD+player2.get_name()+" won the game!"+bcolors.ENDC)
				running = False
				fl=1

		#vertical2 check
		if grid[0][2] == grid [1][1]==grid[2][0]:
			if grid[1][1] == player1.get_id():
				print(bcolors.WARNING+bcolors.BOLD+player1.get_name()+" won the game!"+bcolors.ENDC)
				running = False
				fl=1
			elif grid[1][1] == player2.get_id():
				print(bcolors.WARNING+bcolors.BOLD+player2.get_name()+" won the game!"+bcolors.ENDC)
				running = False
				fl=1

		if fl ==1 :
			break


		z=-1
#input adjustment
		take_input()



		show_grid()








