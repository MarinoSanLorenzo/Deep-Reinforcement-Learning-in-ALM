
import numpy as np

class Time:
	
	def __init__(self):
		self.t0= 0
		self.loopingTime()
		
	def loopingTime(self, period_max = 1):
#		self.period_max = int(input("Enter a maximal period time :"))
		self.period_max = period_max
		self.time = np.arange(self.t0, self.period_max)
		