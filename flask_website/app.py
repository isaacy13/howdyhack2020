from flask import Flask, render_template, request
# may have to kill python.exe in task manager
#py -m venv env
#env\Scripts\activate
#flask run
#$env:FLASK_ENV="development"

#deactivate

#note - use ctrl + f5 to refresh css

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "test_user" and password == "bailey1":
            return render_template("welcome.html")
        return render_template("data.html", username=username, password=password)

    return render_template("index.html")
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")