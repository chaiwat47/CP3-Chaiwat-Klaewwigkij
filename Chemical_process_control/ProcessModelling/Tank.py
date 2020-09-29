import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

Cv  = 0.1     # Outlet valve constant [cubic meters/min/meter^1/2]
A   = 10.0     # Tank area [meter^2]

# inlet flow rate in cubic meters/min
def qin(self,t):
    return 0.15

def deriv(self,h,t):
    return qin(t)/A - Cv*np.sqrt(h)/A  # dh/dt = qin(t)/A - Cv*np.sqrt(h)/A

IC = [0.0] # initial condition
t = np.linspace(0,2000,1001)
h = odeint(deriv,IC,t) # solve derivative equation

plt.plot(t,h)

plt.xlabel('minutes')
plt.ylabel('meters')
plt.title('Gravity-Drained Tank')
plt.legend(['Liquid Level'])
plt.show()
print('K')
