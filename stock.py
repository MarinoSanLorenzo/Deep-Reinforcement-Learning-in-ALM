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
    	
	def __init__(self):
		self.brownianMotion()
		
		
	def brownianMotion(self, plot= False):
		self.brownian_motion = np.random.normal(0,1) 
