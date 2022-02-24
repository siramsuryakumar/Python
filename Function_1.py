# ------------ exercise
def hello_world_printer():
    print("Hello Surya World")


hello_world_printer()


# --------------- exercise 2
def name_printer(name_var):
    print("Your name is : " +name_var)


name = input("Enter your name : \n")
name_printer(name)


# --------------- exercise 3
def volume_rectangular_prism(length_var, width_var, height_var):
    print("The volume of the rectangular prism is : " + str(length_var*width_var*height_var))


length = int(input("Enter the length of the rectangular prism: \t"))
width = int(input("Enter the width of the rectangular prism: \t"))
height = int(input("Enter the height of the rectangular prism: \t"))
volume_rectangular_prism(length, width, height)


