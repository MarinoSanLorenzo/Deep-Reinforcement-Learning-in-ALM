
import numpy as np
import matplotlib.pyplot as plt
import operator
from modules.time import Time
from modules.stock import Stock
from modules.market import Market


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


class Agent:
		
		def __init__(self):
			self.mean_value_dic = {} 	
			self.portfolio_value0 = 1000
			
		def action(self, bm_history_dic):
			  
			for bm, history in bm_history_dic.items():
				  self.mean_value_dic[bm] = np.mean(history)
			
			if   
			self.stock_to_buy = max(self.mean_value_dic).replace("bm", "stock",1)
#			self.stock_to_buy =max(self.mean_value_dic.items(), key=operator.itemgetter(1))[0]
			
			return self.stock_to_buy
			
			






#    	def reward(self, actions_history):		


	