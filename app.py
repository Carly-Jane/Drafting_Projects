# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)

# Set variables
Title = "Australian Energy Production and Consumption"
Dashboard_Overview = "Reviewing Australian's energy production, state by state, and looking for possible correlations between state population totals and/or median incomes of the states population"


# create route that renders index.html template
@app.route("/")
def echo():

    return render_template("index.html", Title=Title)


# Bonus add a new route
@app.route("/")
def echo():

    return render_template("index.html", Dashboard_Overview=Dashboard_Overview)


if __name__ == "__main__":
    app.run(debug=True)