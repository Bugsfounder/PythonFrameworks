# 15. Write a Python program to create a horizontal bar chart with differently ordered colors. 
# Note: Use bottom to stack the women?s bars on top of the men?s bars.
# Sample Data Set:
# languages = [['Language','Science','Math'],
# ['Science','Math','Language'],
# ['Math','Language','Science']]
# numbers = [{'Language':75, 'Science':88, 'Math':96},
# {'Language':71, 'Science':95, 'Math':92},
# {'Language':75, 'Science':90, 'Math':89}]

import numpy as np
from matplotlib import pyplot as plt

num_set = [{'Language':75, 'Science':88, 'Math':96},
           {'Language':71, 'Science':95, 'Math':92},
           {'Language':75, 'Science':90, 'Math':89}]

lan_guage    = [['Language','Science','Math'], 
               ['Science','Math','Language'], 
               ['Math','Language','Science']] 

# Solve the Question : TODO
