import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit
from scipy.optimize import least_squares

# Load the data
data = pd.read_csv("bungdrp table test.csv")  # Replace with your CSV file
x = data['Mass'].values  # Replace with your own titles
y = data['Drop_Height'].values # Replace with your own titles
z = data['Cord_Length'].values # Replace with your own titles

# Define the quadratic model function
def model_func(xy, a, b, c, d, e, f):
    x, y = xy
    return a * (x**2) + b * x * y + c * (y**2) + d * x + e * y + f

# Define the residuals function
def residuals(params, xy_data, z_actual):
    x, y = xy_data
    z_pred = model_func((x, y), *params)
    return z_actual - z_pred

# Regularized residuals to prevent overfitting
def regularized_residuals(params, xy_data, z_actual, alpha=0.1):
    x, y = xy_data
    z_pred = model_func((x, y), *params)
    regularization = alpha * np.sum(np.array(params)**2)  # L2 regularization term
    return z_actual - z_pred + regularization

# Prepare the input data for fitting
xy_data = np.vstack((x, y))

# Initial guess for parameters
initial_guess = [1, 1, 1, 1, 1, 1]

# Perform least-squares fitting with regularization
result = least_squares(regularized_residuals, initial_guess, args=(xy_data, z))
params = result.x

# Extract fitted parameters
a, b, c, d, e, f = params
print(f"Fitted equation: z = {a:.5f}x^2 + {b:.5f}xy + {c:.5f}y^2 + {d:.5f}x + {e:.5f}y + {f:.5f}")

# Calculate predictions and clip negative values
z_pred = model_func((x, y), *params)
z_pred_clipped = np.clip(z_pred, 0, None)

# Calculate R² value
ss_total = np.sum((z - np.mean(z))**2)
ss_residual = np.sum((z - z_pred_clipped)**2)
r_squared = 1 - (ss_residual / ss_total)
print(f"R²: {r_squared:.3f}")

# The rest is just graphing

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x, y, z, color='blue', label='Original Data')

x_grid = np.linspace(min(x), max(x), 30)
y_grid = np.linspace(min(y), max(y), 30)
x_mesh, y_mesh = np.meshgrid(x_grid, y_grid)
z_mesh = model_func((x_mesh, y_mesh), *params)
z_mesh_clipped = np.clip(z_mesh, 0, None)


ax.plot_surface(x_mesh, y_mesh, z_mesh_clipped, alpha=0.5, cmap='viridis')

ax.set_xlabel('Mass (g)')
ax.set_ylabel('Drop Height (cm)')
ax.set_zlabel('Cord Length (cm)')


ax.legend()
plt.show()