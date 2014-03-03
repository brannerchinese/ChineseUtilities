# app3.py
#20140303

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == ('__main__'):
    app.run(debug=True)
