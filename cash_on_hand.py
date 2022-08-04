import csv
from pathlib import Path

# create file path to summary_report
file_path = Path.cwd()/'summary_report.txt'
# create file path to cash on hand csv
coh_cwd = Path.cwd()/'csv_reports'/'Cash-on-hand.csv'

# create function to calculate if surplus or deficit 
def cashonhand_function(forex):
                # create empty list for days
    day = []
            # create empty list for cash 
    cash = []
    
        # open cash on hand csv on read mode a
    with coh_cwd.open(mode = 'r', encoding = 'UTF-8', newline="") as csvfile:
            # read csvfile and create reader object 
            reader = csv.reader(csvfile)
            # skip headers in csv file
            next(reader)
            # create for loop so that for each row in csv
            for row in reader:
                # it will append the days in the csv into the empty list days
                day.append(float(row[0]))
                # it will append the cash in the csv which has been converted to sgd into the empty list cash
                cash.append(float(row[1]) * forex)
   
    # set a global counter
    count = 0
    # create a for loop for amount in the cash list -1 as there is no next day to compare
    for amount in range(len(cash) - 1):
        # calculate difference in cash between each day
        diff = cash[amount] - cash[amount + 1]
        # if the difference is an positive number 
        if diff > 0:
                # open the summary_report txt as file in append mode 
                with file_path.open(mode = 'a', encoding = 'UTF-8', newline="") as file:
                    # write the day with the cash deficit followed by the amount which is rounded off into 2 decimal places 
                    text = file.write(f'\n[CASH DEFICIT] DAY: {day[amount + 1]}, AMOUNT: SGD{round(diff,2)  }')
                    # prevents writing of cash surplus as i add to the global count
                    count += 1
            
    # when no cash deficit count =0 when count = 0 cash surplus written 
    if count == 0:
            # when count = 0 it will open the summary_report txt as file in append mode
            with file_path.open(mode = 'a', encoding = 'UTF-8', newline="") as file:
                # write cash surplus 
                text = file.write(f'\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')