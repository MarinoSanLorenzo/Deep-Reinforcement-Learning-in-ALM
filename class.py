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
			
		
class Portfolio(Time):
	
	def __init__(self, time_obj, plot = False):
		
		self.number_stock = 1
		self.time = time_obj.time
		self.stocks = [Stock(time_obj).random_process for i in range(self.number_stock)]
		self.value_portfolio = 0
		
		x= self.time
		self.stocks_dic = {}
		
		# not working because we should unpack dictionary values
		#line51: should be unpacked as arrays and not as dic_values inside 
		for i in range(self.number_stock):
			  self.stocks_dic[f'stock{i}'] = self.stocks[i]
			  if plot == True:
				    self.plot = plt.plot(x, self.stocks[i])
					
	

			  
    def buySell(self):
		
		if 
		
		
	
	def valuePortfolio(self):
		
		 
       
	
	
	
class Liabilities(Stock):
	
class Action:
	
	def __init__(self, time_obj):
		
		self.time = time_obj.time
		self.action()
		
		
	def action(self):
		
		self.action_value = np.random.choice(["buy","sell"])
		
		return self.action_value
		
	def actionSet(self):
		self.action_set =  [ self.action() for t in range(self.time.shape[0]) ] 	
	
	def chooseStock(self,portfolio_obj):
		self.choice_stock = np.random.randint(portfolio_obj.number_stock +1)
		return self.choice_stock
	
	def decision(self, portfolio_obj):
		self.decision_str = self.action() + "stock" + str(self.chooseStock(portfolio_obj))
		return self.decision_str
	
	def decisionSet(self, portfolio_obj):
		self.decision_set =  [ self.decision(portfolio_obj) for t in range(self.time.shape[0]) ] 	
	
	def operation(self, portfolio_obj):
		
		if self.action == "buy":
			
			
			portfolio_obj.value_portfolio = portfolio_obj.value_portfolio 
						
		
		
		
		
		
	
class State:
	
	

	
class Environment:
	
	def __init__(self):
		self.state = 0
		self.action = Action()
		self.stock = Stock()
		self.liabilities = Liabilities()
	
	