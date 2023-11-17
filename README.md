# PyPoll # Import Code
import os
import csv

udgetdata = os.path.join ("C:\Users\njohanson\OneDrive - Federal Signal Corporation\Desktop\NU-VIRT-DATA-PT-10-2023-U-LOLC\02-Homework\03-Python\Instructions\Starter_Code\PyBank\Resources\budget_data.csv")
                                                          
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

#The total number of votes cast
current_Votes_ = int (row[1]) 

total_votes = current_Votes_(sum)

print (total Votes)
#A complete list of candidates who received votes
list(row (2))
complete= list(row 2)
candiates = Max(complete)
#The percentage of votes each candidate won
percentage = row(3) Percentage 
#The total number of votes each candidate won
Each_canident=["jefferson","charles","Cooper"]
Each_canident.count = row (3)
#The winner of the election based on popular vote
Winner= Max("jefferson","Charles","Cooper")
Print (Winner)
