"""
The following code performs a statistical analysis of augmented seconds 
in a dataset of machine-readable scores.

This script is part of the final project materials for the course "Computational Methods in
Ethnomusicology (Kunstuniversität Graz, 2020)"

Author: Noemi Silvestri (noemi.silvestri@student.kug.ac.at)
"""

from music21 import * # import all from music21

s = converter.parse("Score") # Give the path to the score you want to analyse.
s.show() # Verify if it is the correct score


p_instrument = s.parts[0] # This is used to separate the parts and attribute each of them to a separate variable for analysis.
nn_instrument = p_instrument.flat.notes.stream() # This saves all the notes from the given part into a stream.

#or

nn_melody = s.flat.notes.stream() # If the score does not have multiple parts, the above can be skipped and notes can be saved directly in a stream using this. 

print('The instrument part contains {} notes.'.format(len(nn_instrument))) # Check the total number of notes in a given part.
total_notes_Score = len(nn_part1) + len(nn_part2) # Calculate the total number of notes in the score
print(total_notes_Score) # Print the total number of notes in the score

def aug_sec(instrument_name, part, flag = 0):
    aug_second = 0 # Counter for augumented seconds
# Iteration over the indexes 
    for n in range(len(part)-1):
    # Current element
        n1 = part[n]
    # Next element
        n2 = part[n+1]
    # Creating the interval
        if n1.isNote and n2.isNote:
            intvl = interval.Interval(n1, n2)
    # Checking for augumented seconds
            if intvl.name == "A2":
     # Updating counter
                aug_second +=1   
        
# Print results
     if flag == 1:
    
        print("The {} part contains {} augumented seconds.".format(instrument_name, aug_second))
        total = len(part)
        percentage = aug_second / (total - 1) * 100 # 'total-1' because there are tot-1 numbers of melodic intervals in a part.
        print("- That is {:.2f}% of the total number of intervals.".format(percentage)) 
        
    return aug_second
"""
This function iterates over the indexes of the stream of notes and looks for augumented seconds between consecutive notes. Each time an augumented second is found, the aug_second counter is updated.

If the parameter flag is 1, it prints the results as indicated ("instrument_name" is used to adjust the name of the analysed part). If the flag is 0, as predifined, it returns the number of augmented seconds found in a given part. 
"""

aug_sec("instrument_name", nn_instrument, 1) # This calls the function for a given part.

def percentage_calculator(par1, par2):
    percentage_total_notes = par1 / (par2 - 1) * 100   # 'par2-1' because there are tot-1 numbers of melodic intervals in a score.
    print("That is {:.2f}% of the total number of intervals in the score.".format(percentage_total_notes))
    
"""
This function calculates the percentage of the total number of augmented seconds found in the entire score.

"""

total_total_0 = aug_sec("piano 1", nn_piano1) + aug_sec("piano 2", nn_piano2) # Calculate the total number of augmented seconds
print(total_total_0)
percentage_calculator(total_total_0, total_notes_Score) # This calls the function for a given score

