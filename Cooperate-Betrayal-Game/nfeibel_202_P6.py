#-------------------------------------------------------------------------------
# Name: Nick Feibel
# Project 6
# Date: 12/4/2019
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Class lectures
#-------------------------------------------------------------------------------
# Comments and assumptions: Nick Feibel, nfeibel, G01164484, CS-112-202, no
# collaboration partners. Thanks for grading this!
# What I found most useful was checking the test cases.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------
##########################################################################


#////////////////////////////////////////////////////////////////////////
#Below class represents a Move and whether it is to cooperate or not.
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class Move:

	#########################################################################
	#Below function defines the variables for the Move class. Cooperate's
	#default is set to default.
	#-----------------------------------------------------------------------
	def __init__(self, cooperate=True):
		self.cooperate = cooperate
	
	
	#########################################################################
	#Below function returns a string representation of the move. "x" if they
	#cheated and "." if they cooperated.
	#-----------------------------------------------------------------------
	def __str__ (self):
		if self.cooperate == True:
			return "."
		else:
			return "x"
	
	
	#########################################################################
	#Below function returns a representation of the move as Move(True/False)
	#where it is True if they cooperate, False if they cheat.
	#-----------------------------------------------------------------------
	def __repr__(self):
		return "Move("+str(self.cooperate)+")"


	#########################################################################
	#Below function checks whether 2 moves are the same as each other and
	#returns True if so.
	#-----------------------------------------------------------------------
	def __eq__(self, other):
		if self.cooperate == other.cooperate:
			return True
		return False
	
	
	#########################################################################
	#Below function changes the move to the opposite boolean value.
	#-----------------------------------------------------------------------
	def change(self):
		self.cooperate = not self.cooperate
	
	
	#########################################################################
	#Below function makes a copy of the move.
	#-----------------------------------------------------------------------
	def copy(self):
		newMove = Move(self.cooperate)
		return newMove


#////////////////////////////////////////////////////////////////////////
#Below class represents a PlayerException that will confirm an exception
#in other functions in this program.
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\		
class PlayerException(Exception):
	
	#########################################################################
	#Below function initializes the exception with the confirmed message.
	#-----------------------------------------------------------------------
	def __init__(self, msg):
		self.msg = msg
	
	
	#########################################################################
	#Below function returns the exception message.
	#-----------------------------------------------------------------------
	def __str__(self):
		return self.msg
	
	
	#########################################################################
	#Below function provides a representation of the exception as
	#PlayerException(msg) where msg is the exception message.
	#-----------------------------------------------------------------------
	def __repr__(self):
		return "PlayerException('"+self.msg+"')"


#////////////////////////////////////////////////////////////////////////
#Below class represents a Player which has a style, points, and history.
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\		
class Player:

	#########################################################################
	#Below function initializes the variables for the Player class.
	#Points are defaulted to 0 and history to an empty list if either are
	#not provided. A PlayerException is raised if the style is not one
	#of the confirmed styles.
	#-----------------------------------------------------------------------
	def __init__(self, style, points=0, history=None):
		if style not in ['previous', 'friend', 'cheater', \
			'grudger', 'detective']:
			raise PlayerException("no style '" + style+"'.")
		else:
			self.style = style
		self.points = points
		if history  == None:
			self.history = []
		else:
			self.history = history
	
	
	#########################################################################
	#Below function returns a string representation of the player's style
	#and move history.
	#-----------------------------------------------------------------------
	def __str__(self):
		moves = self.style+"("+str(self.points)+")"
		for i in range(len(self.history)):
			moves = moves + str(self.history[i])
		return moves
	
	
	#########################################################################
	#Below function returns a representation of the player's style and the
	#history.
	#-----------------------------------------------------------------------	
	def __repr__(self):
		string = "Player('"+self.style+"', "+str(self.points)+", ["
		for i in range(len(self.history)):
			if i == len(self.history)-1:
				string = string +repr(self.history[i])
			else:
				string = string + repr(self.history[i])+", "
		string = string +"])"
		return string
	
	
	#########################################################################
	#Below function resets the history of this player.
	#-----------------------------------------------------------------------	
	def reset_history(self):
		self.history = []
	
	
	#########################################################################
	#Below function resets the history and points for this player.
	#-----------------------------------------------------------------------
	def reset(self):
		self.history = []
		self.points = 0
	
	
	#########################################################################
	#Below function updates the player's points with the amount confirmed.
	#-----------------------------------------------------------------------
	def update_points(self, amount):
		self.points = self.points + amount
	
	
	#########################################################################
	#Below function confirms whether the player has been betrayed or not.
	#-----------------------------------------------------------------------
	def ever_betrayed(self):
		if Move(False) in self.history:
			return True
		else:
			return False
	
	#########################################################################
	#Below function appends a move to the history list.
	#-----------------------------------------------------------------------
	def record_opponent_move(self, move):
		self.history.append(move)
	
	
	#########################################################################
	#Below function returns a copy of the current player with the same style.
	#-----------------------------------------------------------------------
	def copy_with_style(self):
		newPlayer = Player(self.style, 0, None)
		return newPlayer
	
	
	#########################################################################
	#Below function confirms the next move of the player depending on
	#which style they are.
	#-----------------------------------------------------------------------
	def choose_move(self):
		if self.style == "previous":
			if len(self.history) > 0:
				return self.history[-1]
				
			else:
				return Move(True)
				
		elif self.style == "friend":
			return Move(True)
			
		elif self.style == "cheater":
			return Move(False)
			
		elif self.style == "grudger":
			if len(self.history) == 0:
				return Move(True)
				
			elif self.ever_betrayed():
				return Move(False)
				
			else:
				return Move(True)
			
		else:
			if len(self.history) == 0:
				return Move(True)
				
			elif len(self.history) == 1:
				return Move(False)
				
			elif len(self.history) == 2:
				return Move(True)
				
			elif len(self.history) == 3:
				return Move(True)
				
			else:
				if not self.ever_betrayed():
					return Move(False)
					
				else:
					return self.history[-1]
					
					
