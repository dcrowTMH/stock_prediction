#libraries import
import yfinance as yf
import pandas as pd
import numpy as pd

def get_stock_hist(period, stock_dict, *stock):
    """
    get the historical price of stock within a period
    
    Parameters
    -----------
    curr: str, short form of the currecy. e.g.US dollar - 'USD'
    
    period: str, period for obtaining the data e.g.'1d','5d','1mos','3mos','6mos','1y','2y','5y','10y','ytd','max'
    
    stock: str, sympbol for the stock e.g. 'TSLA', 'AAPL'
    
    Returns
    -----------
    stock_dict: dict to cotain the dataframe of crypto currency with target currency
    """
    for i in stock:
        ticker = yf.Ticker(f"{i}")
        stock_dict[f'{i}'] = ticker.history(period = period)
    return stock_dict
