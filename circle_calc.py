"""

Purpose: Calculate the area of a circle.

Author: Denise Case

This script illustrates importing modules and using constants.

It illustrates the built-in function round().

When we install Python, it comes with the Python standard library.
Nearly all scripts will import at least one module from the standard library.

We can install additional, third-party modules using pip.
We'll do that later. 

All scripts in this repository use only the standard library.

@uses math module for pi constant

"""
import math  

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# Use the math module's constant for pi
pi = math.pi

# get the radius from the user - input result is always a string
# Use \n to add a blank new line to the terminal before we ask for input
radius_string = input("\nEnter the radius of a circle: ")

# convert the radius_string to a number
radius = float(radius_string)

# calculate the area using the numeric value (not the string)
area = pi * radius**2

# log the results
logger.info(f"The area of a circle with radius {radius} is {area}.")
logger.info("Eww... that's a lot of decimal places - tmi!")


# round the area to two decimal places
area = round(area, 2)

# log the results
logger.info(f"The area of a circle with radius {radius} is {area}.")
logger.info("Much better!")


# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())

string1 = input(5)

string2 = input(10)

string3 = input(15)

# Assuming these are your three values
a = 5
b = 10
c = 15

# Calculate the needed values
_sum = a + b + c
_average = _sum / 3
_product = a * b * c
_minimum = min(a, b, c)
_maximum = max(a, b, c)

# Print the results using f-strings
print(f"The sum of the values is {_sum}")
print(f"The average of the values is {_average}")
print(f"The product of the values is {_product}")
print(f"The smallest value is {_minimum}")
print(f"The largest value is {_maximum}")

In [7]: # Assuming these are your three values
   ...: a = 5
   ...: b = 10
   ...: c = 15
   ...:
   ...: # Calculate the needed values
   ...: _sum = a + b + c
   ...: _average = _sum / 3
   ...: _product = a * b * c
   ...: _minimum = min(a, b, c)
   ...: _maximum = max(a, b, c)
   ...:
   ...: # Print the results using f-strings
   ...: print(f"The sum of the values is {_sum}")
   ...: print(f"The average of the values is {_average}")
   ...: print(f"The product of the values is {_product}")
   ...: print(f"The smallest value is {_minimum}")
   ...: print(f"The largest value is {_maximum}")
The sum of the values is 60
The average of the values is 20.0
The product of the values is 6000
The smallest value is 10
The largest value is 30

In [8]: import logging
   ...:
   ...: # Assuming these are your three values
   ...: a = 10
   ...: b = 20
   ...: c = 30
   ...:
   ...: # Calculate the needed values
   ...: _sum = a + b + c
   ...: _average = _sum / 3
   ...: _product = a * b * c
   ...: _minimum = min(a, b, c)
   ...: _maximum = max(a, b, c)
   ...:
   ...: # Set up basic logging (to the console, with level INFO)
   ...: logging.basicConfig(level=logging.INFO)
   ...:
   ...: # Log the results
   ...: logging.info(f"The sum of the values is {_sum}")
   ...: logging.info(f"The average of the values is {_average}")
   ...: logging.info(f"The product of the values is {_product}")
   ...: logging.info(f"The smallest value is {_minimum}")
   ...: logging.info(f"The largest value is {_maximum}")
INFO:root:The sum of the values is 60
INFO:root:The average of the values is 20.0
INFO:root:The product of the values is 6000
INFO:root:The smallest value is 10
INFO:root:The largest value is 30

