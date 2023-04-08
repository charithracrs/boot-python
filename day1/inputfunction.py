# to take input from the user user sytax "input"

#looks similar to the print function
input("What is your name? ")
# finishes without storing the input

# to print the input
print("Hello " + input("What is your name? ") +"!")

# OR
print("What is your name? ")
name = input()
print("Hello "+name+"!")

# to get the input into a variable
# variable is input_value_1
input_value_1 = input("What is your name? ")
print(input_value_1)

data = 1234
# to attach input value to a string - Format printing
print("Hello "+input_value_1+"!")
print("hello" + data)
print(f"Hello {input_value_1} , {data}!")
print("Hello {} {}!".format(input_value_1, data))
print("Hello {name} - {data}!".format(data=data, name=input_value_1))

# # Tips:
# # Use comments for line of code to describe their implementation
# # Shortcut: Place the cursor on the line or select the line/s
# # on Windows use ctrl+/
# # on Mac use cmd+/

# Excercise print the length of a string
# Use "len()" in-built function

print(f"Length of the name is : { len(    input_value_1   )}"   )

# str type-casting
print("Length of the name is (tc):" + str(len(input_value_1))   )



# Changing the input variable to new piece of data
input_value_1 = "Sammy"
print("Changed variable name is : "+input_value_1)

# Write a program to swtich values stored in variable a and b
a = 18
b = 7
# #Sol
# # c = a
# # a = b
# # b = c

# # Note: Naming variables
# #     1. sensible variable names
# #     2. should be one single unit, use "_" to provide space ("variable_one")
# #     3. shouldn't use in-built function/method names for user defined names (like: print, input, etc)
# #     4. If undeclared variable are used throws "NameError"
