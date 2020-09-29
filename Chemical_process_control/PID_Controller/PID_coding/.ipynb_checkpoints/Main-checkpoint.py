import numpy as np
import matplotlib.pyplot as plt
import TankModel as TM

#create an object for the support functions.
Tank = TM.DrainTank()
H = Tank.TankModel()
t = np.linspace(0,200,101)

plt.plot(t,H)

plt.xlabel('minutes')
plt.ylabel('meters')
plt.title('Gravity-Drained Tank')
plt.legend(['Liquid Level']);
