# -*- coding: utf-8 -*-

"""
Created on Thu Sep 26 21:02:04 2019

@author: sam
"""
import numpy as np
import matplotlib.pyplot as plt

class Time:
	
	def __init__(self):
		self.t0= 0
		self.loopingTime()
		
	def loopingTime(self):
#		self.period_max = int(input("Enter a maximal period time :"))
		self.period_max = 100
		self.time = np.arange(self.t0, self.period_max)
		
class Stock(Time):
	
	def __init__(self):
		self.v0 = 0
		self.time = Time().time
		self.brownianMotion()
		
	def brownianMotion(self, plot= False):
		self.brownian_motion = np.random.normal(0,1, self.time.shape[0]) 
		self.random_process = np.cumsum(self.brownian_motion)
		
		if plot == True:
			self.plot = plt.plot(self.time, self.random_process)	
			
		
class Portfolio(Time):
	
	def __init__(self, plot = False):
		self.number_stock = 10
		self.time = Time().time
		self.stocks = [Stock().random_process for i in range(self.number_stock)]
		
		if plot == True:
			x= self.time
			self.dic = {}
			
			# not working because we should unpack dictionary values
			#line51: should be unpacked as arrays and not as dic_values inside 
			for i in range(self.number_stock):
				  self.dic[f'stock{i}'] = self.stocks[i]
				  self.plot = plt.plot(x, self.stocks[i])
	
	
	
class Liabilities:
	
class Action:
	

	
class Environment:
	
	def __init__(self):
		self.state = 0
		self.action = Action()
		self.stock = Stock()
		self.liabilities = Liabilities()
	
	