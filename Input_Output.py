
user_input = input("Please enter an integer: ")
print("You entered " + user_input)
print("Twice that number is " + str(2*int(user_input)))


"""
user_input = input("Please enter an integer: ")

print("You entered " + user_input)

print("Twice that number is " + str(2*int(user_input)))

 First line uses the input function to print "please enter an integer" 
 and then assigns the input into a variable called user_input. You 
 should keep in mind that user_input is a string now. Second line 
 concatenates "you entered " with user_input and then prints it. In 
 the third line, user_input is converted to an integer first, because we 
 can't multiply strings with numbers, then it is multiplied by 2 and converted 
 back to a string, because we need to concatenate it with the string "twice that
 number is ".
"""
