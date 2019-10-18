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
from modules.calc_total_value import calc_total_value         
#######	
#class Environment:
#	
#	def __init__(self):
#		self.state = 0
#		self.time_obj =Time()
#		self.t = self.time_obj.time
#		
#		self.stock = Stock(self.time_obj)
#		self.market = Market(self.time_obj)
#		self.action = Action(self.time_obj, self.market)
#		self.portfolio = Portfolio(self.time_obj, self.market, self.action)
#		
#		#		self.liabilities = Liabilities()
#	def displayEnv(self):
#		
#		while self.portfolio.portfolio_value > 0:
#			
#			for (t, (dec_key, dec_value), portfolio) in zip(self.t, self.action.decision_set.items(), self.portfolio.portfolio_cum):
#				print('---------------------------------------------------')
#				print(f'step : {t} :') 
#				print(f'{dec_key} : {dec_value}')
#				print(f'Portfolio Value : {portfolio}')
#				print('---------------------------------------------------')
#				time.sleep(0.8)
#				 	
#			break
#		
#	def startSimulation(self):
#		
#		step = 0
#		while True:
#			step +=1
#			self.time_obj =Time()
#			self.t = self.time_obj.time
#			
#			self.stock = Stock(self.time_obj)
#			self.market = Market(self.time_obj)
#			self.action = Action(self.time_obj, self.market)
#			self.portfolio = Portfolio(self.time_obj, self.market, self.action)
#			print('---------------------------------------------------')
#			print(f'step : {step}') 
#			print('The robot takes the following action: {0} : {1}'.format(self.action.decision_set.keys(), self.action.decision_set.values()))
#			print(f'Portfolio Value : {0}'.format(self.portfolio.portfolio_cum))
#			print('---------------------------------------------------')
#			time.sleep(0.8)
#			
#			if self.portfolio.portfolio_value < 950:
#				print("The Reinforcement Learning algorithm got us broken")
#				break
#			
#		else:
#			step = None
			
			
	
#e = Environment()


class Environment2:
	
	def __init__(self):
		self.simulateEnvironment()
		
		
	def simulateEnvironment(self):
		
		step = 0
#		bm_history_array1 = np.array([])
#		bm_history_array2 = np.array([])
#		self.bm_history_dic = {}
		self.stocks_history_dic = {}
		self.agent = Agent()
		self.action_history_dic = {}
		self.total_value_history = np.array([])
		
		s1 = Stock2(initial_value=100)
		s2 = Stock2(initial_value=100)
		
		while True:
			
			#generate stocks
			s1.autoCorrelation(step, mean = 0.001*s1.initial_value, sd=2)
			s2.autoCorrelation(step, mean = -0.001*s1.initial_value, sd=2)
	
	
			#store it as dictionnary
			self.stocks_history_dic['stock1'] = s1.cum_stock_value
			self.stocks_history_dic['stock2'] = s2.cum_stock_value
			
			current_stock_value1 = s1.cum_stock_value[step]
			current_stock_value2 = s2.cum_stock_value[step]
			
			# store agent action history
			action = self.agent.action(self.stocks_history_dic, step)
			self.action_history_dic[f'action_step_{step}'] = action
			# monitor portfolio
			self.agent.portfolio(self.stocks_history_dic, step)
	
			
			# calculate update total value CASH + SUM OF ASSET values
			self.total_value = calc_total_value(self.agent.cash_history, self.agent.asset_value_history_dic, step)
			self.total_value_history = np.append(self.total_value_history, self.total_value)
			# calculate profit of the operation
			self.agent.profit(self.total_value_history, step)
			
			print('---------------------------------------------------')
			print(f'step : {step} :') 
			print("Total value is {0}".format(self.total_value))
			print("Profit realized by the operation is {0}".format(self.agent.profit_history[step])) # or self.profit_step
			
			print('---------------------------------------------------')
			print(f'Current Stock Value 1: {current_stock_value1}')
			print(f'Current Stock Value 2: {current_stock_value2}')
			print('---------------------------------------------------')
			print(" Agent decision to buy : {0}".format(action['stock_to_buy']))
			print(" Agent decision to sell : {0}".format(action['stock_to_sell']))
			print(" Agent decision to keep : {0}".format(action['stock_to_keep']))
			
			print('---------------------------------------------------')
			print("The agent cash amount is : {0}".format(self.agent.cash_history[step]))
			print("The agent asset value of stock 1 is : {0}".format(self.agent.asset_value_history_dic["stock1"][step]))
			print("The agent asset value of stock 2 is : {0}".format(self.agent.asset_value_history_dic["stock2"][step]))
			print('---------------------------------------------------')
			step += 1 	
			time.sleep(0)
			plt.plot(np.arange(step), s1.cum_stock_value, label = "stock1")
			plt.plot(np.arange(step), s2.cum_stock_value, label = "stock2")
			plt.legend(loc= "best")
			plt.title("Stock evolution")
			plt.show()
			fig, ax = plt.subplots()
			ax.plot(np.arange(step),self.total_value_history)
			ax.axhline(y=self.agent.cash_value0,color='red',linestyle='--')
			plt.title("Total value evolution")
			plt.show()
#	
#			plt.plot(np.arange(step), self.total_value_history, label = "Total_value")
#			plt.legend(loc= "best")
#			plt.title("Total value evolution")
#			plt.show()
			
			if step > 10000 or self.total_value <0:
				print("Total profit: {0} at step {1}".format(self.total_value-self.agent.cash_value0, step))
				print("ROE: {0}".format(round(100*(self.total_value/self.agent.cash_value0)-1),2))
				break
		else:
#			step = None
			"never got out"
		
e = Environment2()



