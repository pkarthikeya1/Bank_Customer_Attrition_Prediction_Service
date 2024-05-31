import pandas as pd
import plotly.express as px

def plot_churned_unchurned(
    customers: pd.DataFrame,
    column_to_plot: str
    ):
  """
  Plots the counts of a categorical variable as a bar chart using Plotly.

  Args:
      customers (pandas.DataFrame): The DataFrame containing the categorical variable.
      category_column (str): The name of the column containing the categorical data.
  """

  # Count the occurrences of each category
  category_counts = customers[column_to_plot].value_counts()
  

  # Create the bar chart using px.bar
  fig = px.bar(category_counts, x=category_counts.index, y=category_counts.values, color={1:"Unchurned", 0:"Churned"})

  # Customize the chart (optional)
  fig.update_layout(title='Category Counts', xaxis_title=column_to_plot, yaxis_title='Count')

  # Display the chart
  return fig.show()
