# app4.py
#20140303

from flask import Flask, render_template, redirect, session
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PoemInputForm(Form):
    name = TextAreaField('name', validators=[DataRequired()])
    submit = SubmitField('submit')


app = Flask(__name__) # __name__ because this file is self-contained.
app.config['SECRET_KEY'] = 'secretsecret'
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    the_form = PoemInputForm()
    if the_form.validate_on_submit():
        session['input'] = the_form.name.data
        return redirect('/format')
    return render_template('index.html', form=the_form)

@app.route('/format')
def results():
    text = session['input']
    return render_template('results.html', text=text)

if __name__ == ('__main__'):
    app.run(debug=True)
