from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def index() :
    date = datetime.datetime.now()
    h = date.hour
    m = date.minute
    s = date.second
    return render_template("index.html", heure = h, minute = m, seconde = s)
  
@app.route("/florian")
def florian():
  return "<h1>C'est pas vrai d'abord</h1>"
@app.route("/madec")
def madec():
  return "<h1>t</h1>"
  
 
app.run()


