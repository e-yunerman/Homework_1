#python exceptions let you deal with unexpected results

try:			#it will try to whatever is in the try function
	print(a)	#this will throw an exception since a is not defined
except:
	print("a is not defined!")
	
#there are specific errors to help with cases
try:
	print(a)	#again, since a is not defined it will throw an exception
except NameError:
	print("a is stil not defined!")
except:
	print("Something else went wrong.")
	
#printing a will break our program since a is not defined
print(a)