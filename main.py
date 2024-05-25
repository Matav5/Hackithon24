from flask import Flask, render_template,request
from flask_socketio import SocketIO
import random
from apscheduler.schedulers.background import BackgroundScheduler
from grafy import grafy
import data.zpracovani as zprac
from datetime import timedelta,timezone,datetime
import sys

app = Flask(__name__)

sensors = ["sensor1", "sensor2", "sensor3", "sensor4", "sensor5", "sensor6"]
timestamps = ["2024-05-24T21:14:30", "2024-05-24T21:14:31", "2024-05-24T21:14:32", "2024-05-24T21:14:33", "2024-05-24T21:14:34", "2024-05-24T21:14:35"]

def update_data(od=None):
    print('Update...')
    if od is None:
        od = datetime.now(tz=timezone.utc) - timedelta(minutes=25)

    throughput = zprac.get_throughput(od)
    
    events_per_sensor = throughput[["timestamp", "messages_per_second"]].copy()
    messages_per_second = throughput[["timestamp", "messages_per_second"]].copy()
    data_flow_bps =throughput[["timestamp", "throughput_per_second"]].copy() 
    
    print(events_per_sensor.head())
    print(messages_per_second.head())
    print(data_flow_bps.head())
   

    # generování HTML grafů


    return messages_per_second, data_flow_bps, events_per_sensor

@app.route('/api/data', methods=['GET'])
def api_data():
    date = request.args.get('date')

    messages_per_second, data_flow_bps, events_per_sensor = update_data(date)
    
    return {
        'plot_in_time_s': messages_per_second.to_json(),
        'plot_in_time_h': data_flow_bps.to_json(),
        'plot_bar_sensor': events_per_sensor.to_json(),
        'datum': datetime.now(tz=timezone.utc).isoformat()
    }
@app.route('/')
def home():
    
    messages_per_second, data_flow_bps, events_per_sensor = update_data()
    
    
    plot_in_time_s = grafy.scatter_plot(messages_per_second["timestamp"], messages_per_second["messages_per_second"], 'Messages Per Second').to_html(full_html=False)
    plot_in_time_h = grafy.area_chart(data_flow_bps["timestamp"], data_flow_bps["throughput_per_second"], 'Data Flow in bps').to_html(full_html=False)
    plot_bar_sensor = grafy.bar_chart(events_per_sensor["timestamp"],events_per_sensor["messages_per_second"], 'Events Per Sensor').to_html(full_html=False)
    
    return render_template('home.html', plot_in_time_s=plot_in_time_s, plot_in_time_h=plot_in_time_h, plot_bar_sensor=plot_bar_sensor,datum=datetime.now(tz=timezone.utc))


# stránka na grafy - zaměřené pro jiné values
@app.route('/grafy')
def graf():
    # temp data na test
    fig_scatter = grafy.scatter_plot(timestamps, messages_per_second,'Bodov graf').to_html(full_html=False)
    fig_bar = grafy.bar_chart(timestamps, data_flow_bps,'Sloupcov graf').to_html(full_html=False)
    return render_template('grafy.html', plot_scatter=fig_scatter, plot_bar=fig_bar)

if __name__ == '__main__':
    app.run(debug=True)
  