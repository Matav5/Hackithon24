from flask import Flask, render_template
from grafy import grafy
import random
app = Flask(__name__)


# Temp data z db
timestamps = ["2024-05-24T21:14:30", "2024-05-24T21:14:31", "2024-05-24T21:14:32", "2024-05-24T21:14:33", "2024-05-24T21:14:34", "2024-05-24T21:14:35"]
messages_per_second = [10, 12, 8, 15, 11, 14]
data_flow_bps = [8000, 9500, 7000, 12000, 8500, 11000]


@app.route('/') 
def domov():
    return render_template('home.html')


@app.route('/grafy')
def graf():
    """
    x_values = [random.uniform(0, 500) for _ in range(10)]
    y_values = [random.uniform(0, 100) for _ in range(10)]
    """
    # temp data na test
    fig_scatter = grafy.scatter_plot(timestamps, messages_per_second).to_html(full_html=False)
    fig_bar = grafy.bar_chart(timestamps, data_flow_bps).to_html(full_html=False)
    return render_template('grafy.html', plot_scatter=fig_scatter, plot_bar=fig_bar)


if __name__ == '__main__':
    app.run(debug=True)
