# app5.py
# David Prager Branenr
# 20140303

"""Basic Flask application to process Chinese poem."""

from flask import Flask, render_template, redirect, session
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from format_poem import format_poem

class PoemInputForm(Form):
    poem = TextAreaField('poem', validators=[DataRequired()])
    submit = SubmitField('submit')


app = Flask(__name__) # __name__ because this file is self-contained.
app.config['SECRET_KEY'] = 'secretsecret'
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    the_form = PoemInputForm()
    if the_form.validate_on_submit():
        session['input_poem'] = the_form.poem.data
        return redirect('/format')
    return render_template('index.html', form=the_form)

@app.route('/format')
def results():
    session['input_poem'] = format_poem(session['input_poem'])
    # process text
    return render_template('results.html')

if __name__ == ('__main__'):
    app.run(debug=True)
