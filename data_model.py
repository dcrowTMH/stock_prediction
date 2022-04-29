import yfinance as yf
import pandas as pd
import numpy as np

class Data_model():
    
    def __init__(self):
        self.data_dict = {}
        self.stock = ['TSLA', 'AAPL', 'MSFT'] # focus on TSLA, AAPL & MSFT first
        self.period = '3mos' # using 3month of data to predict the upcoming Close price
        
    def data_gain(self):
        stock_dict = {}
        for i in self.stock:
            ticker = yf.Ticker(f"{i}")
            stock_dict[f'{i}'] = ticker.history(period = self.period)
            stock_dict[f'{i}'].to_csv(f'data/{i}.csv', index = False) # save the data in data folder
        self.data_dict['raw_data'] = stock_dict
        
model = Data_model()
model.data_gain()