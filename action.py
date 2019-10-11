
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
	
		def action(self, bm_history_dic):
			  
			for stock, history in bm_history_dic.items():
				  self.mean_value_dic[stock] = np.mean(history)
				  
			self.stock_to_buy =max(self.mean_value_dic.items(), key=operator.itemgetter(1))[0]
#			stock_list = []
#			mean_list = np.array([])
#			for stock, mean in self.mean_value_dic.items():
#				stock_list.append(stock)
#				mean_list = np.append(self.mean_value_dic, mean)
			
#			print("buy {0}".format(self.stock_to_buy))
			
			return self.stock_to_buy
			
			






#    	def reward(self, actions_history):		


	