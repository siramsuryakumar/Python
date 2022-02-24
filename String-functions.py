# -------------------------------String operations
exp_var = "Hello Surya World"
exp_1 = 'Hello Surya World'
exp_2 = "Vinny Sunny"
# --------------------------- String index starts from 0 to length of the string-1
print(exp_2[2])
print(exp_2[0])
print(exp_var[10])
# --------------------------- String slicing
print(exp_2[:3])
print(exp_2[2:])
print(exp_2[2:7])
# ---------------------------- String concatenation
print("Vinny" + " " + "Sunny")
# --------------------------- Concatenate integer and String (str())
print("Sunny = " + str(100) + " " + "Vinny = " + str(100))
# ----------------------------- type() function
exp_3 = 2.333
exp_4 = "Vinny Sunny"
exp_5 = 12
exp_6 = True
print(type(exp_3))
print(type(exp_4))
print(type(exp_5))
print(type(exp_6))
# --------------------------------- Escape sequence commonly used
print("Sunny\tVinny")   # Tab
print("Sunny\nVinny")   # new line
print("Vinny is \'Important\' to Sunny")  # for '\ and "\
print("Vinny Sunny \\")   # for \
# --------------------------------- Challenge for Asterisk Triangle
print("*******\n *****\n  ***\n   *")
# -------------------------------- input() function to getdata from user
exp_var = input("Enter your buddy name\n")
print("Your buddy name is " + exp_var)
print(type(exp_var))
# -------------------------------- Even if the user enter the integer or float value, system converts into string only
exp_num = input("Enter your favourite number \n")
print("Your favourite number is " + exp_num)
print(type(exp_num))

