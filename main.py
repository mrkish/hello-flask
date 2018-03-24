from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
<body>
<form action="/hello" method="post">
<label for="first-name">First Name:</label>
<input id="first-name" type="text" name="first_name" />
<input type="submit"/>
</form>
</body>
</html>
"""

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '</h1>'



@app.route('/forms')
def index():
    return form


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)


if __name__ == "__main__":
    app.run()
