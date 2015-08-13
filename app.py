"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import os, sys

sys.dont_write_bytecode = True
import random

from flask import Flask, render_template, stream_with_context, request, Response, redirect, url_for, flash
from wtforms import StringField, validators
from flask_wtf import Form
from storage import backbone, helper
from model import tables, func

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'x6dgbjldprk3lm52')

###
# Routing for your application.
###
@app.route('/')
def home():
    """Render website's home page."""
    msg = "Default Page Loaded"
    return render_template('home.html', msg=msg)

@app.route('/db/')
@app.route('/db/<table>')
@app.route('/db/<table>/<type>', methods=['GET', 'POST'])
def dbset(table=None, type=None):
    tR = None
    form = None
    ''' Sqlite3 operators '''
    cmd = ["view", "insert", "delete", "update"]

    ''' What Columns am I looking for? '''
    selectorsUnite = ["id", "lastName", "firstName"]

    if request.method == 'GET':
        signal = "GET"
        ''' Let's fetch our Database results now '''
        tR = tables.dbStructure().main(table, type, selectorsUnite)

        if isinstance(tR, dict):
            type = "dict"

        elif isinstance(tR, list):
            type = "list"

        if type==cmd[1]:
            form = Bill(request.form)

    if request.method == 'POST':
        form = Bill(request.form)

        if form.validate():
            flash = 'Thanks for registering'
            return render_template('db/viewer.html', cmd=cmd, tR=tR, table=table, type=type, flash=flash)

        else:
            return render_template('db/viewer.html', cmd=cmd, tR=tR, table=table, type=type, form=form)

    return render_template('db/viewer.html', cmd=cmd, tR=tR, table=table, type=type, form=form)

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = Bill(request.form)

    if request.method == 'POST':
        if form.validate():
            username = [form.username.data, form.email.data]
            flash('Thanks for registering')
            pr = True
            redirect('dbset')
            return redirect(url_for('home', pr=True))
        else:
            return render_template('register.html', form=form, pr=False)

    elif request.method == 'GET':
        return render_template('register.html', form=form)

    else:
        return redirect(url_for('reg'))

''' Name your Table '''
class Bill(Form):
    ''' What columns are involved? '''
    columnTypes = ['id', 'LastName', 'FirstName', 'Address', 'City']
    firstname = StringField('First Name', [validators.DataRequired("Please Enter your Name")])
    lastname = StringField('Last Name',  [validators.DataRequired("Please Enter your Email")])
    address = StringField('Address')
    city = StringField('City',  [validators.DataRequired("Please Enter your City")])

@app.route('/stream')
def streamed_response():
    def generate():
        yield "<div class='red'>Hello " + request.args['name'] + "!</div>"

    return Response(stream_with_context(generate()))

@app.context_processor
def utility_processor():
    def cssStyle():
        r = lambda: random.randint(0, 200)
        color = "#%02X%02X%02X" % (r(), r(), r())
        return color
    return dict(cssStyle=cssStyle)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.template_global(name='zip')
def _zip(*args, **kwargs):  # to not overwrite builtin zip in globals
    return __builtins__.zip(*args, **kwargs)

if __name__ == '__main__':
    app.run(debug=True)
