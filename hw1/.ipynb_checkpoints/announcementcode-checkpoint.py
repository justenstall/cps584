%matplotlib inline

from IPython import display

import time

 

l = -((b + (k*w1))/w2) # line equation to plot

plt.plot(k,l,linestyle='--', c='g') 

display.display(plt.gcf()) 

display.clear_output(wait=True)

time.sleep(0.000001)