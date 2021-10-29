 
 
 
# PROGRAM        : TO DEVELOP A DASHBOARD AND DISPLAY ALL NECESSARY DETAILS OF ZOMATO BANGLORE RESTAURANT AND PERRFORM DATA ANALYSIS  
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 29-10-2021
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 

from flask import Flask , render_template 

app=Flask(__name__)
@app.route("/")
def table():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True,port=5000)
