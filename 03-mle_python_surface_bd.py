# import modules
import numpy as np
import matplotlib.pyplot as plt

N = 50
S = np.arange(1,N+1)
theta = np.linspace(0.1,0.9,100)

# Likelihood Estimate
S_grid, theta_grid = np.meshgrid(S, theta)
L = S_grid*np.log(theta_grid) + (N-S_grid)*np.log(1-theta_grid)

# installing qt
fig = plt.figure() 
ax = fig.add_subplot(111,projection='3d')
s = ax.plot_surface(S_grid, theta_grid, L, cmap='jet')
ax.set_xlabel('S')
ax.set_ylabel('theta')
ax.set_zlabel('L(theta|S)')
ax.view_init(65,15)
# plt.show()
plt.savefig("./plots/sThetaL.png")