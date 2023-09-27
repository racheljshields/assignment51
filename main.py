#This is a dictionary of stocks

#Start by creating the dictionary of stocks 
stocks_dict={
  "TSLA": "Tesla (TSLA) - 248.50",
  "F":"Ford (F) - 12.30",
  "AMZN": "Amazon Inc. (AMZN) - 138.23",
  "T": "AT&T Inc. (T) - 14.40",
  "VZ": "Verizon Communication Inc. (VZ) - 33.45",
  "GOOGL": "Alphanet Inc. (GOOGL) - 136.38",
  "NOK": "Nokia Oyj (NOK) - 4.04",
  "SNAP": "Snap Inc. (SNAP) - 9.39",
  "CMCSA": "Comcast Corporation (CMCSA) - 45.03",
  "AAPL":"Apple Inc. (AAPL) - 178.04",
}
#Retrieve the ticker from the user
x = input('Please enter your stock symbol:')
#Utilize the stock_dict.get to provide a message for tickers not in the dictionary
z=stocks_dict.get(x)
print(z)
