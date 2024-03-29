---
layout: default
title: Finite Difference Method
---
Code and excerpt from lecture notes demonstrating application of the finite difference method (FDM) to steady-state flow in two dimensions. The extracted lecture note is taken from a course I taught entitled Advanced Computational Methods in Geotechnical Engineering.

### **Governing Equation**

Steady-state groundwater flow in two-dimensions is governed by the differential equation

$$
k_x \frac{\partial^2 h}{\partial x^2} + k_y \frac{\partial^2 h}{\partial y^2} = Q
$$

where $$ k_x $$ and $$ k_y $$ are the hydraulic conductivities in the $$ x $$ and $$ y $$ directions, respectively,  $$ h $$ is the hydraulic head and $$ Q $$ represents source/sink in the flow domain. If the hydraulic conductivity is assumed to be isotropic, i.e. $$ k_x = k_y = k $$, and if source/sink terms are ignored in the flow domain, we get

$$
\frac{\partial^2 h}{\partial x^2} + \frac{\partial^2 h}{\partial y^2} = 0
$$

which is a form of the well-know Laplace equation.

### **Spatial Discretization**

The first step is to spatially discretize the domain over which we aim to solve the problem and define the boundary conditions. A typical 2D discretization is shown in the figure below where the two-dimensional domain is discretized with a uniform grid mesh i.e. $$ \Delta x = \Delta y $$.

![2D grid](assets/images/2D_grid.png){: .center-image }
*FDM 2D grid*

This is achieved by dividing the $$ x $$ and $$ y $$ directions into $$ N_x $$ and $$ N_y $$ number of elements, where for a square domain we have $$ N = N_x = N_y $$. In general, if $$ L_x $$ and $$ L_y $$ represent the dimensions in the $$ x $$ and $$ y $$ directions, we have

$$
\Delta x = \frac{L_x}{N_x} \quad \text{and} \quad \Delta y = \frac{L_y}{N_y}
$$

The hydraulic head value at a given point in the domain, say $$ (x_i,y_j) $$, is represented by

$$
h(x_i,y_j) = h_{i,j}
$$

for $$ i=0,1,\cdots,N_x $$ and $$ j=0,1,\cdots,N_y $$. The boundary conditions are specified on some edges of the domain. For example, if the head values are known to be $$ \bar{h}_1 $$ along $$ x=0 $$ and $$ x=L_x $$ and $$ \bar{h}_2 $$ along $$ y=0 $$ and $$ y=L_y $$, we write

$$
h_{0,j} = h_{N,j} = \bar{h}_1 \quad \text{and} \quad h_{i,0} = h_{i,N} = \bar{h}_2
$$

The next step is to approximate the partial derivatives in terms of difference equations. The finite difference approximations of the derivatives are given by

$$
\begin{align}
\frac{\partial^2 h}{\partial x^2} &= \frac{h_{i+1,j} - 2h_{i,j} + h_{i-1,j}}{\Delta x^2} \nonumber \\
\frac{\partial^2 h}{\partial y^2} &= \frac{h_{i,j+1} - 2h_{i,j} + h_{i,j-1}}{\Delta y^2}
\end{align}
$$

Using these in simplified governing equation gives

$$
\frac{h_{i+1,j} - 2h_{i,j} + h_{i-1,j}}{\Delta x^2} + \frac{h_{i,j+1} - 2h_{i,j} + h_{i,j-1}}{\Delta y^2} = 0
$$

For a uniform mesh size where $$ \Delta x = \Delta y $$, we get

$$
h_{i,j-1} + h_{i-1,j} - 4h_{i,j} + h_{i+1,j}  + h_{i,j+1} = 0
$$

This equation is represented by the five-point stencil with the highlighted nodes in the  previous figure. It implies that the hydraulic head at point $$ (x_i,y_j) $$ is obtained by averaging the values of neighboring points. The system of equation can now be derived for arbitrarily chosen grid mesh.

#### **Solution for $$ N_x = N_y = 4 $$**

Consider a $$ 1~\mathrm{m} \times 1~\mathrm{m} $$ grid divided into an equal number of elements $$ N_x = N_y = 4 $$ in both directions ($$ N_x+1 = N_y+1 = 5 $$ nodes in both directions) as shown in the figure below. The grid involves 25 nodes which are numbered as shown in the figure.

![2D 4x4 grid](assets/images/2D_4x4_grid.png){: .center-image }
*2D grid for $$N_x=N_y=4$$*

Let's assume that the following boundary conditions are defined for the hydraulic head (in arbitrary units):

$$
\begin{alignat}{2}
h &= 10 \qquad &&\text{for} \; y = 1 \nonumber \\
h &= 0 \qquad &&\text{for} \; x=0, x=1 \, \text{and} \, y = 0
\end{alignat}
$$

