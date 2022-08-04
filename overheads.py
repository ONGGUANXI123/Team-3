import csv
from pathlib import Path
# create file path to summary_report
file_path = Path.cwd()/'summary_report.txt'
# create file path to cash on hand csv
oh_csv = Path.cwd()/'csv_reports'/'Overhead.csv'
#create overhead function to find out maximum overhead
def overhead_function(forex):
        #open overhead csv in read mode
        with oh_csv.open(mode = 'r', encoding = 'UTF-8', newline="") as csvfile:
            #read the csv and return a reader object
            reader = csv.reader(csvfile)
            #create a dictionary to store both the expenses and amount of expense
            oh_dict = {}
            #skip csv header
            next(reader)
            #create for loop lines in the overhead csv
            for line in reader:
                # from reader take the expenses and convert it from usd to sgd then add them with the corresponding days which is the first value of line hence line[0]
                oh_dict[line[0]] = float(line[1]) * forex
            # set initial highest value as 0
        highest_value = 0
        #create a for loop to loop through the expense amount
        for i in oh_dict:
            #if the expense is greater than the highest value
            if oh_dict[i] > highest_value:
                #it will be replace and become the new highest value
                highest_value = oh_dict[i]
        #create a for loop to call back the days and the expenses from the dictionary using .item which the list wih keys and value
        for i, value in oh_dict.items():
            #if value matches the highest value from before means that the set of expense and value is the highest overhead 
            if value == highest_value:
                #open summary_txt in append mode
                    with file_path.open(mode = 'a', encoding = 'UTF-8', newline="") as file:
                        # write the expense with the highest overhead and round expense value to 2dp
                        words = file.write(f'\n[HIGHEST OVERHEADS] {i}: SGD{round(value, 2)}')