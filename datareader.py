# -*- coding: utf-8 -*-
"""DataReader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aJufo48MFnSjQOSDbiYzcZGqcTEK7k1M
"""

import pandas as pd
import numpy as np
import yfinance as yf
import json


class DataReader:

    def __init__ (self, directory, start_date, end_date, risk_free_rate =0.06):

        """
        directory is the indormation of the raw json file

        assets are the set of the securities
        shorts is the set of stocks to be shorted
        longs is the set of stock in long position
        data stores the historical information of the assets
        [start_date, end_date] is the period to receive the data
        """
        self.directory = directory
        self.assets = []
        self.shorts = []
        self.longs = []
        self.data = pd.DataFrame()
        self.start_date = start_date
        self.end_date = end_date
        self.risk_free_rate = risk_free_rate
        
        self.read_data()


    def read_data(self):

        with open(self.directory) as f:
            self.assets = json.load(f)
        #reading the shorts and longs
        
        short_names = self.assets['shorts']
        long_names = self.assets['longs']
        self.assets = short_names+long_names

        #reading the historical data by the closed column from yfinance
        self.data  = yf.download(self.assets, self.start_date, self.end_date)['Close']


        """
        It is possible that some of the assets might be delisted in that time period.
        we will remove those from the shorts longs and assets.
        Moreover, we drop the columns with missing values.

        """

        self.data.dropna(axis = 1, inplace = True)
        self.data.set_index(pd.to_datetime(self.data.index), inplace = True)

        self.assets= self.data.columns
        
        for col in self.assets:
            if col in short_names:
                self.shorts.append(col)
            if col in long_names:
                self.longs.append(col)

    def get_asset_names(self):
        return {'assets': self.assets, 'shorts': self.shorts, 'longs' : self.longs}

    def get_dates(self):
        return {'start_date:': self.statr_date, 'end_date': self.end_date}
   
    def get_data(self):
        return self.data



