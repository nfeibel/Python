#-------------------------------------------------------------------------------
# Name: Nick Feibel
# Project 3
# Due Date: 10/1/2019
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Class lectures
#-------------------------------------------------------------------------------
# Comments and assumptions: Thanks for grading this!
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------
###########################################################################

###########################################################################
#Below is a function to calculate how many times a number n can be divided
#until an even number is encountered.
def how_odd(n):

	counter = 0
	
	#Below is a while loop that continues until the first even is encountered
	while (n % 2) != 0:
		n = int(n/2)
		counter += 1
	
	#Once an even number is encountered, the counter is returned.
	return counter


###########################################################################
#Below is a function to calculate how many times a number n can be divided
#into a third, when odd, and then multiplied by 4/3, when even, until we reach the value 1.
def vibrate(n):

	counter = 0
	
	#Below is a while loop that continues until 1 is reached.
	while n != 1:
	
		#The below if statement confirms whether it is even or odd and
		#proceeds with the necessary calculations.
		if (n % 2) == 0:
			n = int(n *(4/3))+1
			
		else:
			n = int(n/3)
			
		counter += 1
		
	#Once 1 is reached, we return the counter.
	return counter


###########################################################################
#Below is a function to confirm whether the item name is combustible based
#on the provided combustibles list. True is returned if combustible, False
#if not.
def is_combustible(name, combustibles):

	#Below we verify whether the combustibles list is empty and if so,
	#confirm False.
	if len(combustibles) == 0:
		return False
		
	#Below we use a for loop to go over the combustibles list.
	for i in range(0,len(combustibles)):
	
		#The if statement below verifies whether the combustible at
		#index i is the name. True is returned if so.
		if combustibles[i] == name:
			return True
	
	#If True has not been returned by now, we can return False
	#since the combustibles list has been iterated through already.
	return False


###########################################################################
#Below is a function to confirm which combustible has ther largest size.
#The name is confirmed as a string.
def biggest_combustible(names, sizes, combustibles):

	largest_combustible = 0
	largest_index = 0
	
	#Below we iterate over the list of names to verify combustibility.
	for i in range(0, len(names)):
	
		#The if statement below is used to confirm whether we are over the max
		#index and if so, breaks the loop.
		if i >= len(names) or i >= len(sizes):
			break
			
		#If the index is not over max, we then compare the combustible at
		#index i with the largest combustible. If it is larger, we update
		#the index of the largest combustible and the index of the largest
		#combustible.
		elif is_combustible(names[i], combustibles):
			if largest_combustible < sizes[i]:
				largest_index = i
				largest_combustible = sizes[i]
	
	#If there was no combustible or no items in the list of combustibles or
	#names, we confirm None below. Else, we confirm the name of the largest
	#combustible.
	if largest_combustible == 0:
		return None
	
	else:
		return names[largest_index]


###########################################################################
#Below is a function to confirm whether any package is oversized in the list
#sizes compared to the maximum provided. If any are oversized, we confirm True
#and if not, we confirm False.
def any_oversized(sizes, maximum):

	#A for loop is used to iterate over the list of sizes.
	for i in range(0,len(sizes)):
	
		#The if statement below confirms whether the size at sizes index i
		#is larger than the maximum, and if so, returns True.
		if sizes[i] > maximum:
			return True
	
	#If a return has not been reached by this point, we know that none
	#of the sizes are over the maximum.
	return False


###########################################################################
#Below is a function to confirm whether there are 2 combustibles next to
#eachother in the list names. This is confirmed as either True, there
#are adjacent combustibles, or False, there are no adjacent ones.
def any_adjacent_combustibles(names, combustibles):

	#Below we iterate over the list of names, ensuring we minus 1 index
	#since we will be comparing the current name to the following name 
	#in the list.
	for i in range(0, len(names)-1):
	
		#Below we call our previously made function, is_combustible,
		#and if it returns True for both the current index and the next index
		#it returns True.
		if is_combustible(names[i], combustibles) and \
			is_combustible(names[i+1], combustibles):
			return True
			
	#If a return has not been reached by this point, we know that there are
	#no adjacent combustibles and return False.
	return False


