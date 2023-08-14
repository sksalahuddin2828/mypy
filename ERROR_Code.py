import numpy as np
import pandas as pd
import sympy as sp
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from IPython.display import display, HTML
import time

# Function to solve quadratic equation
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if isinstance(discriminant, np.ndarray):
        roots = np.where(discriminant >= 0, (-b + np.sqrt(discriminant)) / (2*a), None)
    else:
        if discriminant < 0:
            return None
        else:
            roots = (-b + np.sqrt(discriminant)) / (2*a)
    return roots

# Create a blank figure
blank_fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])
blank_fig.update_layout(showlegend=False, xaxis_visible=False, yaxis_visible=False)

display(blank_fig)
time.sleep(1)  # Wait for 1 second

# Create a message to explain what's happening
explanation = go.Scatter(
    x=[],
    y=[],
    mode='text',
    text=['Let\'s visualize quadratic equations and their roots!'],
)
explanation_fig = go.Figure(data=[explanation])
explanation_fig.update_layout(showlegend=False, xaxis_visible=False, yaxis_visible=False)
display(explanation_fig)
time.sleep(3)  # Wait for 3 seconds

# Generate data for a, b, and c
a_list = np.linspace(-10, 10, 100)
b_list = np.linspace(-10, 10, 100)
a_grid, b_grid = np.meshgrid(a_list, b_list)
c_grid = -a_grid - b_grid

# Create dataframe for quadratic roots and coefficients
roots_data = []
equation_data = []

for a_val, b_val, c_val in zip(a_list, b_list, c_grid):
    roots = solve_quadratic(a_val, b_val, c_val)
    if roots is not None:
        roots_data.append({'a': a_val, 'b': b_val, 'c': c_val, 'roots': roots})
    
    x = sp.Symbol('x')
    equation = x**2 + b_val*x + c_val
    equation_data.append({'a': a_val, 'b': b_val, 'c': c_val, 'equation': equation})

df_roots = pd.DataFrame(roots_data)
df_equations = pd.DataFrame(equation_data)

# Create an animated scatter 3D plot
scatter_animation = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])
scatter_animation.update_layout(scene=dict(xaxis_title='a', yaxis_title='b', zaxis_title='Roots'))

for i in range(len(df_roots)):
    a_val = df_roots.loc[i, 'a']
    b_val = df_roots.loc[i, 'b']
    c_val = df_roots.loc[i, 'c']
    roots = solve_quadratic(a_val, b_val, c_val)
    
    if roots is not None:
        if isinstance(roots, tuple):
            scatter_animation.add_trace(go.Scatter3d(
                x=[a_val],
                y=[b_val],
                z=[roots[0]],
                mode='markers',
                marker=dict(size=8, color='red', opacity=0.8),
                name='Real Roots'
            ))
        else:
            scatter_animation.add_trace(go.Scatter3d(
                x=[a_val],
                y=[b_val],
                z=[roots],
                mode='markers',
                marker=dict(size=8, color='blue', opacity=0.8),
                name='Real Roots'
            ))

    display(scatter_animation)
    time.sleep(0.2)  # Wait for 0.2 seconds
    scatter_animation.data = []  # Clear the scatter plot for the next step

# Create a message to explain how the equations are formed
equation_explanation = go.Scatter(
    x=[],
    y=[],
    mode='text',
    text=['Now, let\'s explore how the equations are formed with b and c values.'],
)
equation_explanation_fig = go.Figure(data=[equation_explanation])
equation_explanation_fig.update_layout(showlegend=False, xaxis_visible=False, yaxis_visible=False)
display(equation_explanation_fig)
time.sleep(3)  # Wait for 3 seconds

# Create animated equations plot
equation_animation = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter', 'rowspan': 1}]])
equation_animation.update_layout(xaxis_title='x', yaxis_title='Equation Value')

for i in range(len(df_equations)):
    equation = df_equations.loc[i, 'equation']
    b_val = df_equations.loc[i, 'b']
    c_val = df_equations.loc[i, 'c']
    
    expression = equation.subs({sp.Symbol('b'): sp.Symbol('b_val'), sp.Symbol('c'): sp.Symbol('c_val')})
    func = sp.lambdify(sp.Symbol('x'), expression, "numpy")
    x_vals = np.linspace(-10, 10, 500)
    y_vals = func(x_vals)
    
    equation_animation.add_trace(go.Scatter(
        x=x_vals,
        y=y_vals,
        mode='lines',
        name=f'Equation for b={b_val}, c={c_val}'
    ))

    display(equation_animation)
    time.sleep(0.2)  # Wait for 0.2 seconds
    equation_animation.data = []  # Clear the equation plot for the next step

# Final message
final_explanation = go.Scatter(
    x=[],
    y=[],
    mode='text',
    text=['That\'s how you can creatively visualize quadratic equations and their roots using Plotly!'],
)
final_explanation_fig = go.Figure(data=[final_explanation])
final_explanation_fig.update_layout(showlegend=False, xaxis_visible=False, yaxis_visible=False)
display(final_explanation_fig)
time.sleep(3)  # Wait for 3 seconds
