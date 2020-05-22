# Python program to get the real-time 
# currency exchange rate 
  
# Function to get real time currency exchange  
def RealTimeCurrencyExchangeRate(currency) : 
  
    # importing required libraries 
    import requests, json 
  
    # base_url variable store base url  
    base_url = r"https://www.freeforexapi.com/api/live?"
  
    # main_url variable store complete url 
    #main_url = base_url + "pairs=" + from_currency+ to_currency

    

    # get method of requests module  
    # return response object  
    req_ob = requests.get(base_url + "pairs=" + currency[1]+ currency[0]) 
  
    # json method return json format 
    # data into python dictionary data type. 
      
    # result contains list of nested dictionaries 
    result = req_ob.json()

    print(result)
    '''print(" Result after parsing the json data :\n",
          result["rates"]["USDJMD"]["rate"]) '''
  
  
# Driver code 
if __name__ == "__main__" : 
  
    # currency code 
    currency = ('USD', 'KYD')
  
  
    # function calling 
    RealTimeCurrencyExchangeRate(currency) 
