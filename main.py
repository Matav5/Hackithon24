from flask import Flask, render_template, request
from flask_socketio import SocketIO
import random
from apscheduler.schedulers.background import BackgroundScheduler
from grafy import grafy

app = Flask(__name__)

sensors = ["sensor1", "sensor2", "sensor3", "sensor4", "sensor5", "sensor6"]
timestamps = ["2024-05-24T21:14:30", "2024-05-24T21:14:31", "2024-05-24T21:14:32", "2024-05-24T21:14:33", "2024-05-24T21:14:34", "2024-05-24T21:14:35"]

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
    fig_scatter = grafy.scatter_plot(timestamps, messages_per_second,'Bodov graf').to_html(full_html=False)
    fig_bar = grafy.bar_chart(timestamps, data_flow_bps,'Sloupcov graf').to_html(full_html=False)
    return render_template('grafy.html', plot_scatter=fig_scatter, plot_bar=fig_bar)

@app.route('/filter', methods=['GET', 'POST'])
def filter(): 
    topics = {
        "topic1": ["category1", "category2", "category3"],
        "topic2": ["category1", "category2", "category3"],
        "topic3": ["category1", "category2"]
    }
    if request.method == 'POST':
        selected_topic = request.form['topic']
        selected_category = request.form['category']
        # Process the selected topic and category as needed
        # For example, filter data based on these selections
        #return render_template('results.html', selected_topic=selected_topic, selected_category=selected_category)
        pass
    else:
        return render_template('filter.html', topics=topics)



if __name__ == '__main__':
    app.run(debug=True)
