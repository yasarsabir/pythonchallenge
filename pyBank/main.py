#import dependencies
import os
import csv
import pandas as pd

#assign file to read
csvpath = os.path.join('Resources', 'budget_data.csv')

#set variables
count = 0
net_change_list = []
Maximum_profit = 0
month_max_profit =""
Maximum_loss = 0
month_max_loss = ""
total_profit_loss = 0

#open the file and read the data
with open(csvpath) as text: 
    data = csv.reader(text)
#discard hearder
    header = next(data)
    first_row = next(data)
    previous_net = float(first_row[1])

#1) COUNT the number of months using a for loop 
    for row in data:
        count  += 1
        total_net = int(row[1])
        
        #note count += 1 is same as count = count + 1
   #redundant code to check the data types of the numbers given in the csv file
        #print (total_net) 
        #print (previous_net)
        #print(type(previous_net))
        #print(type(total_net))
        # they were both strings

        net_change = total_net - previous_net
        previous_net = total_net
        net_change_list += [net_change]
        total_profit_loss += int(row[1])
        if net_change > Maximum_profit :
            Maximum_profit = net_change
            month_max_profit = row[0]
        if net_change < Maximum_loss:
            Maximum_loss = net_change
            month_max_loss = row [0]

average_change = sum(net_change_list)/len(net_change_list)

#need to fix the average change value 

# Print all the information
analysis = (f'''Financial Analysis
---------------------------- 
Total Months:   {int(count) + 1} 
Total: $  {total_profit_loss}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {month_max_profit}  ($ {int(Maximum_profit)} ) 
Greatest Decrease in Profits: {month_max_loss}  ($ {int(Maximum_loss)} ) '''
)
#print analysis
print(analysis)
# Export analysis to analysis.py.
#specify the output file
output_path = os.path.join('analysis.txt')
with open(output_path, 'w') as textfile:
    textfile.write(analysis)