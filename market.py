import numpy as np
import matplotlib.pyplot as plt
from modules.time import Time
from modules.stock import Stock

		
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
