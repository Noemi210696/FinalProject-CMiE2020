"""
This code can be used to create a plot for categorical variables.
"""

import matplotlib.pyplot as plt 

data = {"Score1" : 4, "Score2": 5, "Score3" :0, "Score" : 7} # Assign each score the number of augmented seconds found in it.  
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(figsize=(8, 3)) # Create the plot and adjust the size of the figure as you prefer
axs.bar(names, values)
axs.bar(names, values, color="grey") # Adjust the color of the bars
plt.ylabel("Number of A2") # Define the label for the y axis
plt.ylim(top=80) # Set the top limit of the y axis
plt.xlabel("Parts") # Define the label for the x axis
fig.suptitle('Augmented Seconds', size = 14) # Define the title of the plot