
import numpy as np
import matplotlib.pyplot as plt
import operator
from modules.time import Time
from modules.stock import Stock
from modules.market import Market
from modules.calc_var_step import calc_var_step


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

			self.portfolio_value0 = 1000
			
			
		def action(self, bm_history_dic, step):
			self.mean_value_dic = {} 	
			self.variation_last_step_dic = {} 
			self.action_dic = {}
			self.stock_to_buy_dic = {}
			self.stock_to_sell_dic = {}
			self.stock_to_keep_dic = {}
			  
			for bm, history in bm_history_dic.items():
				# for decision to keep stock
				  self.mean_value_dic[bm] = np.mean(history) # for decision
				# for decision to buy/sell stock
				  self.variation_last_step_dic[bm] = calc_var_step(history[-3:step]) 
			
			
			
			for bm, variation in self.variation_last_step_dic.items():
				if variation > 0.1:
					self.stock_to_buy_dic[bm.replace("bm", "stock",1)] = variation # rename the bm key as stock for the aaction/decision of agent
				elif variation < -0.1:
					self.stock_to_sell_dic[bm.replace("bm", "stock",1)] = variation
				elif variation <= 0.1 and variation >= -0.1:
					self.stock_to_keep_dic[bm.replace("bm", "stock",1)] = variation
					
			
			
			
			self.stock_to_buy = list(self.stock_to_buy_dic.keys())
			self.stock_to_sell = list(self.stock_to_sell_dic.keys())
			self.stock_to_keep = list(self.stock_to_keep_dic.keys())
#			self.stock_to_keep = max(self.mean_value_dic).replace("bm", "stock",1)
#			self.stock_to_buy =max(self.mean_value_dic.items(), key=operator.itemgetter(1))[0]
			
			self.action_dic = {"stock_to_buy" : self.stock_to_buy, "stock_to_sell" : self.stock_to_sell, "stock_to_keep" : self.stock_to_keep}
			
			
			return (self.action_dic)
			
			
		def portfolio(self, stocks_history_dic):
			self.portfolio_value0
			
			
			
			





#    	def reward(self, actions_history):		


	