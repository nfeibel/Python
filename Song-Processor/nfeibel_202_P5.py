#-------------------------------------------------------------------------------
# Name: Nick Feibel
# Project 5
# Due Date: 10/31/2019
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Class lectures
#-------------------------------------------------------------------------------
# Comments and assumptions: Nick Feibel, nfeibel, G01164484, CS-112-202, no
# collaboration partners. Thanks for grading this!
# What I found most useful was using the Python Visualizer with the test
# cases provided in the instructions.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------
##########################################################################


#########################################################################
#Below function creates a dictionary of note durations. A base_tempo
#is provided.
#-----------------------------------------------------------------------
def generate_durations(base_tempo):
	
	#The multiplier is determined and then the dictionary is returned.
	multiplier = 60/base_tempo
	return {'Whole': 4 * multiplier, 'Half': 2 * multiplier, 'Quarter': \
	1 * multiplier, 'Eighth': 0.5 * multiplier, 'Sixteenth': 0.25*multiplier}


#########################################################################
#Below function creates a dictionary of frequency values provided a 
#base_freq.
#-----------------------------------------------------------------------	
def generate_frequencies(base_freq):

	#Frequency keys are initialized as well as the dictionary
	#that will be returned at the end.
	frequency = {'C': -9,'C#':-8,'D':-7,'D#':-6,'E':-5,'F':-4,'F#':-3,\
	'G':-2,'G#':-1,'A':0,'A#':1,'B':2}
	newDict = {}
	
	#Loop iterates through and determines the frequency for the octave's 
	#notes, octave by octave and adds the value to 
	for i in range(-3,4):
		for letter, value in frequency.items():
			newDict[letter + str(i+4)] = base_freq * (2**((value+(i*12))/12))
	
	#The straggler notes we then assign their values outside a loop.
	newDict['A0'] = base_freq * (2**((0+(-4*12))/12))
	newDict['A#0'] = base_freq * (2**((1+(-4*12))/12))
	newDict['B0'] = base_freq * (2**((2+(-4*12))/12))
	newDict['C8'] = base_freq * (2**((-9+(4*12))/12))
	
	return newDict


#########################################################################
#Below function finds either the highest or lowest note in a song
#provided as filename.
#-----------------------------------------------------------------------
def find_note(filename, highest_or_lowest):

	#Below I open the file, copy the contents to a string and then
	#split that string into a listOfLines. The notes list is initiated
	#and the notes from the listOfLines are added to the notes list
	#to keep track of all the notes.
	fileObject = open(filename)
	fileContents = fileObject.read()
	fileObject.close()
	listOfLines = fileContents.split("\n")
	listOfLines[:] = listOfLines[2:-1]
	notes = []
	for i in range(len(listOfLines)):
		notes.append(listOfLines[i].split(",")[0])
	
	#Below a simple if-else statement is used to verify whether highest or
	#lowest should be found.
	if highest_or_lowest == True:
	
		#The first note is initialized as the highest and it's octave
		#is saved as well. I use a function I made called letterValue
		#to confirm a numerical value for the note in an octave (0-11).
		#This is called to confirm the current highestLetter value.
		currentHighest = notes[0]
		highestNumber = currentHighest[-1]
		highestLetter = letterValue(currentHighest[0])
		
		#A loop is used to iterate through the notes list and find the
		#absolute highest note in the list. If-elif-else statement 
		#used to first check the octave, then check the letterValue.
		for i in range(len(notes)):
			if highestNumber < notes[i][-1]:
				currentHighest = notes[i]
				highestNumber = currentHighest[-1]
				highestLetter = letterValue(currentHighest[0])
				
			elif highestNumber > notes[i][-1]:
				continue
				
			else:
				if highestLetter < letterValue(notes[i][0]):
					currentHighest = notes[i]
					highestNumber = currentHighest[-1]
					highestLetter = letterValue(currentHighest[0])
					
		return currentHighest
		
	else:
	
		#Same process as above except for the lowest note.
		currentLowest = notes[0]
		lowestNumber = currentLowest[-1]
		lowestLetter = letterValue(currentLowest[0])
		
		for i in range(len(notes)):
			if lowestNumber > notes[i][-1]:
				currentLowest = notes[i]
				lowestNumber = currentLowest[-1]
				lowestLetter = letterValue(currentLowest[0])
				
			elif lowestNumber < notes[i][-1]:
				continue
				
			else:
				if lowestLetter > letterValue(notes[i][0]):
					currentLowest = notes[i]
					lowestNumber = currentLowest[-1]
					lowestLetter = letterValue(currentLowest[0])
					
		return currentLowest
	
	#return None statement included just incase.
	return None


