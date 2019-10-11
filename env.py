# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:23:17 2019

@author: sam
"""

# -*- coding: utf-8 -*-

"""
Created on Thu Sep 26 21:02:04 2019
@author: sam
"""
import time
import numpy as np
import matplotlib.pyplot as plt
import os


path = "C:\\Users\\sam\\Documents\\DL\\Reinforcement Learning in ALM\\Deep-Reinforcement-Learning-in-ALM-master\\Deep-Reinforcement-Learning-in-ALM-master"
os.chdir(path)

from modules.time import Time
from modules.stock import Stock, Stock2
from modules.market import Market
from modules.portfolio import Portfolio
from modules.action import Action, Agent            
	
class Environment:
	
	def __init__(self):
		self.state = 0
		self.time_obj =Time()
		self.t = self.time_obj.time
		
		self.stock = Stock(self.time_obj)
		self.market = Market(self.time_obj)
		self.action = Action(self.time_obj, self.market)
		self.portfolio = Portfolio(self.time_obj, self.market, self.action)
		
		#		self.liabilities = Liabilities()
	def displayEnv(self):
		
		while self.portfolio.portfolio_value > 0:
			
			for (t, (dec_key, dec_value), portfolio) in zip(self.t, self.action.decision_set.items(), self.portfolio.portfolio_cum):
				print('---------------------------------------------------')
				print(f'step : {t} :') 
				print(f'{dec_key} : {dec_value}')
				print(f'Portfolio Value : {portfolio}')
				print('---------------------------------------------------')
				time.sleep(0.8)
				 	
			break
		
	def startSimulation(self):
		
		step = 0
		while True:
			step +=1
			self.time_obj =Time()
			self.t = self.time_obj.time
			
			self.stock = Stock(self.time_obj)
			self.market = Market(self.time_obj)
			self.action = Action(self.time_obj, self.market)
			self.portfolio = Portfolio(self.time_obj, self.market, self.action)
			print('---------------------------------------------------')
			print(f'step : {step}') 
			print('The robot takes the following action: {0} : {1}'.format(self.action.decision_set.keys(), self.action.decision_set.values()))
			print(f'Portfolio Value : {0}'.format(self.portfolio.portfolio_cum))
			print('---------------------------------------------------')
			time.sleep(0.8)
			
			if self.portfolio.portfolio_value < 950:
				print("The Reinforcement Learning algorithm got us broken")
				break
			
		else:
			step = None
			
			
	
e = Environment()


class Environment2:
	
	def __init__(self):
		self.simulateEnvironment()
		
		
	def simulateEnvironment(self):
		
		step = 0
		bm_history_array1 = np.array([])
		bm_history_array2 = np.array([])
		bm_history_dic = {}
		stocks_history_dic = {}
		agent = Agent()
		while True:
			s1 = Stock2().brownian_motion
			s2 = Stock2().brownian_motion
			
			bm_history_array1 = np.append(bm_history_array1,s1)
			bm_history_array2 = np.append(bm_history_array2,s2)
			
			bm_history_dic['bm1'] = bm_history_array1
			bm_history_dic['bm2'] = bm_history_array2
			
			cum_stock_value1 = np.cumsum(bm_history_array1)
			cum_stock_value2 = np.cumsum(bm_history_array2)
			
			stocks_history_dic['stock1'] = cum_stock_value1
			stocks_history_dic['stock2'] = cum_stock_value2
			
			current_stock_value1 = cum_stock_value1[step]
			current_stock_value2 = cum_stock_value2[step]
			
			
			
			step += 1
			print('---------------------------------------------------')
			print(f'step : {step} :') 
			print(f'Current Stock Value 1: {current_stock_value1}')
			print(f'Current Stock Value 2: {current_stock_value2}')
			print(" Agent decision : {0}".format(agent.action(bm_history_dic)))
			print('---------------------------------------------------')
			time.sleep(0.5)
			plt.plot(np.arange(step), cum_stock_value1, label = "stock1")
			plt.plot(np.arange(step), cum_stock_value2, label = "stock2")
			plt.legend(loc= "best")
			plt.title("Stock evolution")
			plt.show()
			 	
			if current_stock_value1 < -3:
				print("Big Loss {0} at step {1}".format(current_stock_value1, step))
				break
		else:
#			step = None
			"never got out"
		
e = Environment2()



