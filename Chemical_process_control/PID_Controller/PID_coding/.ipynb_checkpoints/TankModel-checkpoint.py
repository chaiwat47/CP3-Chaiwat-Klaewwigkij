import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

class DrainTank:
    '''The following functions interact with the main file'''
    def __init__(self, area, Cv, IC, t):
		self.area = area
		self.Cv   = Cv
		self.t    = t
		return None
	
	def qin(self,t):
		return 0.15
	
	def solve(self,h,t):
		dh = qin(t)/self.A - self.Cv*np.sqrt(h)/self.A
		h = odeint(deriv,IC,t)
		self.h = h
		return h
	

		

