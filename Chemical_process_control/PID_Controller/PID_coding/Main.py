import numpy as np
import matplotlib.pyplot as plt
import TankModel as TM

#create an object for the support functions.
t = np.linspace(0,200,101)
IC = [0.0]
A = 1.0
Cv = 0.1
H = TM.DrainTank(A,Cv,IC,t)


#print(t)
#plt.plot(t,H)
print(H)
#plt.xlabel('minutes')
#plt.ylabel('meters')
#plt.title('Gravity-Drained Tank')
#plt.legend(['Liquid Level']);
