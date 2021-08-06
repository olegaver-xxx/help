from flask import render_template
from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    date = datetime.datetime.now()
    return render_template('index.html',name=date)

app.run(host='0.0.0.0', port=80,debug=True)