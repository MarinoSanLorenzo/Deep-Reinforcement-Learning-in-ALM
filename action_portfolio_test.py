# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:02:12 2019

@author: sam
"""

import numpy as np 

step = 3
current_value_stock = {}
portfolio_nbstock_history_dic = {"stock1" : np.array([]), "stock2" : np.array([])}
portfolio_vstock_history_dic = {"stock1" : np.array([]), "stock2" : np.array([])}
portfolio_value = 

for stock, value in e.stocks_history_dic.items():
	current_value_stock[stock] = value[step]

for action, stocks in a.action_dic.items():
	
	if "buy" in action:
		for stock in stocks:
			portfolio_nbstock_history_dic[stock] = np.append(portfolio_nbstock_history_dic[stock] , 1)
			portfolio_vstock_history_dic[stock] = np.append(portfolio_vstock_history_dic[stock] , current_value_stock[stock])
		


	elif "sell" in action:
		for stock in stocks:
			portfolio_nbstock_history_dic[stock] = np.append(portfolio_nbstock_history_dic[stock] , -1)
			portfolio_vstock_history_dic[stock] = np.append(portfolio_vstock_history_dic[stock] , current_value_stock[stock])
		

#	elif "keep" in action:
#		for stock in stocks:
#			portfolio_nbstock_history_dic[stock] = np.append(portfolio_nbstock_history_dic[stock] , 1)
#			portfolio_vstock_history_dic[stock] = np.append(portfolio_vstock_history_dic[stock] , current_value_stock[stock])
#		
#
#		
#		
