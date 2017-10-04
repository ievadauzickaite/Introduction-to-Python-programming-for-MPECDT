# Solve linear advection equation 

### Try FTBS

from  math import *
import numpy as np
import pylab

# Divide space into equal intervals
npoints = 40 # no of points

points = np.linspace(0, 1, npoints)

# Divide time into time steps
ntime = 100 # no of time steps

# Wind 
# Courant number
c = 0.2
d = 1 - c

# Initial conditions (dar reikia paziureti, kaip efektyviau padaryti)
# Pabandyti ir kitas pradines salygas
phi_new = []
for x in points:
    if x <= 0.5:
        phi_new.append(0.5 * (1 - cos(4 * pi * x)))
    else:
        phi_new.append(0)

phi_new = np.array(phi_new)
pylab.plot(points, phi_new)

for tstep in range(ntime): # ntime
    #phi_new = np.array(phi_new)
    #pylab.plot(point, phi_new)
    phi_old = phi_new[:]
    phi_new = []
    for j in range(npoints):
        phi_new.append(d * phi_old[j] + c * phi_old[j-1])
        
phi_new = np.array(phi_new)
pylab.plot(points, phi_new)

# Jeigu tasku skaicius ir c kitoks, kazkuriuo metu pabaiga pradeda
# kilti ir tada persinesa visa banga i sona. Kodel ir ar susije su krastais