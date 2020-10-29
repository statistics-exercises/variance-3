import matplotlib.pyplot as plt
import numpy as np

ssum, indices, S2 = 0, np.zeros(200), np.zeros(200)
for i in range(200) : 
  # Add code to setup the numpy arrays called indices and average to generate the desired
  # plot here.
  
  
  
# This will plot the graph for the data.  You should not need to adjust this.
plt.plot( indices, S2, 'ro' )
plt.xlabel("Number of random variables")
plt.ylabel("S^2")
plt.savefig("least_squares.png")