#########################################################################
#Below function creates a random_song provided a filename, tempo,
#tuning, and num_measures.
#-----------------------------------------------------------------------	
def random_song(filename, tempo, tuning, num_measures):

	#Random module of course is used for this so it is imported at the start.
	import random
	
	#File we are writing to is opened. Durations dictionary is defined
	#and the tempo and tuning are written to the file at the start.
	fileObject = open(filename, 'w')
	durations = {'Whole': 4, 'Half': 2, 'Quarter': \
	1, 'Eighth': 0.5, 'Sixteenth': 0.25}
	fileObject.write(str(tempo) + '\n')
	fileObject.write(str(tuning) + '\n')
	
	#Below a loop iterates through the number of measures with the beats
	#initialized as 4 at the start of every loop. Then a while loop is used
	#to continue adding beats until the measure is filled. A string is
	#made by using random.choice and random.randint and then the string is
	#written to the file. If a duration chosen is too long for the beats left
	#the loop continues so it continues until one that fits is selected.
	for i in range(num_measures):
		beats = 4
		while beats > 0:
			currentType = random.choice(["Sixteenth", "Eighth", 'Quarter', \
			'Half','Whole'])
			if beats < durations[currentType]:
				continue
				
			currentString = random.choice(["C","C#","D","D#","E","F","F#",\
			"G","G#","A","A#","B"])+str(random.randint(1,7))			
			fileObject.write(currentString+","+currentType+"\n")
			beats = beats - durations[currentType]
	
	#Once the file has been completed, it is closed and we return None.
	fileObject.close()
	return None


