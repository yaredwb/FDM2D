---
layout: default
---
### **Governing Equation**

Steady-state groundwater flow in two-dimensions is governed by the differential equation

$$
k_x \frac{\partial^2 h}{\partial x^2} + k_y \frac{\partial^2 h}{\partial y^2} = Q
$$

where the parameters are as described in the one-dimensional case. If the permeability is assumed to be isotropic, i.e. $$ k_x = k_y = k $$, and if source/sink terms are ignored in the flow domain, we get 

$$
\frac{\partial^2 h}{\partial x^2} + \frac{\partial^2 h}{\partial y^2} = 0
$$
which is a form of the well-know Laplace equation.

### Spatial Discretization

The first step is to spatially discretize the domain over which we aim to solve the problem and define the boundary conditions. A typical 2D discretization is shown in the figure below where the two-dimensional domain is discretized with a uniform grid mesh i.e. $$ \Delta x = \Delta y $$.

![2D grid](assets/images/2D_grid.png)

This is achieved by dividing the $$ x $$ and $$ y $$ directions into $$ N_x $$ and $$ N_y $$ number of elements, where for a square domain we have $$ N = N_x = N_y $$. In general, if $$ L_x $$ and $$ L_y $$ represent the dimensions in the $$ x $$ and $$ y $$ directions, we have

$$
\Delta x = \frac{L_x}{N_x} \quad \text{and} \quad \Delta y = \frac{L_y}{N_y} 
$$

The hydraulic head value at a given point in the domain, say $$ (x_i,y_j) $$, is represented by

$$
h(x_i,y_j) = h_{i,j}  
$$

for $$ i=0,1,\cdots,N_x $$ and $$ j=0,1,\cdots,N_y $$. The boundary conditions are specified on some edges of the domain. For example, if the head values are known to be $$ \bar{h}_1 $$ along $$ x=0 $$ and $$ x=L_x $ and $ \bar{h}_2 $$ along $$ y=0 $$ and $$ y=L_y $$, we write

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

#### Solution for $$ N_x = N_y = 4 $$

Consider a $$ 1~\mathrm{m} \times 1~\mathrm{m} $$ grid divided into an equal number of elements $$ N_x = N_y = 4 $$ in both directions ($$ N_x+1 = N_y+1 = 5 $$ nodes in both directions) as shown in the figure below. The grid involves 25 nodes which are numbered as shown in the figure.

-> ![2D 4x4 grid](assets/images/2D_4x4_grid.png) <-

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