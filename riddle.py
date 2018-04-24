import os
import json
from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)


#opening the json riddle file
with open("data/riddle.json", "r") as json_data:
        data = json.load(json_data)

#index app route
def write_to_file(filename, data):
     with open(filename, "a") as file:
        file.writelines(data)

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
        write_to_file("data/players.txt", request.form["username"])
        return redirect(request.form["username"])
    return render_template("index.html")
        
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)     