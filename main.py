from flask import Flask, render_template
from grafy import grafy
app = Flask(__name__)

@app.route('/') 
def domov():
    return render_template('index.html')

@app.route('/graf')
def graf():
    fig = grafy.mapa()
    return render_template('graf.html', plot=fig.to_html(full_html=False))


if __name__ == '__main__':
    app.run(debug=True)
