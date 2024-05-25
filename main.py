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
        topic_form = request.form['topic']
        
        start_date_dt = datetime.fromisoformat(start_date)
        end_date_dt = datetime.fromisoformat(end_date)

        # datetime picker -> str -> datetime
        start_date_formatted = start_date_dt.strftime('%Y, %m, %d, %H, %M')
        end_date_formatted = end_date_dt.strftime('%Y, %m, %d, %H, %M')
        print(start_date_formatted)
        print(end_date_formatted)
        print(topic_form)
        # dořešit možnou 0 na datumu nebo dni - pokud len(datum/mesic) neni 2

        # Získej data podle formuláře:
        

        return render_template('filter.html', topics=topics, start_date=start_date_formatted, end_date=end_date_formatted)
    else:
        return render_template('filter.html', topics=topics)



if __name__ == '__main__':
    app.run(debug=True)
  