###########################################################################
#Below is a function to provide a list of all combustibles in the list of
#names. A list is returned.
def get_combustibles(names, combustibles):

	combustiblelist = []
	
	#Below we iterate over the list of names.
	for i in range(len(names)):
	
		#Below we use the is_combustible function from earlier to verify
		#whether the name at index i is combustible and if so, we append
		#the name to the combustiblelist.
		if is_combustible(names[i], combustibles):
			combustiblelist.append(names[i])
			
	#Below we return the completed combustiblelist. If no names are
	#combustible this list is empty.
	return combustiblelist


###########################################################################
#Below is a function to provide a list of all items under the price limit.
def cheap_products(names, prices, limit):

	itemsUnder = []
	
	#Below we iterate over the list of names.
	for i in range(len(names)):
	
		#If a price is over less than or equal to the limit, we append
		#the name to the itemsUnder list.
		if prices[i] <= limit:
			itemsUnder.append(names[i])
			
	#Below we return the itemsUnder list. If no names are in the list
	#it is going to return an empty list.
	return itemsUnder


###########################################################################
#Below is a function to iterate over the names and sizes provided to package
#the various names based on their sizes. Any less than or equal to 2, it
#is in boxList's list at index 0, if larger than 2 but less than or equal
#to 5, it goes in boxList's list at index 1, if larger than 5 or less than
#or equal to 25, it goes in the list at index 2, and if larger than 25 but
#less than or equal to 50, it goes in the list at index 3. Any larger names
#are excluded.
def box_sort(names, sizes):

	#Below we initialize the boxList with the 0-3 index lists.
	boxList = [[],[],[],[]]
	
	#Below we iterate over the names and the if statement within
	#it sorts the names into boxList based on their respective
	#sizes.
	for i in range(len(names)):
		if sizes[i] <= 2:
			boxList[0].append(names[i])
		elif sizes[i] <= 5:
			boxList[1].append(names[i])
		elif sizes[i] <= 25:
			boxList[2].append(names[i])
		elif sizes[i] <= 50:
			boxList[3].append(names[i])
			
	#Once we have iterated over all the names, we return the boxList.
	return boxList


###########################################################################
#Below is a function to iterate over the names and sizes provided to package
#the various names based on their sizes and the box_size allowed. We add
#the respective names until their sizes add up to box_size. We cannot exceed
#box_size, so if it does, we need to start a new box. If any name's respective
#size is larger than box_size, we immediately put it at the current position
#of the boxList with a * in front of it. Then we continue setting up the
#box we had been working on.
def packing_list(names, sizes, box_size):

	#Below we initialize the boxList we will be returning.
	#The packedBox is initialized as well which simply is the box
	#actively being packed. We also initialize the currentValue
	#of the boxes and the boxNumber which is the index of boxList
	#we are currently on.
	boxList = []
	packedBox = []
	currentValue = 0
	boxNumber = 0
	
	#Below we iterate over the list of names provided.
	for i in range(len(names)):
	
		#Below is an if statement to verify whether the current
		#box can be packed with the current size we are on. If not
		#it checks whether the size is larger than the box_size allowed.
		#If neither of those are triggered, we know that the size is within
		#the limit and would overflow. If the current size can be added,
		#we append the packedBox list with the respective name of the size.
		#If the size is larger than the allowed, we append the boxList
		#with the name of the oversize item with a * before it, then 
		#we move onto the next boxNumber. If the packedBox is going to
		#overflow, we append the packedBox to the boxList and move onto
		#the next box.
		if (sizes[i] + currentValue <= box_size):
			packedBox.append(names[i])
			currentValue = sizes[i] + currentValue
		elif (sizes[i] > box_size):
			boxList.append(['*' + names[i]])
			boxNumber += 1
		else:
			boxList.append(packedBox)
			boxNumber += 1
			packedBox = [names[i]]
			currentValue = sizes[i]
			
	#Below we check whether the packedBox has values in it, and if so
	#append it to the boxList.
	if len(packedBox) > 0:
			boxList.append(packedBox)
	
	#Below we return the fully formed boxList.
	return boxList