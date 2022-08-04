import api, cash_on_hand, overheads, profit_loss
#from the 4 other files import 
from pathlib import Path

#create function to run all 4 functions at once
def main():

    #create variable forex to contains the exchange rate from usd to sgd
    forex = api.api_function()

    #from overheads.py import overhead_function with forex as parameter 
    overheads.overhead_function(forex)

    #from cash_on_hand.py import cashonhand_function with forex as parameter 
    cash_on_hand.cashonhand_function(forex)

    #from profit_loss.opy import profitloss_function with forex as parameter 
    profit_loss.profitandloss_function(forex)

#call back function
main()

