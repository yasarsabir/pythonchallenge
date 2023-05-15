#import dependencies
import os
import csv
import pandas as pd

#assign file to read
csvpath = os.path.join('Resources', 'election_data.csv')

#set variables
count = 0
candidate_list = []
Votes_for_Charles = 0
Votes_for_Diana = 0
Votes_for_Raymon = 0

#open the file and read the data
with open(csvpath) as text: 
    data = csv.reader(text, delimiter=",")

#discard header
    header = next(data)
    first_row = next(data)

#1) COUNT the total number of votes, ie the number of rows in column 1 
    for row in data:
        count  += 1

# 2) Retrieve the names of all the candidates and add them to the empty candidate list
        data_column = row[2]
# Iterate over each item in the data column
    # Check if the item is not already in the candidate_list
        if data_column not in candidate_list:
        # Add the item to the candidate_list
            candidate_list.append(data_column)

        # Print the unique candidate strings to check how how many candidates they are- 
        # THIS PART OF THE CODE TAKES AGES TO SORT THROUGH 30,000 peices of data!
        #could have used len here
        print(candidate_list)

   #3) Retrieve each unique candidate from the candidate list, and count the number of votes for each
        if row[2] == candidate_list[0]:
                Votes_for_Charles  += 1
        elif row[2] == candidate_list[1]:
                Votes_for_Diana    += 1
        elif row[2] == candidate_list[2]:
                Votes_for_Raymon   += 1
                 
#4) Calculate the percentage of votes for each candidate  
Percentage_votes_Charles = (Votes_for_Charles/count)*100
Percentage_votes_Diana = (Votes_for_Diana/count)*100
Percentage_votes_Raymon = (Votes_for_Raymon/count)*100

#dictionary of candiates to find name of winner (key is name, value is percentage votes)
values = {"Charles Casper Stockham": (Percentage_votes_Charles), "Diana Degette": (Percentage_votes_Diana), "Raymon Anthony Doane":(Percentage_votes_Raymon)}
#calculate the maximum key from the dictionary 
winners_name = max(values, key=values.get)

#Analysis section
analysis = (f'''
Election Results
-------------------------
Total Votes:  {count}    
-------------------------
Charles Casper Stockham: {Percentage_votes_Charles:.3f}% ({Votes_for_Charles})
Diana DeGette: {Percentage_votes_Diana:.3f}% ({Votes_for_Diana}))
Raymon Anthony Doane: {Percentage_votes_Raymon:.3f}% ({Votes_for_Raymon}))
-------------------------
Winner: {winners_name} 
-------------------------''')
#print the analysis to the terminal
print(analysis)

#write the analysis to the text file
output_path = os.path.join('analysis.txt')
with open(output_path, 'w') as textfile:
    textfile.write(analysis)