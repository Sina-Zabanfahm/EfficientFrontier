#!/usr/bin/env python
# coding: utf-8

# In[84]:


import datareader
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.optimize as sco


# In[80]:


class RnPrConstructor:
    """
    Class will receive historical data, start_date and
    end_date and computes randomized weights for a portfolio
    """
    def __init__ (self,data, start_date = '2020-03-01',
                  end_date = '2023-03-01'):
        
        self.data = data
        start_date = start_date
        end_date = end_date
        self.weights = None
        
    def construct_weights(self):
        idx = self.data.columns
        self.weights = np.random.rand(len(self.data.columns))
        self.weights = self.weights / np.sum(self.weights)
        #print(self.weights)
        self.weights = self.weights
        return np.array(self.weights)
    
    def get_dates(self):
        
        return {'start_date': start_date, 'end_date': end_date}
    
    def get_weights(self):
        
        return self.weights
    

