# pcinput
# input functions that check for type
# Pieter Spronck

# These functions are rather ugly as they print error messages if something is wrong.
# However, they are meant for a course, which means they are used by students who
# are unaware (until the end of the course) of exceptions and things like that.

# This function asks for a floating-point number. You may use it for the exercises.
# The parameter is a prompt that is displayed when the number is asked.
# The function uses an exception to check whether the input is actually
# a floating-point number. We will discuss exceptions in the future, just use the
# function as is for now.
# To use the function, write something like:
#   myNumber = rsdpu.getFloat( "Give me a number> " )
# This will then ask the user of the program for a floating-point number, and will store
# whatever the user entered in myNumber. It will also make sure that actually
# a floating-point number or an integer is entered; if the user enters anything else,
# an error message is displayed and the user has to enter something else.
def getFloat( prompt ):
	while True:
		try:
			num = float( input( prompt ) )
		except ValueError:
			print( "That is not a number -- please try again" )
			continue
		return num

# Similar for getting integers.
def getInteger( prompt ):
	while True:
		try:
			num = int( input( prompt ) )
		except ValueError:
			print( "That is not an integer -- please try again" )
			continue
		return num

# And for strings (leading and trailing spaces are removed)
def getString( prompt ):
	line = input( prompt )
	return line.strip()

# And for getting one upper-case letter
def getLetter( prompt ):
	while True:
		line = input( prompt )
		line = line.strip()
		line = line.upper()
		if len( line ) != 1:
			print( "Please enter exactly one character" )
			continue
		if line < 'A' or line > 'Z':
			print( "Please enter a letter from the alphabet" )
			continue
		return line
