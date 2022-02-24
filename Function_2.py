# ------------------------Challenge: Celsius to Fahrenheit
def fahrenheit(celsius):
    return 1.8 * celsius + 32


celsius_temp = int(input("Enter the Celsius temperature : \t"))
fahrenheit_temp = fahrenheit(celsius_temp)
print("The Fahrenheit equivalent of " + str(celsius_temp) + " degrees Celsius is " + str(fahrenheit_temp))
print("The Fahrenheit equivalent of " + str(celsius_temp) + " degrees Celsius is rounded to " + str(round(fahrenheit_temp)))

# --------------------------Celsius to Fahrenheit Solution with round()
