from flask import render_template
from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    date = datetime.date.today()
    return render_template('index.html',date=date)

app.run(host='0.0.0.0', port=8080,deb
