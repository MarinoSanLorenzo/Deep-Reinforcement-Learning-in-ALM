import numpy as np
import time
import matplotlib.pyplot as plt
from modules.time import Time


class Stock:
    	
	def __init__(self, time_obj):
		self.v0 = 0
		self.time = time_obj.time
		self.brownianMotion()
		
	def brownianMotion(self, plot= False):
		self.brownian_motion = np.random.normal(0,1, self.time.shape[0]) 
		self.random_process = np.cumsum(self.brownian_motion)
		
		if plot == True:
			self.plot = plt.plot(self.time, self.random_process)	
			

class Stock2:
    	
	def __init__(self, initial_value = 100, index = None):
		self.initial_value = initial_value
		self.cum_stock_value = np.array([])
		self.index = index

		
	def __str__(self):
		if self.index is None:
			return("stock")
		elif not(self.index is None):
			return("stock"+str(self.index))
		
	def autoCorrelation(self, step, mean=0, sd=1,plot= False):
		
		if step == 0:
			self.cum_stock_value = np.append(self.cum_stock_value, self.initial_value)
		else:
			stock_value = max(self.cum_stock_value[step-1] +  np.random.normal(mean,sd),0)  # can't have a stock lower than 0
			self.cum_stock_value = np.append(self.cum_stock_value, stock_value)
		
    