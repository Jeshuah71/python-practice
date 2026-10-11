# Data types 
print("Hello"[4]) # This is called Subscripting 
# we can count backwards 
print("Hello"[0])

# String 
print("123" + "345") # This is still concatenation 

# Integer = Whole numbers 
print(124 + 234 )

# Large integers 324_345_321
print(123_123_445)

# Float numbers are the ones that have decimal places that means decimal numbers
print(3.1415)

# Boolean 
print(True) 
print(False)

# Function is a machines that makes potatoes into chips 
len("Hello")

# type checks the datatype of something v
print(type(123))
print(type("Hello"))
print(type(True))
print(type(1.234))


# Convert the data type
print(int("123")+ int("456"))
int("123")
# Value error: Invalid literal for int() with base 10: 'abc' this is whenn we do int("abc")
int()
float()
str()
bool()

name_of_the_user = input("Enter your name") # This is a string
length_of_name = len(name_of_the_user) # this is a int 

print(type(length_of_name))
print(type(name_of_the_user))





# Exercise 
print("number of letters in your name: " +  str(length_of_name))


# Operations 

print("My age: " + str(12))
print(123 + 456)

print(7 - 3)
print(3 * 2)
print(6 / 3)
# python convert that to a flowating point 
print(6 // 3) # This is a class int. remove the decimal places 

print(2**3) # this is to calculate the power 

# take into account the priority 
# PEMDASLR Paranthesis, Exponents, Multiplication, Division, Addition and substraction
print(3 * 3 + 3 / 3 -3 )

# BMI calculation 
bmi = 84 / 1.65 ** 2 
print(bmi) 

# we have to convert the number into integer
print(int(bmi))

# Round the number
print(round(bmi))

print(round(bmi, 2))

# Number manipulation 

score = 0 

# user scores a point 
score += 1 
print(score)

# f-strings 
print("Your score is" + str(score))

# different way to handle data
score = 0
height = 1.8
is_winning = True
# F string insert different datatypes in one string 
print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

# Tip calculator project 
150 