#########################################################################
#Below function confirms the turn payouts depending on what moves are made.
#-----------------------------------------------------------------------
def turn_payouts(move_a, move_b):
	if move_a.cooperate and move_b.cooperate == True:
		return (2,2)
		
	elif (move_a.cooperate == False) and (move_b.cooperate == False):
		return (0,0)
		
	else:
		if move_a.cooperate == False:
			return (3,-1)
			
		else:
			return (-1,3)


#########################################################################
#Below function confirms the turn payouts depending on what moves are made.
#-----------------------------------------------------------------------			
def build_players(initials):

	playerList = []
	
	for i in initials:
		if i == 'p':
			playerList.append(Player('previous'))
			
		elif i == 'f':
			playerList.append(Player('friend'))
			
		elif i == 'c':
			playerList.append(Player('cheater'))
			
		elif i == 'g':
			playerList.append(Player('grudger'))
			
		elif i == 'd':
			playerList.append(Player('detective'))
			
		else:
			raise PlayerException("no style with initial '"+i+"'.")
			
	return playerList


#########################################################################
#Below function returns a player dictionary from a provided list of players.
#-----------------------------------------------------------------------	
def composition(players): 

	playerDic = {}
	
	for i in range(len(players)):
		if playerDic.get(players[i].style, 'ohno') != 'ohno':
			playerDic[players[i].style] += 1
			
		else:
			playerDic[players[i].style] = 1
			
	return playerDic


#########################################################################
#Below function runs a turn provided 2 players and updates their respective
#points and histories.
#-----------------------------------------------------------------------	
def run_turn(player_a, player_b):
	if id(player_a) == id(player_b):
		raise PlayerException('players must be distinct.')
		
	player_a.points -= 1
	player_b.points -= 1
	player_aMove = player_a.choose_move()
	player_bMove = player_b.choose_move()
	player_a.record_opponent_move(player_bMove)
	player_b.record_opponent_move(player_aMove)
	pointTally = turn_payouts(player_aMove, player_bMove)
	player_a.update_points(pointTally[0])
	player_b.update_points(pointTally[1])


#########################################################################
#Below function runs a game provided 2 players and a number of turns.
#-----------------------------------------------------------------------	
def run_game(player_a, player_b, num_turns=5):
	if id(player_a) == id(player_b):
		return
		
	player_a.reset_history()
	player_b.reset_history()
	
	for i in range(num_turns):
		run_turn(player_a,player_b)


#########################################################################
#Below function runs a tournament and returns a composition of the players
#that survived the number of rounds confirmed.
#-----------------------------------------------------------------------
def run_tournament(players, num_turns=10, num_rounds=5, \
	starting_points=0, num_replaces=5):
	
	#Loop for rounds played.
	for i in range(num_rounds):	

		#Loop for resetting players' points and setting them to the default.
		for j in range(len(players)):
			players[j].reset()
			players[j].points = starting_points
		
		#Loop for playing the games between all players, ensuring everyone
		#plays eachother once.
		for j in range(len(players)):
			totalPlayers = len(players)-1
			while j < totalPlayers:
				run_game(players[j], players[totalPlayers], num_turns)
				totalPlayers -= 1
		
		#Loop to remove low scoring players.
		for j in range(num_replaces):
			minPlayerIndex = 0
			for k in range(1,len(players)):
				if players[minPlayerIndex].points > players[k].points:
					minPlayerIndex = k
					
			players.pop(minPlayerIndex)
					
		counter = 0		
		
		#Loop iterates through list and removes all negative scoring players.
		while counter < len(players)-1:
			if players[counter].points < 0:
				players.pop(counter)
				
			else:
				counter += 1
				
		#Checks whether all players are out.
		if len(players) < 1:
			raise PlayerException('all players died after round' \
				+ str(i+1)+'.')
				
		#Loop iterates through top scoring players and makes a copy of them
		#and adds them to the players list.
		for j in range(num_replaces):

			maxPlayerIndex = 0
			for k in range(len(players)-1):
				if players[maxPlayerIndex].points < players[k+1].points:
					maxPlayerIndex = k+1
					
			players.append(players[maxPlayerIndex].copy_with_style())
		
	return composition(players)