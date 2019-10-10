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

class Time:
	
	def __init__(self):
		self.t0= 0
		self.loopingTime()
		
	def loopingTime(self, period_max = 1):
#		self.period_max = int(input("Enter a maximal period time :"))
		self.period_max = period_max
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
			
		
class Market(Time):
	
	def __init__(self, time_obj, plot = False):
		
		self.number_stock = 10
		self.time = time_obj.time
		self.stocks = [Stock(time_obj).random_process for i in range(self.number_stock)]
		
		
		x= self.time
		self.stocks_dic = {}
		
		# stire all random process in dictionnary :
        # {stock0 : array(...), stock1 : array(...),...}
		for i in range(self.number_stock):
			  self.stocks_dic[f'stock{i}'] = self.stocks[i]
			  if plot == True: # choose to display plot or not set to False by default
				    self.plot = plt.plot(x, self.stocks[i], label = f'stock{i}')
				    plt.legend(loc = "best")
				    plt.title("Stocks evolution")
        
class Portfolio(Time):
    
    def __init__(self, time_obj,market_obj, action_obj):
        self.portfolio_value0 = 1000
        self.time = time_obj.time
        self.portfolio_array = np.array(np.repeat(np.nan,len(self.time)))
        self.operation(market_obj,action_obj)
#        self.portfolio_array[0] = self.portfolio_value
        
    def operation(self, market_obj, action_obj, showPlot= False):
        decision = list(action_obj.decision_set.values())
        market = market_obj.stocks_dic
        stock_id = action_obj.stock_id 

        for (i,  id_stock, dec) in zip(self.time,stock_id, decision ):
            if "buy" in dec:
                self.portfolio_array[i] = market[id_stock][i] # add to the portfolio the stock to buy 
            elif "sell" in dec:
                 self.portfolio_array[i] = -market[id_stock][i] # add to the portfolio the stock to buy 
            self.portfolio_value = self.portfolio_array[i] + self.portfolio_value0	# update the value of portfolio by the last item in the array		      
		
        
        self.portfolio_cum = np.cumsum(self.portfolio_array)  + self.portfolio_value0
        if showPlot == True:
	        self.plot_portfolio = plt.plot(self.time, self.portfolio_cum  )
	        plt.title("Portfolio evolution")
	            
            
            
            
        
        

#class Liabilities(Stock):
#	
            
class Action:
	
	def __init__(self, time_obj, market_obj):
		
		self.time = time_obj.time
		self.actionSet()
		self.chooseStock(market_obj)
		self.decision(market_obj)
        
		
		
	def action(self):
		
		self.action_value = np.random.choice(["buy","sell"])
		
		return self.action_value
		
	def actionSet(self):
		self.action_set =  [ self.action() for t in range(self.time.shape[0]) ] 	
		return self.action_set
    
	def chooseStock(self,market_obj):
		# generate stock index for further indexing in the portfolio class
		self.choice_stock = [np.random.randint(market_obj.number_stock ) for t in range(self.time.shape[0]) ]
		return self.choice_stock
	
	def decision(self, market_obj):
        # concatenate the decision buy/sell + stock_{i} eg. {decision0 : "buy stock6",...}
		self.decision_set = {}
		self.stock_id = []
		for ((i, act), stock_index) in zip(enumerate(self.action_set), self.choice_stock):
                  self.decision_set[f'decision_{i}'] = act + " stock" + str(stock_index)
                  self.stock_id.append("stock" + str(stock_index))
		return self.decision_set
	# be careful change the decision set



	
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


