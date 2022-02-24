# ---------------------------- int() & float() functions
num_var = input("1.\tEnter your favourite number\n")
print(type(num_var))
num_var = int(input("1.\tEnter your favourite number\n"))
print(type(num_var))
# num_var = int("10.1") ------------- error
num_var = int(10.5)    # -- Maps to Nearest integer
print(num_var)

# --------------------- float (Even user enter integer, that will convert into float type
float_var = float(input("2.\t Enter the favourite float number\n"))
print(type(float_var))

# --------------------------

