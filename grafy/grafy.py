#Zde by měly být funkce a pomocné funkce na vizualizaci grafů
import plotly.graph_objects as go
import plotly.express as px
import json
import pandas as pd
import numpy as np
import os 

def scatter_plot(x_categories, y_values, title='Bodový graf'):
    fig = go.Figure(data=[go.Scatter(x=x_categories, y=y_values, mode='markers')])
    fig.update_layout(title=title)
    return fig

def area_chart(x_categories, y_values, title='Plošný graf'):
    fig = go.Figure(data=[go.Scatter(x=x_categories, y=y_values, fill='tozeroy')])
    fig.update_layout(title=title)
    return fig

def pie_chart(labels, values, title='Koláčový graf'):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title=title)
    return fig

def time_series_chart(timestamps, throughput_values, title='Časový graf throughputu'):
    fig = go.Figure(data=[go.Scatter(x=timestamps, y=throughput_values)])
    fig.update_layout(title=title, xaxis_title='Čas', yaxis_title='Throughput (jednotky/s)')
    return fig

def bar_chart(x_categories, y_values, title='Sloupcový graf'):
    fig = go.Figure(data=[go.Bar(x=x_categories, y=y_values)])
    fig.update_layout(title=title)
    return fig

