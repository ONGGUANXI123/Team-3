import requests 
from pathlib import Path

#set file path to summary_report.txt
file_path = Path.cwd()/'summary_report.txt'
# .touch() created a new txt called 'summary_report.txt'
file_path.touch()

#create variable to store apikey
apikey = '9WJYXMOWLRTGBAMU'

#create variable 'Alphavantage' to store api with apikey inserted
Alphavantage = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={apikey}'

#upon requests call the data from the api
response = requests.get(Alphavantage)

#use json to extract the data from the api
data = response.json()


#create a function to extract the exchange rate from the nested list 
def api_function():

    #pm25 to extract only the exchange rate from the nested list
    pm25 = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

    #float the str to become an decimal 
    pm25 = float(pm25)
    #print(pm25)
    #exchange_rate = f'[CURRENCY COVERSION RATE] USD1 = SGD{pm25}'

    #ensure that the file_path exist 
    if file_path.exists():

        #when file_path exist open the file_path using append as file
        with file_path.open(mode= "a", encoding= "UTF-8", newline= "") as file:

            #then write the conversion rate from the api into file
            file.write(f'[CURRENCY COVERSION RATE] USD1 = SGD{pm25}')
            
    #return the conversion rate value 
    return pm25