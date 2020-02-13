import numpy as np
import matplotlib
import scipy.linalg as lin
import matplotlib.pyplot as plt

class FDMSteadyFlow2D:
  def __init__(self, Nx, Ny, h_top):
    self.Nx = Nx
    self.Ny = Ny
    self.h_top = h_top

  def buildCoeffMatrix(self):
    '''
    Constructs the coefficient matrix A of the final linear
    system of equations of the form Ax = b
    '''
    # Create the diagonal, upper and lower components of B
    Bdiag  = -4 * np.eye(self.Nx - 1)
    Bupper = np.diag([1] * (self.Nx - 2), 1)
    Blower = np.diag([1] * (self.Nx - 2), -1)

    # Add components to create B
    B = Bdiag + Bupper + Blower

    # Create a block matrix where the diagonals are each B
    Bs = [B] * (self.Nx - 1)
    A  = lin.block_diag(*Bs)

    # Create the identity diagonals
    I = np.ones((self.Nx - 1) * (self.Nx - 2))
    Iupper = np.diag(I, self.Nx - 1)
    Ilower = np.diag(I, -self.Nx + 1)

    # Add the identity diagonal to A to complete it
    A += Iupper + Ilower

    return A

  def buildRHSVector(self):
    '''
    Constructs the right hand side vector b of the final linear
    system of equations of the form
    '''
    b = np.zeros((self.Nx - 1)**2)
    b[-self.Nx+1:] = -self.h_top

    return b

  def solveLinearSystem(self, A, b):
    '''
    Solves the final linear system Ax = b and concatenates the
    boundary conditions (BCs) to the solution
    '''
    # Solve for h vector and reshape array to 2D
    h = lin.solve(A, b)
    h = h.reshape((self.Nx - 1, self.Ny - 1))

    # Create empty 2D array with all nodes and insert BCs ans solution
    h2D  = np.zeros((self.Nx + 1, self.Ny + 1))
    h2D[0] = self.h_top         # Insert top BC
    h2D[1:-1,1:-1] = h[::-1]    # Insert solution (::-1 => inverted)

    return h2D

  def plotSolution(self, h2D):
    '''
    Plots the color plot of the solution on a 2D meshgrid
    '''
    # Create 1D arrays with number of nodes
    x = np.linspace(0, 1, self.Nx + 1)
    y = np.linspace(1, 0, self.Ny + 1)

    # Create 2D mesh grid
    X, Y = np.meshgrid(x, y)

    # Plot solution on mesh grid
    matplotlib.rcParams['figure.figsize'] = 6.2, 5
    #plt.clf()
    plt.contourf(X, Y, h2D, 10)
    plt.colorbar()
    plt.xlabel(r'$x$ [$\mathrm{m}$]')
    plt.ylabel(r'$y$ [$\mathrm{m}$]')
    #plt.savefig('2D_Flow_Nx_Ny_' + str(Nx) + '.eps')

if __name__ == "__main__":
  fdm = FDMSteadyFlow2D(Nx=20, Ny=20, h_top=10)
  A = fdm.buildCoeffMatrix()
  b = fdm.buildRHSVector()
  h = fdm.solveLinearSystem(A, b)
  fdm.plotSolution(h)