#########################################################################
#Below function changes all the notes in a filename based on the confirmed
#dictionary of changes and the confirmed shift. New file is confirmed
#with the same name simply _changed is added to it.
#-----------------------------------------------------------------------
def change_notes(filename, changes, shift):

	#The file is opened and contents copied and split into a list
	#as lines. Then the file we are writing to is setup. 
	fileObject = open(filename)
	fileContents = fileObject.read()
	fileObject.close()
	splitFile = fileContents.split('\n')
	splitName = filename.split('.')
	fileObject2 = open(splitName[0]+"_changed."+splitName[1], 'w')
	
	#The last line is checked whether it is an empty space and if it is
	#it is removed.
	if splitFile[-1] == '':
		splitFile.pop(-1)
	
	#The tempo and tuning are added at the start to the output list.
	output = [splitFile.pop(0)]
	output.append(splitFile.pop(0))
	
	#We then confirm the letterShift and octaveShift based on whether
	#it is greater than or less than +-11.
	if (shift > 11) or (shift < -11):		
		if shift < 0:
			letterShift = (shift % -12)
			octaveShift = (shift // -12)*-1
		else:
			letterShift = shift % 12
			octaveShift = shift // 12
	else:
		octaveShift = 0
		letterShift = shift
	
	#A loop is then used to iterate through the splitFile line by line
	#and make the confirmed changes.
	for i in range(len(splitFile)):
		currentLine = splitFile[i].split(',')
		
		#First we instantly check whether the note is in the changes
		#dictionary and if so we make the change and continue.
		if changes.get(currentLine[0], 'ohno') != 'ohno':
			output.append(changes[currentLine[0]]+','+currentLine[1])
			continue
		
		#Then there is an if-else statement to check whether the shift
		#is positive or negative.
		if shift < 0:
		
			#Shift positive confirmed and the line's octave and 
			#value are initialized.
			octave = currentLine[0][-1:]
			value = letterValue(currentLine[0][:-1])

			#If-else statement checks whether the shift is going
			#to cause the note to go out of bounds, and if that
			#is the case, assigns the output as the current note
			#rather than shifting.
			if ((((value + letterShift < 0) and \
			(((int(octave)+octaveShift-1) < 0) or ((value <9)  and \
			((int(octave)+octaveShift-1) == 0)))) or \
			(octaveShift + int(octave) < 0)) or \
			((int(octave)+octaveShift) <= 0 and value + letterShift < 9))\
			and not ((octaveShift + int(octave) -1 == 0) and \
			12+(value + letterShift) >= 9):
				output.append(currentLine[0]+','+currentLine[1])
				
			else:
				
				#If the shift is not going to be too much, an if-else
				#statement is used to check whether the shift is going
				#to cause the note to go to another octave and if so,
				#it assigns the new octave value. If not, it simply
				#assigns the new note with the current octave.
				if value + letterShift < 0:
					output.append(valueLetter(12 + (value+letterShift))+\
					str(int(octave)+octaveShift-1)+','+currentLine[1])
					
				else:
					output.append(valueLetter(value+letterShift)+\
					str(int(octave)+octaveShift)+','+currentLine[1])
					
		else:
		
			#The same is done for shifting in the positive direction.
			octave = currentLine[0][-1:]
			value = letterValue(currentLine[0][:-1])
			
			if (((value + letterShift > 12) and \
			(((int(octave)+octaveShift+1) > 8) or \
			(((int(octave)+octaveShift+1) == 8))) \
			or (octaveShift + int(octave)) > 8)) \
			or ((int(octave)+octaveShift) == 8 and value + letterShift > 0):
				output.append(currentLine[0]+','+currentLine[1])
				
			else:
				if value + letterShift > 11:
					output.append(valueLetter((value+letterShift)-12)+\
					str(int(octave)+octaveShift+1)+','+currentLine[1])
					
				else:
					output.append(valueLetter(value+letterShift)+\
					str(int(octave)+octaveShift)+','+currentLine[1])
	
	#Once the output list is complete, it is written to the new file.
	for i in range(len(output)):
		fileObject2.write(output[i]+'\n')
	
	#File is closed and None is returned.
	fileObject2.close()
	return None


#########################################################################
#Below function makes a dictionary of the tempo, tuning, types, and
#notes in a confirmed file, filename.
#-----------------------------------------------------------------------
def song_as_dict(filename):	

	#The file is opened and contents copied and split into a list as lines.
	fileObject = open(filename)
	fileContents = fileObject.read()
	fileObject.close()
	splitFile = fileContents.split('\n')
	splitName = filename.split('.')
	
	#We check if the last line is an empty space and if that is the case,
	#we remove it.
	if splitFile[-1] == '':
		splitFile.pop(-1)
	
	#The tempo and tuning are confirmed and the types and 
	#notes are initialized.
	output = {'tempo': int(splitFile.pop(0))}
	output['tuning'] = float(splitFile.pop(0))
	output['types'] = {}
	output['notes'] = {}
	
	#A loop goes through the splitFile and adds the note and type line by
	#line.
	for i in range(len(splitFile)):
		
		#The currentLine is split into note and type.
		currentLine = splitFile[i].split(',')
		
		#If-else statement checks whether a note has been added previously,
		#and if not, it initializes that dictionary for the note.
		if output['notes'].get(currentLine[0][:-1], 'ohno') == 'ohno':
			output['notes'][currentLine[0][:-1]] = \
			{int(currentLine[0][-1:]): 1}
			
		else:
			
			#If a note has been found in the dictionary, we check whether the
			#octave is in the dictionary for the note already, and if not
			#it initializes it.
			if output['notes'][currentLine[0][:-1]].get(\
			int(currentLine[0][-1:]), 'ohno') == 'ohno':
				output['notes'][currentLine[0][:-1]][int(\
				currentLine[0][-1:])] = 1
				
			else:
			
				#If the octave is already in the dictionary, we simply iterate
				#the counter for it.
				output['notes'][currentLine[0][:-1]][int(\
				currentLine[0][-1:])] += 1
		
		#Then we check whether a type has been added previously,
		#and if not, it initializes that dictionary for the type.
		if output['types'].get(currentLine[1].strip(), 'ohno') == 'ohno':
			output['types'][currentLine[1].strip()] = 1
			
		else:
			
			#If the type is already in the dictionary, we simply iterate
			#the counter for it.
			output['types'][currentLine[1].strip()] += 1
	
	#The output dictionary is returned.
	return output

#########################################################################
#Below function provides a value for a provided letter. Value is 0 - 11
#0 being C, the bottom of the scale, and 11 being B, the top of the scale.
#-----------------------------------------------------------------------	
def letterValue(letter):

	frequency = {'C': 0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,\
	'A':9,'A#':10,'B':11}
	return frequency[letter]

#########################################################################
#Below function provides a letter for a provided value. Value is 0 - 11
#0 being C, the bottom of the scale, and 11 being B, the top of the scale.
#-----------------------------------------------------------------------	
def valueLetter(randomValue):
	
	frequency = {0: 'C',1: 'C#',2: 'D',3:'D#',4:'E',5:'F',6:'F#',7:'G',\
	8:'G#',9:'A',10:'A#',11:'B'}
	return frequency[randomValue]