The boundary conditions imply the hydraulic head values are $$ h = 0 $$ for nodes $$ 1,2,3,4,5,6,10,11,15,16~\text{and}~20 $$ and $$ h = 10 $$ for nodes $$ 21,22,23,24~\text{and}~25 $$. The unknown nodes are $$ 7,8,9,12,13,14,17,18~\text{and}~19 $$. The finite difference equations at these unknown nodes can now be written based on the difference equation obtained earlier and according to the 5 point stencil illustrated.

- For nodes 7, 8 and 9

  $$
  \begin{align}
	-4h_7 + h_8 + h_{12} &= 0 \\
	h_7 - 4h_8 + h_9 + h_{13} &= 0 \\
	h_8 - 4h_9 + h_{14} &= 0
	\end{align}
  $$

- For nodes 12, 13 and 14

  $$
  \begin{align}
	h_7 - 4h_{12} + h_{13} + h_{17} &= 0 \\
	h_8 + h_{12} - 4h_{13} + h_{14} + h_{18} &= 0 \\
	h_9 + h_{13} - 4h_{14} + h_{19} &= 0
	\end{align}
  $$

- For nodes 17, 18 and 19

  $$
  \begin{align}
	h_{12} - 4h_{17} + h_{18} &= -10 \\
	h_{13} + h_{17} - 4h_{18} + h_{19} &= -10 \\
	h_{14} + h_{18} - 4h_{19} &= -10
	\end{align}
  $$

The 9 equations for the 9 unknowns can be written in matrix form as

$$
\left[ \begin{array}{ccc|ccc|ccc}
-4 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
1 & -4 & 1 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 1 & -4 & 0 & 0 & 1 & 0 & 0 & 0 \\
\hline
1 & 0 & 0 & 1 & -4 & 0 & 1 & 0 & 0 \\
0 & 1 & 0 & 1 & -4 & 1 & 0 & 1 & 0 \\
0 & 0 & 1 & 0 & 1 & -4 & 0 & 0 & 1 \\
\hline
0 & 0 & 0 & 1 & 0 & 0 & -4 & 1 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 & 1 & -4 & 1 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & -4 \\
\end{array} \right]
\left\lbrace
\begin{matrix}
h_7 \\ h_8 \\ h_9 \\ h_{12} \\ h_{13} \\ h_{14} \\ h_{17} \\ h_{18} \\ h_{19}
\end{matrix}
\right\rbrace =
\left\lbrace
\begin{matrix}
0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ -10 \\ -10 \\ -10
\end{matrix}
\right\rbrace
$$

which is a linear system of the form $$ \mathbf A \mathbf x = \mathbf b $$. A closer inspection of the coefficient matrix $$ \mathbf A $$ shows that it has a block matrix structure of the form

$$
\mathbf A =\left[ \begin{array}{c|c|c}
\mathbf D & \mathbf I & \textbf{O} \\
\hline
\mathbf I & \mathbf D & \mathbf I \\
\hline
\textbf{O} & \mathbf I & \mathbf D \\
\end{array} \right]
$$

where

$$
\mathbf D = \left[ \begin{array}{ccc}
-4 & 1 & 0 \\
1 & -4 & 1 \\
0 & 1 & -4
\end{array} \right] \qquad \text{and} \qquad
\mathbf I = \left[ \begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array} \right]
$$

and $$ \textbf{O} $$ is a zero matrix.

The coefficient matrix $$ \mathbf A $$ is constructed in Python using various methods from the `numpy` and `scipy` modules. An excerpt from the code that builds the coefficient matrix is shown below.

```python
def buildCoeffMatrix(self):
    Ddiag  = -4 * np.eye(self.Nx - 1)
    Dupper = np.diag([1] * (self.Nx - 2), 1)
    Dlower = np.diag([1] * (self.Nx - 2), -1)
    D = Bdiag + Bupper + Blower
    Ds = [D] * (self.Nx - 1)
    A  = lin.block_diag(*Ds)
    I = np.ones((self.Nx - 1) * (self.Nx - 2))
    Iupper = np.diag(I, self.Nx - 1)
    Ilower = np.diag(I, -self.Nx + 1)
    A += Iupper + Ilower
    return A
```

The right hand side vector is constructed similarly.

```python
def buildRHSVector(self):
    b = np.zeros((self.Nx - 1)**2)
    b[-self.Nx+1:] = -self.h_top
    return b
```

The final linear system is solved using the `linalg` linear algebra module from `scipy`.

```python
def solveLinearSystem(self, A, b):
    h = lin.solve(A, b)
    h = h.reshape((self.Nx - 1, self.Ny - 1))
    h2D = np.zeros((self.Nx + 1, self.Ny + 1))
    h2D[0] = self.h_top
    h2D[1:-1,1:-1] = h[::-1]
    return h2D
```

Solving the system of equations above gives the solution vector

$$
\left\lbrace 0.71 \;\; 0.98 \;\; 0.71 \;\; 1.88 \;\; 2.50 \;\; 1.88 \;\; 4.29 \;\; 5.27 \;\; 4.29  \right\rbrace^\intercal
$$

Combining these values with the boundary conditions, the final nodal hydraulic heads can be written in full as

