import csv
from pathlib import Path

# create file path to summary_report.txt
file_path = Path.cwd()/'summary_report.txt'

# create file path to profit and loss csv
profitlost_cwd = Path.cwd()/'csv_reports'/'profit-and-loss-usd.csv'

# create function to calculate if the profit is in surplus or deficit
def profitandloss_function(forex):
        # create empty list
        day = []
        #create an empty list
        net_profit = []
   
        # open profit and loss csv on read mode 
        with profitlost_cwd.open(mode = 'r', encoding = 'UTF-8', newline = "") as csvfile:

            #read csv file and create reader object
            reader = csv.reader(csvfile)

            #skip title in the csv
            next(reader)

            #create for loop in each row of csv
            for line in reader:

                #from csv append the days into the day list 
                day.append(int(line[0]))

                #from csv append the net profit into the netprofit list
                net_profit.append(float(line[4]) * forex)

        # set global counter
        count = 0

        # create a for loop for amount in the netprofit, -1 as there is no next day to compare
        for amount in range(len(net_profit) - 1):

            # find difference in net profit between each day
            difference = net_profit[amount] - net_profit[amount + 1]

            # if the difference is greater than 0 means it is positive 
            if difference > 0:
            #when positive open summary_report txt in append mode 
                with file_path.open(mode = 'a', encoding = 'UTF-8', newline="") as file:

                # write the day with the profit deficit followed by the amount which is rounded off into 2 decimal places
                    msg = file.write(f'\n[PROFIT DEFICIT] DAY: {day[amount + 1]}, AMOUNT: SGD{round(difference, 2)}')

                    # add 1 to count so that surplus would not be printed
                    count += 1
            
        # when no profit deficit count =0 when count = 0 cash surplus written 
        if count == 0:            

            # when count = 0 it will open the summary_report txt as file in append mode
            with file_path.open(mode = 'a', encoding = 'UTF-8', newline="") as file:

                # Write NET PROFIT SURPLUS NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY into the summary_report txt
                msg = file.write(f'\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
        