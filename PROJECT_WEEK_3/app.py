from pymongo import MongoClient 
from flask import Flask 
# PROGRAM        : CREATING A FRONT END DISPLAY USING FLASK AND HTML TO DISPLAY PDF REPORT
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 22-OCT-2021
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 

from flask import render_template

from flask import redirect
from flask import url_for 
from flask import request
from pymongo import MongoClient

app=Flask(__name__)
connection=MongoClient("mongodb://localhost:27017")

# Displaying The Report from front end  i.e Using Flask and HTML
@app.route('/')
def index():
    return render_template("report.html")


if __name__=="__main__":
    app.run(debug=True,port=5000)