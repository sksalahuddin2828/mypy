import numpy as np
import plotly.graph_objs as go
import sympy as sp

# Step 1: Deriving the Wave Speed Equation
v, FT, mu = sp.symbols('v FT mu')
wave_speed_equation = sp.sqrt(FT / mu)

# Step 2: Calculating Wave Speed
tension_values = np.linspace(1, 200, 100)
linear_density_values = np.linspace(0.01, 0.2, 100)

tension_mesh, linear_density_mesh = np.meshgrid(tension_values, linear_density_values)
wave_speed_values = np.sqrt(tension_mesh / linear_density_mesh)

# Create a 3D surface plot using Plotly
surface = go.Surface(
    x=tension_mesh, y=linear_density_mesh, z=wave_speed_values,
    colorscale='Viridis', colorbar_title='Wave Speed',
    lighting=dict(ambient=0.4),
)

layout = go.Layout(title='Wave Speed vs Tension and Linear Density',
                   scene=dict(
                       xaxis_title='Tension (FT)',
                       yaxis_title='Linear Density (mu)',
                       zaxis_title='Wave Speed (v)',
                       aspectmode='data',
                       bgcolor='#f0f0f0'  # Set background color
                   ),
                   margin=dict(l=0, r=0, b=0, t=80))

# Adding the 3D surface plot
fig = go.Figure(data=[surface], layout=layout)
fig.update_layout(scene_aspectmode='data')
fig.update_layout(scene_zaxis_type='log')  # Adjust the z-axis to log scale

# Animation frames
frames = []
for i in range(len(tension_values)):
    frame = go.Frame(data=[go.Surface(
        x=tension_mesh, y=linear_density_mesh, z=wave_speed_values,
        colorscale='Viridis', colorbar_title='Wave Speed',
        surfacecolor=wave_speed_values[:i+1, :],
        lighting=dict(ambient=0.4),
    )])
    frames.append(frame)

# Slider for animation
slider = {
    'steps': [
        {'args': [[f'frame{i+1}']], 'label': str(i+1), 'method': 'animate'}
        for i in range(len(tension_values))
    ],
    'active': 0,
    'transition': {'duration': 300, 'easing': 'cubic-in-out'},
}

fig.frames = frames
fig.update_layout(updatemenus=[{
    'buttons': [
        {'args': [None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}],
         'label': 'Play', 'method': 'animate'},
        {'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}],
         'label': 'Pause', 'method': 'animate'},
    ],
    'direction': 'left', 'pad': {'r': 10, 't': 87}, 'showactive': False,
    'type': 'buttons', 'x': 0.1, 'xanchor': 'right', 'y': 0, 'yanchor': 'top'
}], sliders=[slider])

# Show the plot
fig.show()
