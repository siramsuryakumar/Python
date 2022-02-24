# -------------- defining the functions in python
def print_four():
    print("Sunny Vinny")
    print("Vinny Sunny")


# ------------ Calling the functions
print_four()


# -------------functions with parameters
def cube_number(num_var):
    print(num_var ** 3)


cube_number(5)


# ------------ functions with multiple parameters
def string_slice(string_var, start_pos, length_var):
    print(string_var[start_pos:start_pos+length_var-1])


string_slice("Vinny Sunny", 1, 5)


# ------------ functions with default parameter value
def default_parameter(num_var1=5, num_var2=5):
    print(num_var1 + num_var2)


default_parameter()
default_parameter(5, 10)
default_parameter(15)


# ------------- functions with return
def function_return(num_var3):
    return num_var3 ** 3


print(function_return(10))
example_var = function_return(100)
print("Cube value is :" + str(example_var))
