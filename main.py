from flask import Flask, render_template
from grafy import grafy
import random
app = Flask(__name__)


# Temp data z db
sensors = ["sensor1", "sensor2", "sensor3", "sensor4", "sensor5", "sensor6"]
events_per_sensor = [random.randint(1, 100) for _ in sensors]

# temp data i pro láďu
timestamps = ["2024-05-24T21:14:30", "2024-05-24T21:14:31", "2024-05-24T21:14:32", "2024-05-24T21:14:33", "2024-05-24T21:14:34", "2024-05-24T21:14:35"]
messages_per_second = [10, 12, 8, 15, 11, 14]
data_flow_bps = [8000, 9500, 7000, 12000, 8500, 11000]


@app.route('/') 
def domov():
    fig_in_time_s = grafy.time_series_chart(timestamps, messages_per_second,'Časová řada [s]').to_html(full_html=False)
    fig_in_time_h = grafy.time_series_chart(timestamps, messages_per_second,'Časová řada [h]').to_html(full_html=False)
    fig_bar_sensor = grafy.bar_chart(sensors, events_per_sensor,'Senzory').to_html(full_html=False)
    return render_template('home.html', plot_in_time_s=fig_in_time_s, plot_in_time_h=fig_in_time_h, plot_bar_sensor=fig_bar_sensor)


@app.route('/grafy')
def graf():
    # temp data na test
    fig_scatter = grafy.scatter_plot(timestamps, messages_per_second,'Bodov graf').to_html(full_html=False)
    fig_bar = grafy.bar_chart(timestamps, data_flow_bps,'Sloupcov graf').to_html(full_html=False)
    return render_template('grafy.html', plot_scatter=fig_scatter, plot_bar=fig_bar)


if __name__ == '__main__':
    app.run(debug=True)
