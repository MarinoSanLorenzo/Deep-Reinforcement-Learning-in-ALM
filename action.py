
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

			self.cash_value0 = 1000
			self.asset_nbstock_history_dic = {"stock1" : np.array([]), "stock2" : np.array([])}
			self.asset_vstock_history_dic = {"stock1" : np.array([]), "stock2" : np.array([])}
			self.asset_value_history_dic = {}
			self.cash_history = np.array([])
			self.action_dic_history = {}
			
		def action(self, stocks_history_dic, step):
			self.mean_value_dic = {} 	
			self.variation_last_step_dic = {} 
			self.action_dic = {}
			self.stock_to_buy_dic = {}
			self.stock_to_sell_dic = {}
			self.stock_to_keep_dic = {}
			  
			for stock_name, stock_value in stocks_history_dic.items():
				# for decision to keep stock
#				  self.mean_value_dic[bm] = np.mean(history) # for decision
				# for decision to buy/sell stock
				  self.variation_last_step_dic[stock_name] = calc_var_step(stock_value[-3:step]) 
			
			
			
			for stock_name, variation in self.variation_last_step_dic.items():
				
				if variation > 0.1:
					self.stock_to_buy_dic[stock_name] = variation # rename the bm key as stock for the aaction/decision of agent
				elif variation < -0.1:
					self.stock_to_sell_dic[stock_name] = variation
				elif variation <= 0.1 and variation >= -0.1:
					self.stock_to_keep_dic[stock_name] = variation
					
			
			
			
			self.stock_to_buy = list(self.stock_to_buy_dic.keys())
			self.stock_to_sell = list(self.stock_to_sell_dic.keys())
			self.stock_to_keep = list(self.stock_to_keep_dic.keys())
#			self.stock_to_keep = max(self.mean_value_dic).replace("bm", "stock",1)
#			self.stock_to_buy =max(self.mean_value_dic.items(), key=operator.itemgetter(1))[0]
			
			self.action_dic = {"stock_to_buy" : self.stock_to_buy, "stock_to_sell" : self.stock_to_sell, "stock_to_keep" : self.stock_to_keep}
			self.action_dic_history[f'action_step_{step}'] = self.action_dic
			
			return (self.action_dic)
			
			
		def portfolio(self, stocks_history_dic, step):
			
			self.current_value_stock = {}
			
			if step ==0:
				print("step0")
				self.cash_history = np.append(self.cash_history,self.cash_value0)
				
			elif step!=0:
				
				for stock, value in stocks_history_dic.items():
					self.current_value_stock[stock] = value[step]
			
				for action, stocks in self.action_dic.items():
					
					if "buy" in action and len(stocks)!= 0:
						print("buy")
						for stock in stocks:
	    						if self.cash_history[step-1] >= self.current_value_stock[stock]:
								   
									   self.asset_nbstock_history_dic[stock] = np.append(self.asset_nbstock_history_dic[stock] , 1)
									   self.asset_vstock_history_dic[stock] = np.append(self.asset_vstock_history_dic[stock] , self.current_value_stock[stock])
									   self.volume_operation = float(self.asset_nbstock_history_dic[stock]*self.asset_vstock_history_dic[stock] )
									   # buy by withdrawing the value on the cash dic
									   print("cash_history : {0} -- volume_operation {1}".format(self.cash_history, volume_operation))
									   self.cash_history = np.append(self.cash_history, self.cash_history - self.volume_operation)
									   self.asset_value_history_dic[stock] = np.append(self.asset_value_history_dic[stock] ,volume_operation)
	    						else:
									   print("not enough cash :{0} to buy {1} of value {2}".format(self.cash_history[step-1], stock,self.current_value_stock[stock] ))
				
					elif "sell" in action and len(stocks) != 0:
						print("sell")
						for stock in stocks:
    						# get values of number of stock and current values on the market
							self.asset_nbstock_history_dic[stock] = np.append(self.asset_nbstock_history_dic[stock] , 1)
							self.asset_vstock_history_dic[stock] = np.append(self.asset_vstock_history_dic[stock] , self.current_value_stock[stock])
							self.volume_operation = -float(self.asset_nbstock_history_dic[stock]*self.asset_vstock_history_dic[stock])
							# sell by withdrawing the value on the cash dic
							self.cash_history = np.append(self.cash_history, self.cash_history[step] + self.volume_operation)
							self.asset_value_history_dic[stock] = np.append(self.asset_value_history_dic[stock] ,self.volume_operation)
						
					else:
						print("do nothing")
						self.cash_history = np.append(self.cash_history, self.cash_history[step-1])
						for stock, asset_values in self.asset_value_history_dic.items():
							
							asset_values = np.append(asset_values, asset_values[step-1])
			
			return(self.asset_value_history_dic , self.cash_history)						
			
			





#    	def reward(self, actions_history):		


	