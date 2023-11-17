# Import Code
import os
import csv

# Path to collect data from the Resources folder
Budgetdata = os.path.join ("C:\Users\njohanson\OneDrive - Federal Signal Corporation\Desktop\NU-VIRT-DATA-PT-10-2023-U-LOLC\02-Homework\03-Python\Instructions\Starter_Code\PyBank\Resources\budget_data.csv")
                                                          
# The total number of months included in the dataset
with open(Budgetdata) as csv_file:
    Budgetdata = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    counter = 0
for row in csv_reader:
  counter = counter + 1
print (counter)

# The net total amount of "Profit/Losses" over the entire period
current_profit_loss_ = int (row[1]) sum 
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
Final_profit.append row [1]
Final profits = total_loss + Profit_loss
# The greatest increase in profits (date and amount) over the entire period
Profit_loss= int(row 2)
Greatest_Increase = Max(profit_loss)
# The greatest decrease in profits (date and amount) over the entire period
GProfit_loss= int(row 2)
greatest_Decrease = Max (profit_Loss)

print (greatest_Decrease)
print (greatest_Increase)
print (current_profit_loss)
print (Final_Profit)
