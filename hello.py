from flask import Flask, render_template

from flask import g

import sqlite3

app  = Flask('flaskwp1')
app.secret_key = 'some_secret'
app.database = "sample.db"

# webcode = open('webcode.html').read() - not needed

#@app.route('/student')
#def student():
#    return render_template("student.html")

# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
                       DATABASE=os.path.join(app.root_path, 'flaskr.db'),
                       SECRET_KEY='development key',
                       USERNAME='admin',
                       PASSWORD='default'
                       ))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)




@app.route('/student')
def homepage():
    return render_template("student.html")

@app.route('/login2')
def homepage2():
    return render_template("login2.html")

@app.route('/vid_student.html')
def student():
    return render_template("vid_student.html")

@app.route('/recruiter.html')
def recruiter():
    return render_template("presenter.html")

@app.route('/student.html')
def r2():
    return render_template("student.html")

@app.route('/check')
def check():
    return render_template("event1.html")
# login page

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    error = None
#    if request.method == 'POST':
#        if request.form['username'] != app.config['USERNAME']:
#            error = 'Invalid username'
#        elif request.form['password'] != app.config['PASSWORD']:
#            error = 'Invalid password'
#        else:
#            session['logged_in'] = True
#            flash('You were logged in')
#            return redirect(url_for('show_entries'))

#    return render_template('login.html', error=error)

# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
            flash(u'Invalid password provided', 'error')

        else:
            session['logged_in'] = True 
            flash('You are logged in')

            return redirect(url_for('check'))
    return render_template('login.html', error=error)

# logout page
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were recently logged out')
    return redirect(url_for('login'))

@app.route('/index')
def home():
    return render_template('folder/index.html')

    #g.db = connect.db()
    #cur = g.db.execute('select * from posts')
    #posts = [dict(title = row[0],description = row[1]) for row in cur.fetchall()]
    #g.db.close();
    #return render_template('index.html', posts = posts)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000)
