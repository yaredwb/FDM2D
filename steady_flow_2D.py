import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.linalg as lin

matplotlib.rcParams['figure.figsize'] = 6.2, 5

# Spatial discretization
Nx = Ny = 20

# Construct the Coefficient matrix A
Bdiag  = -4 * np.eye(Nx-1)
Bupper = np.diag([1] * (Nx-2), 1)
Blower = np.diag([1] * (Nx-2), -1)
B = Bdiag + Bupper + Blower

Bs = [B] * (Nx-1)

A = lin.block_diag(*Bs)

Dupper = np.diag(np.ones((Nx-1)*(Nx-2)), Nx-1)
Dlower = np.diag(np.ones((Nx-1)*(Nx-2)), -Nx+1)

np.set_printoptions(threshold=np.inf)

A += Dupper + Dlower

# Construct the RHS vector b
b = np.zeros((Nx-1)**2)
b[-Nx+1:] = -10

# Solve the linear system Ax = b
h = lin.solve(A,b)

# Add boundary conditions to solution and reshape to a 2D array
h = h.reshape((Nx-1,Ny-1))
h2D = np.zeros((Nx+1,Ny+1))  # Whole grid with unknown nodes and BCs
h2D[0] = 10                  # BC at the top for this particulat example
h2D[1:-1,1:-1] = h[::-1]     # h[::-1] reverses the array h


x = np.linspace(0,1,Nx+1)
y = np.linspace(1,0,Ny+1)

X, Y = np.meshgrid(x,y)

plt.clf()
#plt.pcolormesh(X,Y,h2D)
plt.contourf(X,Y,h2D,10)
plt.colorbar()
plt.xlabel(r'$x$ [$\mathrm{m}$]')
plt.ylabel(r'$y$ [$\mathrm{m}$]')
#plt.savefig('2D_Flow_Nx_Ny_' + str(Nx) + '.eps')