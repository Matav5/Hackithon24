#Zde by měly být funkce a pomocné funkce na vizualizaci grafů
import plotly.graph_objects as go
import plotly.express as px
import json
import pandas as pd
import numpy as np
import os 


def scatter_plot(x_categories, y_values, title):
    fig = go.Figure(data=[go.Scatter(x=x_categories, y=y_values, mode='markers')])
    fig.update_layout(title=title, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    return fig


def area_chart(x_categories, y_values, title):
    fig = go.Figure(data=[go.Scatter(x=x_categories, y=y_values, fill='tozeroy')])
    fig.update_layout(title=title, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    return fig


def pie_chart(labels, values, title):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title=title, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    return fig


def time_series_chart(timestamps, throughput_values, title):
    fig = go.Figure(data=[go.Scatter(x=timestamps, y=throughput_values, mode='lines')])
    fig.update_layout(title=title, xaxis_title='Čas', yaxis_title='Throughput (jednotky/s)', plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    return fig


def bar_chart(x_categories, y_values, title):
    fig = go.Figure(data=[go.Bar(x=x_categories, y=y_values)])
    fig.update_layout(title=title, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    return fig

