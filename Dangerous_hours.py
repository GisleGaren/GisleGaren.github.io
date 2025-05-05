import numpy as np
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# Get the current working directory (Jupyter-compatible)
current_dir = os.getcwd()

# Then continue as normal
# Update the path to the correct location of the parquet file
parquet_path = os.path.join(current_dir, 'optimized_datasets', 'vehicle_crashes_cleaned.parquet')


# Read the parquet file
df = pd.read_parquet(parquet_path)

# Convert CRASH TIME to datetime and combine with CRASH DATE
df['timestamp'] = df['CRASH DATE'] + pd.to_timedelta(df['CRASH TIME'].str.split(':').str[0].astype(int), unit='h')
df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.day_name()

# Group the data for plotting
collision_counts = df.groupby(['day_of_week', 'hour']).size().reset_index(name='collisions')

# Reorder days of the week for consistency
collision_counts['day_of_week'] = pd.Categorical(
    collision_counts['day_of_week'],
    categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    ordered=True
)

# Create interactive bar chart using Plotly
fig = px.bar(
    collision_counts,
    x='hour',
    y='collisions',
    color='day_of_week',
    color_discrete_sequence=px.colors.qualitative.Set1,
    barmode='group',
    labels={'collisions': 'Number of Collisions', 'hour': 'Hour of Day'},
    title='Interactive Collision Frequency by Hour and Day of Week',
    height=600,
    width=1000
)

fig.update_layout(
    xaxis=dict(tickmode='linear'),
    legend_title_text='Day of Week'
)

# Create the 'assets' directory inside the GitHub Pages site if it doesn't exist
assets_dir = os.path.join(current_dir, 'GisleGaren.github.io', 'assets')
os.makedirs(assets_dir, exist_ok=True)

# Define output HTML path
output_path = os.path.join(assets_dir, 'dangerous_hours_plot.html')

# Save the Plotly chart as an interactive HTML file
fig.write_html(output_path, include_plotlyjs='cdn')

# Optionally show the chart during development
fig.show()