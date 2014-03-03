# app1.py
#20140303

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Test.'

if __name__ == ('__main__'):
    app.run(debug=True)