$$
\left[ \begin{matrix}
10 & 10 & 10 & 10 & 10 \\
0 & 4.29 & 5.27 & 4.29 & 0 \\
0 & 1.88 & 2.50 & 1.88 & 0 \\
0 & 0.71 & 0.98 & 0.71 & 0 \\
0 & 0 & 0 & 0 & 0
\end{matrix} \right]
$$

A two-dimensional color contour plot of this solution is shown in the figure below with 10 contour levels and and linear interpolation between neighboring nodes.

![Solution for a 4x4 grid](assets/images/Solution_for_4x4_grid.png){: .center-image }
*Solution for $$N_x=N_y=4$$*

#### **Solution for an $$ N_x \times N_y $$ grid**

In general, we want to obtain a solution on an arbitrarily discretized grid. Let the domain be discretized into $$ N_x \times N_y $$ elements ($$ (N_x + 1) \times (N_y + 1) $$ nodes) where $$ N_x $$ and $$ N_y $$ are chosen such that $$ \Delta x = \Delta y $$ i.e. a uniform grid. The coefficient matrix $$ \mathbf A $$ will have a similar block structure as described in the previous section but with more element matrices $$ \mathbf B $$ and $$ \mathbf I $$. The size of matrix $$ \mathbf A $$ will be $$ (N_x-1)^2 \times (N_y-1)^2 $$ and its block form may be written as

$$
\mathbf A = \left[ \begin{array}{c|c|c|c|c}
\mathbf D & \mathbf I & \textbf{O} & \cdots & \textbf{O} \\
\hline
\mathbf I & \mathbf D & \mathbf I & \ddots & \vdots \\
\hline
\textbf{O} & \mathbf I & \ddots & \ddots & \textbf{O} \\
\hline
\vdots & \ddots & \ddots & \mathbf D & \mathbf I \\
\hline
\textbf{O} & \cdots & \textbf{O} & \mathbf I & \mathbf D \\
\end{array} \right]
$$

The sizes of the matrices $$ \mathbf B $$ and $$ \mathbf I $$ change depending on the selected $$ N_x $$ and $$ N_y $$ values. For the particular example considered here where the boundary conditions are known along the four boundaries, the matrices $$ \mathbf B $$ and $$ \mathbf I $$ will have sizes of $$ (N_x - 1) \times (N_y - 1) $$ and may be written as

$$
\mathbf D = \left[ \begin{array}{ccccc}
-4 & 1 & 0 & \cdots & 0 \\
1 & -4 & 1 & \ddots  & \vdots  \\
0 & \ddots & \ddots & \ddots & 0 \\
\vdots & \ddots & 1 & -4 & 1 \\
0 & \cdots & 0 & 1 & -4
\end{array} \right] \quad \text{and} \quad
\mathbf I = \left[ \begin{array}{ccccc}
1 & 0 & \cdots & \cdots & 0 \\
0 & 1 & \ddots &  & \vdots \\
\vdots & \ddots & \ddots & \ddots & \vdots \\
\vdots &  & \ddots & 1 & 0 \\
0 & \cdots & \cdots & 0 & 1
\end{array} \right]
$$

The right hand side vector $$ \mathbf b $$ will have a size of $$ (N_x-1)^2 $$ for this particular case. Following a similar node numbering convention as described earlier, the vector $$ \mathbf b $$ may be written as

$$
\mathbf b = \left\lbrace \begin{matrix}
0 & 0 & \cdots & 0 & -10 & \cdots & -10
\end{matrix} \right\rbrace^\intercal
$$

where $$ (N_x + 1) $$ nodes at the top boundary have a hydraulic head value of $$ h=10 $$. With $$ \mathbf A $$ and $$ \mathbf b $$ constructed for given $$ N_x $$ and $$ N_y $$ values, the linear system can be solved for the hydraulic heads at the unknown nodes. The follwing figures show the color contour plots for grid sizes of $$ 10 \times 10 $$, $$ 50 \times 50 $$ and $$ 100 \times 100 $$, respectively.

We use `matplotlib` to plot the final solution on a 2D meshgrid.

```python
def plotSolution(self, h2D):
    x = np.linspace(0, 1, self.Nx + 1)
    y = np.linspace(1, 0, self.Ny + 1)
    X, Y = np.meshgrid(x, y)
    matplotlib.rcParams['figure.figsize'] = 6.2, 5
    plt.contourf(X, Y, h2D, 10)
    plt.colorbar()
    plt.xlabel(r'$x$ [$\mathrm{m}$]')
    plt.ylabel(r'$y$ [$\mathrm{m}$]')
```

![Solution for a 10x10 grid](assets/images/Solution_for_10x10_grid.png){: .center-image }
*Solution for $$N_x=N_y=10$$*

![Solution for a 50x50 grid](assets/images/Solution_for_50x50_grid.png){: .center-image }
*Solution for $$N_x=N_y=50$$*

![Solution for a 100x100 grid](assets/images/Solution_for_100x100_grid.png){: .center-image }
*Solution for $$N_x=N_y=100$$*
