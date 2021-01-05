from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Ben'}
    projects = [
        {
            'title':'Pitching Stats Dashboard',
            'date':'11/19/2020',
            'github':'github.com/bgunn34/pitchers_dashboard'
        },
        {
            'title':'Batting Stats Dashboard',
            'date':'12/02/2020',
            'github':'github.com/bgunn34/batters_dashboard'
        }
    ]
    return render_template('index.html',user=user,projects=projects)