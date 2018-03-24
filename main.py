from flask import Flask, request, redirect
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

time_form = """
    <!doctype html>
    <head>
    <title>Validate Time</title>
    </head>
    <body>
    <style>
        .error {{ color: red; }}
        </style>
    <h1>Validate Time</h1>
    <form method="POST">
        <label>Hours (24-hour format)
            <input name="hours" type="text" value="{hours}" />
        </label>
        <p class="error">{hours_error}</p>
        <label>Minutes
            <input name="minutes" type="text" value="{minutes}" />
        </label>
        <p class="error"> {minutes_error}</p>
        <input type="submit" value="Validate" />
    </form>
    </body>
    </html>
    """

@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='',hours_error='',minutes='', minutes_error='')

def is_integer(num):
    try:
        int(num)
        return TrueP
    except ValueError:
        return False

@app.route('/validate-time', methods=['POST'])
def validate_time():

    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour value out of range (0-23)'
            hours = ''

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            miuntes_error = 'Minute value out of range (0-59)'
            minutes = ''

    if not minutes_error and not hours_error:
        time = str(hours) + ':' + str(minutes)
        return redirect('/valid-time?time={0}'.format(time))
    else:
        return time_form.format(hours_error=hours_error, 
               minutes_error=minutes_error, 
               hours = hours, 
               minutes = minutes)

@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitted {0}. Thanks for submitting a valid time!</h1>'.format(time)

if __name__ == "__main__":
    app.run()
