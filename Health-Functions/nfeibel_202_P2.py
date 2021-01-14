#-------------------------------------------------------------------------------
# Name: Nick Feibel
# Project 2
# Due Date: 9/18/2019
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
##########################################################################



#The function below returns the risk level times the mean arterial pressure
#with the systolic and diastolic variables provided as ints.
def blood_pressure(systolic, diastolic):

	#Below we ensure the values are converted to int.
	systolic = int(systolic)
	diastolic = int(diastolic)
	
	#Below is the calculation of mean arterial pressure using 
	#the values of systolic and diastolic pressure.
	meanPressure = float((systolic + (2 * diastolic)) / 3)
	
	#We then use the above formula to determine the risk value
	#starting with the highest risk scenario. We then confirm
	#the mean arterial pressure.
	if (systolic > 180) or (diastolic > 120):
		risk = 1.4
		return round(risk * meanPressure, 2)
	
	elif (140 <= systolic) or (90 <= diastolic):
		risk = 1.3
		return round(risk * meanPressure, 2)
	
	elif (130 <= systolic) or (80 <= diastolic):
		risk = 1.2
		return round(risk * meanPressure, 2)
		
	elif (120 <= systolic) and (diastolic < 80):
		risk = 1.1
		return round(risk * meanPressure, 2)

	else:
		risk = 1.0
		return round(risk * meanPressure, 2)


###########################################################################
#Below is a function to calculate the BMI for a person based on their weight
#and height as a float rounded to 2 decimals. Since this is 
#calculated using Kilos, we need to check if the 
#ISU (International System of Units) is not used (set to False),
#and if it is False, we convert to ISU.
def standard_BMI(weight, height, ISU):

	#Below we check whether ISU is met, and if so, we just need
	#to convert weight/height to floats to ensure calculation is 
	#done correctly. If not, we convert to ISU.
	if ISU == True:
		weight = float(weight)
		height = float(height)
		
	else:
		weight = float(weight / 35)
		height = float(height * .025)
		
	#Once we know we have the correct ISU values, we can
	#return the BMI as a float rounded to 2 decimals.
	return round(float(weight/(height ** 2)), 2)
	
	

#Below is a function to confirm whether someone is underweight, normal weight,
#overweight, or obese by using the weight, heigh, age, and gender of a person.
#The confirmation is provided as a String. This function calls the standard_BMI
#function to confirm whether they are underweight, normal weight, overweight,
#or obese.
def BMI_chart(weight, height, age, gender):

	#Below we ensure the weight, height, and age are converted to the proper
	#value types.
	weight = int(weight)
	height = float(height)
	age = int(age)
	
	#Below we check whether the person is 18 or over as male and female adults
	#have the same BMI chart values/categories. We can then confirm their
	#category based on their scenarios. If they are not an adult, they are a
	#child and we check whether they are a male or female child, and determine
	#the BMI chart category based on the male/female child scenarios.
	if age >= 18:		
		if standard_BMI(weight, height, True) < 18.5:
			return 'underweight'
				
		elif standard_BMI(weight, height, True) <= 25:
			return 'normal'
				
		elif standard_BMI(weight, height, True) <= 30:
			return 'overweight'
				
		else:
			return 'obese'	
	
	else:		
		if(gender == 'male'):
			if standard_BMI(weight, height, True) < 14:
				return 'underweight'
			
			elif standard_BMI(weight, height, True) <= 19:
				return 'normal'
			
			elif standard_BMI(weight, height, True) <= 22:
				return 'overweight'
				
			else:
				return 'obese'
				
		else:
			if standard_BMI(weight, height, True) < 15:
				return 'underweight'
				
			elif standard_BMI(weight, height, True) <= 20:
				return 'normal'
				
			elif standard_BMI(weight, height, True) <= 23:
				return 'overweight'
				
			else:
				return 'obese'		


################################################################
#The function below is used to confirm whether a person's HCT
#is normal or not. If normal, we return the boolean True, and if
#not we return the boolean False. This function uses red cell count,
#total cell count, age, and gender. Red cell count is in int,
#total cells count in int, and age in int. Gender is a string.
def HCT(red_cells, total_cells, age, gender):

	#Below we calculate the volume percentage by dividing the red cell count
	#by the total cell count. We then multiply this by 100 to ensure we 
	#have a percentage
	volumePercentage = (red_cells/total_cells) * 100
	
	#Below we check whether they are 18 or older. If they are
	#we branch down to check whether they are male or female
	#and then confirm whether their HCT is normal or not. If a child
	#we confirm based on their restrictions.
	if age >= 18:
		if gender == 'male':
			if 40.7 < volumePercentage < 50.3:
				return True
				
			else:
				return False
				
		else:
			if 36.1 < volumePercentage < 44.3:
				return True
			
			else:
				return False
			
	else:
		if 36 < volumePercentage < 40:
			return True
			
		else:
			return False
			

#########################################################################
#The function below is used to confirm the risk of cardiovascular disease
#for someone. The provided info is total cholesterol (total) as an int, 
#HDL which is good colesterol as an int, the number of triglycerides 
#(trig) as a float, age as an int, and gender as a string. Risk is provided
#as a number 0 to 5.
def LDL(total, HDL, trig, age, gender):

	#Below we calculate the k by using an if-elif-else statement using
	#the conditions specified.
	if ((11.3 <= trig <= 43.5)):
		k = .2
	
	elif ((total > 250) and (trig > 43.5)):
		k = 0.19 - (((total - 250)//10) * .01)
		
	else:
		k = 0
	
	#Below we use the k value calculated in the previous if-elif-else 
	#statement to calculate the LDL.
	lowDL = float((total - HDL) - (k * trig))
	
	#Below we then check whether they are over 18, and if not, check whether
	#they are a male or female child. Then depending on this we confirm the
	#risk level they have based on the confirmed conditions and calculations.
	if age < 18:
		if lowDL < 100:
			return 0
			
		else:
			risk = ((lowDL - 100)//15) + 1
			if risk > 5:
				return 5
				
			else:
				return risk
	
	else:
		if (gender == 'male' and 70 >= HDL >= 40) or \
		(gender == 'female' and 70 >= HDL >= 50):
			if lowDL < 120:
				return 0
				
			else: 
				risk = ((lowDL - 120)//20) + 1				
				if risk > 5:
					return 5
					
				else:
					return risk
				
		elif ((HDL < 40) and (gender == 'male')) or \
		((HDL < 50) and (gender == 'female')):
			if lowDL < 120:
				return 1
				
			else: 
				risk = ((lowDL - 120)//20) + 1
				if risk > 5:
					return 5
					
				else:
					return risk + 1
					
		else:
			if lowDL < 120:
				return 0
				
			else: 
				risk = ((lowDL - 120)//20) + 1
				if risk > 5:
					return 5

				else:
					return risk - 1
		
