import numpy as np
import matplotlib.pyplot as plt
from modules.time import Time
from modules.stock import Stock
from modules.market import Market



class Portfolio(Time):
    
    def __init__(self, time_obj,market_obj, action_obj):
        self.portfolio_value0 = 1000
        self.time = time_obj.time
        self.portfolio_array = np.array(np.repeat(np.nan,len(self.time)))
        self.operation(market_obj,action_obj)
        self.portfolio_array[0] = self.portfolio_value
        
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
	            
            
            
            
        
