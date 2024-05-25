from flask import Flask, render_template, request
from flask_socketio import SocketIO
import random
from apscheduler.schedulers.background import BackgroundScheduler
from grafy import grafy
import numpy as np

app = Flask(__name__)

sensors = ["sensor1", "sensor2", "sensor3", "sensor4", "sensor5", "sensor6"]
timestamps = ["2024-05-24T21:14:30", "2024-05-24T21:14:31", "2024-05-24T21:14:32", "2024-05-24T21:14:33", "2024-05-24T21:14:34", "2024-05-24T21:14:35"]

treemap_labels = ['A', 'B', 'C', 'D', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2']
treemap_parents = ['', '', '', '', 'A', 'A', 'B', 'B', 'C', 'C']
treemap_values = [10, 20, 30, 40, 5, 5, 10, 10, 15, 15]
data = np.random.randn(1000)
labels = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [40, 30, 20, 10]


events_per_sensor = []
messages_per_second = []
data_flow_bps = []

def update_data():
    print('Update...')
    global events_per_sensor, messages_per_second, data_flow_bps
    events_per_sensor = [random.randint(1, 100) for _ in sensors]
    messages_per_second = [random.randint(5, 20) for _ in range(6)]
    data_flow_bps = [random.randint(5000, 15000) for _ in range(6)]
    
    print(events_per_sensor)
    print(messages_per_second)
    print(data_flow_bps)
    return events_per_sensor, messages_per_second, data_flow_bps

@app.route('/api/data')
def api_data():
    plot_in_time_s, plot_in_time_h, plot_bar_sensor = update_data()
    return {
        'plot_in_time_s': plot_in_time_s,
        'plot_in_time_h': plot_in_time_h,
        'plot_bar_sensor': plot_bar_sensor,
        'timestamps': ["2024-05-24T21:14:30", "2024-05-24T21:14:31", "2024-05-24T21:14:32", "2024-05-24T21:14:33", "2024-05-24T21:14:34", "2024-05-24T21:14:35"]
    }


@app.route('/')
def home():
    plot_in_time_s, plot_in_time_h, plot_bar_sensor = update_data()
    plot_in_time_s = grafy.time_series_chart(timestamps, plot_in_time_s, 'Časov graf - sekundy').to_html(full_html=False)
    plot_in_time_h = grafy.time_series_chart(timestamps, plot_in_time_h, 'Časov graf - hodiny').to_html(full_html=False)
    plot_bar_sensor = grafy.bar_chart(timestamps, plot_bar_sensor, 'Sloupcov graf - senzory').to_html(full_html=False)
    return render_template('home.html', plot_in_time_s=plot_in_time_s, plot_in_time_h=plot_in_time_h, plot_bar_sensor=plot_bar_sensor)


# stránka na grafy - zaměřené pro jiné values
@app.route('/grafy')
def graf():
    # temp data na test
    timestamps = ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04']
    messages_per_second = [100, 120, 130, 110]
    data_flow_bps = [200, 250, 300, 220]

    # Placeholder data for treemap and box plot
    treemap_labels = ['A', 'B', 'C', 'D', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2']
    treemap_parents = ['', '', '', '', 'A', 'A', 'B', 'B', 'C', 'C']
    treemap_values = [10, 20, 30, 40, 5, 5, 10, 10, 15, 15]
    data = np.random.randn(1000)

    fig_scatter = grafy.scatter_plot(timestamps, messages_per_second, 'Bodový graf').to_html(full_html=False)
    fig_bar = grafy.bar_chart(timestamps, data_flow_bps, 'Sloupcový graf').to_html(full_html=False)
    fig_time_series = grafy.time_series_chart(timestamps, messages_per_second, 'Časový graf throughputu').to_html(full_html=False)
    fig_box_plot = grafy.box_plot(data, 'Box plot').to_html(full_html=False)
    fig_treemap = grafy.treemap_chart(treemap_labels, treemap_parents, treemap_values, 'Treemap graf').to_html(full_html=False)

    return render_template('grafy.html', 
                           plot_scatter=fig_scatter, 
                           plot_bar=fig_bar,
                           plot_time_series=fig_time_series,
                           plot_box_plot=fig_box_plot,
                           plot_treemap=fig_treemap)


@app.route('/filter', methods=['GET', 'POST'])
def filter(): 
    topics = {
        "topic1": ["category1", "category2", "category3"],
        "topic2": ["category1", "category2", "category3"],
        "topic3": ["category1", "category2"]
    }
    if request.method == 'POST':
        from datetime import datetime

        start_date = request.form['start_date']
        end_date = request.form['end_date']
        
        start_date_dt = datetime.fromisoformat(start_date)
        end_date_dt = datetime.fromisoformat(end_date)

        # datetime picker -> str -> datetime
        start_date_formatted = start_date_dt.strftime('%Y, %m, %d, %H, %M')
        end_date_formatted = end_date_dt.strftime('%Y, %m, %d, %H, %M')
        print(start_date_formatted)
        print(end_date_formatted)
        # dořešit možnou 0 na datumu nebo dni - pokud len(datum/mesic) neni 2

        return render_template('filter.html', topics=topics, start_date=start_date_formatted, end_date=end_date_formatted)
    else:
        return render_template('filter.html', topics=topics)



if __name__ == '__main__':
    app.run(debug=True)
