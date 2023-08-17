import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Interactive User Input
x = sp.Symbol('x')
a = float(input("Enter the value of 'a': "))
f_x = input("Enter the function f(x): ")

# Define the Function and its Differentiation
f = a * sp.sympify(f_x)
f_prime = sp.diff(f, x)

# Create Numeric Functions for Plotting
f_numeric = sp.lambdify(x, f, 'numpy')
f_prime_numeric = sp.lambdify(x, f_prime, 'numpy')

# Create Visualization
x_vals = np.linspace(-10, 10, 400)
y_vals_f = f_numeric(x_vals)
y_vals_f_prime = f_prime_numeric(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals_f, label='$af(x)$', color='blue')
plt.plot(x_vals, y_vals_f_prime, label='$a\\frac{df(x)}{dx}$', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Visualization of $af(x)$ and $a\\frac{df(x)}{dx}$')
plt.legend()
plt.grid()
plt.show()
