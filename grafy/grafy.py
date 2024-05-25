import plotly.graph_objects as go
import numpy as np

# Data for the charts
timestamps = ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04']
throughput_values = [100, 120, 130, 110]
x_categories = ['A', 'B', 'C', 'D']
y_values = [10, 15, 13, 17]
labels = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [40, 30, 20, 10]
data = np.random.randn(1000)
z_values = np.random.rand(10, 10)
x_labels = list('ABCDEFGHIJ')
y_labels = list('abcdefghij')
treemap_labels = ['A', 'B', 'C', 'D', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2']
treemap_parents = ['', '', '', '', 'A', 'A', 'B', 'B', 'C', 'C']
treemap_values = [10, 20, 30, 40, 5, 5, 10, 10, 15, 15]

def scatter_plot(x_categories, y_values, title='Bodový graf', marker_size=15):
    fig = go.Figure(data=[go.Scatter(x=x_categories, y=y_values, mode='markers', 
                                     marker=dict(size=marker_size))])
    fig.update_layout(title=title, xaxis_title='Kategorie', yaxis_title='Hodnoty', 
                      yaxis=dict(gridcolor='lightgray'), plot_bgcolor='rgba(0,0,0,0)', 
                      paper_bgcolor='rgba(0,0,0,0)',
                      xaxis=dict(
            tickformat='%H:%M:%S'  # Format the x-axis to show only time
        ))
    return fig

def area_chart(x_categories, y_values, title='Plošný graf'):
    fig = go.Figure(data=[go.Scatter(x=x_categories, y=y_values, fill='tozeroy', 
                                     line=dict(color='royalblue'))])
    fig.update_layout(title=title, xaxis_title='Kategorie', yaxis_title='Hodnoty', 
                      yaxis=dict(gridcolor='lightgray'), plot_bgcolor='rgba(0,0,0,0)', 
                      paper_bgcolor='rgba(0,0,0,0)',
                      xaxis=dict(
            tickformat='%H:%M:%S'  # Format the x-axis to show only time
        ))
    return fig

def pie_chart(labels, values, title='Koláčový graf'):
    fig = go.Figure(data=[go.Pie(
        labels=labels, 
        values=values, 
        hole=.3,
        textinfo='label+percent',  # Display labels and percentages
        textposition='outside',  # Position labels outside the pie chart
        marker=dict(
            colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],  # Example colors
            line=dict(color='#FFFFFF', width=2)  # White border around segments
        ),
        textfont=dict(color='black')  # Set the label text color to black
    )])

    fig.update_layout(
        showlegend=False,  # Remove the legend
        plot_bgcolor='rgba(0,0,0,0)', 
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=60, b=0, l=0, r=0),  # Adjust top margin for the title
        annotations=[dict(
            text=title,
            x=0.05,  # Position near the left edge
            y=1.1,  # Position above the plot area
            xref='paper',
            yref='paper',
            font_size=20,
            showarrow=False
        )]
    )
    return fig

def time_series_chart(timestamps, throughput_values, title='Časový graf throughputu'):
    fig = go.Figure(data=[go.Scatter(x=timestamps, y=throughput_values, mode='lines+markers', 
                                     line=dict(color='firebrick', width=2))])
    fig.update_layout(title=title, xaxis_title='Čas', yaxis_title='Throughput (jednotky/s)', 
                      yaxis=dict(gridcolor='lightgray'), plot_bgcolor='rgba(0,0,0,0)', 
                      paper_bgcolor='rgba(0,0,0,0)',
                      xaxis=dict(
            tickformat='%H:%M:%S'  # Format the x-axis to show only time
        ))
    return fig

def bar_chart(x_categories, y_values, title='Sloupcový graf'):
    fig = go.Figure(data=[go.Bar(x=x_categories, y=y_values, marker_color='indianred')])
    fig.update_layout(
        title=title, 
        xaxis_title='Kategorie', 
        yaxis_title='Hodnoty', 
        yaxis=dict(gridcolor='lightgray'), 
        plot_bgcolor='rgba(0,0,0,0)', 
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            tickformat='%H:%M:%S'  # Format the x-axis to show only time
        )
    )
    return fig

def histogram(data, title='Histogram'):
    fig = go.Figure(data=[go.Histogram(x=data, marker=dict(color='rgba(100, 200, 102, 0.7)', 
                                                           line=dict(color='rgb(8, 48, 107)', width=1.5)))])
    fig.update_layout(title=title, xaxis_title='Hodnoty', yaxis_title='Počet', 
                      yaxis=dict(gridcolor='lightgray'), plot_bgcolor='rgba(0,0,0,0)', 
                      paper_bgcolor='rgba(0,0,0,0)')
    return fig

def treemap_chart(labels, parents, values, title='Treemap graf'):
    fig = go.Figure(go.Treemap(
        labels=labels,
        parents=parents,
        values=values,
        marker=dict(
            colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
        )
    ))

    fig.update_layout(
        title=title,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    return fig

def box_plot(data, title='Box plot'):
    fig = go.Figure(data=[go.Box(y=data, marker_color='darkblue')])
    fig.update_layout(
        title=title,
        yaxis_title='Hodnoty',
        yaxis=dict(gridcolor='lightgray'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    return fig
# Generate the figures
#scatter_fig = scatter_plot(x_categories, y_values)
#area_fig = area_chart(x_categories, y_values)
#pie_fig = pie_chart(labels, values)
#time_series_fig = time_series_chart(timestamps, throughput_values)
#bar_fig = bar_chart(x_categories, y_values)
#histogram_fig = histogram(data)


# Display the figures (in a Jupyter notebook, use .show())
#scatter_fig.show()
#area_fig.show()
#pie_fig.show()
#time_series_fig.show()
#bar_fig.show()
#histogram_fig.show()

