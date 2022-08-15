from flask import Flask, render_template, jsonify, send_file, request, redirect, url_for
import pandas as pd
from plotting import make_plot_brand, make_plot_year, make_plot_fuel_type, make_plot_engine, make_plot_transmission
from flask_swagger_ui import get_swaggerui_blueprint
import seaborn as sns
import matplotlib.pyplot as plt


#This is going to be our main module, with all our RESTful endpoints.

# Create the application instance
app = Flask(__name__, template_folder="templates")

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Cars Predictions"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


username = ""
password = ""





@app.route('/cars')
@app.route('/cars/')
def cars():
    cars_data = pd.read_csv("train.csv").fillna("null")
    cars_api = cars_data.to_dict(orient="records")

    return jsonify(cars_api)



@app.route('/graphs/brands', methods = ["GET", "POST"])
def graph_brands():   
    print("brand", request.form.getlist("brand"))
    brand = request.form.get("brand")
    plot = make_plot_brand(brand)

    return send_file(plot,attachment_filename='plot.png',mimetype='image/png')

@app.route('/graphs/fuel_types', methods = ["GET", "POST"])
def graph_fuels():   
    print("fuel_type", request.form.getlist("fuel_type"))
    fuel_type = request.form.get("fuel_type")
    plot = make_plot_fuel_type(fuel_type)

    return send_file(plot,attachment_filename='plot.png',mimetype='image/png')


@app.route('/graphs/years', methods = ["GET", "POST"])
def graph_years():   
    print("year", request.form.getlist("year"))
    year = request.form.get("year")
    plot = make_plot_year(year)

    return send_file(plot,attachment_filename='plot.png',mimetype='image/png')


@app.route("/", methods = ["GET", "POST"])
def login():
    
    print("login")
    if request.method == "POST" and username == "user" and password == "pass" :
        
        print("hihihi")
        return redirect(url_for("check"))
    else :
        message = "Connectez-vous"
        return render_template("login.html", message = message, username = username, password = password)

@app.route("/login/check", methods = ["GET", "POST"])
def check() :
    username = request.form.getlist("username")[0]
    password = request.form.getlist("password")[0]
    if username == "user" and password == "pass" :
        
        return redirect(url_for("home"))
    else :
        return redirect(url_for("login"))


    
@app.route("/home", methods = ["GET", "POST"])
def home():

    return render_template("home.html")


@app.route("/stats", methods = ["GET", "POST"])
def show():
    brand_list=["Maruti", "Hyundai", "Honda", "Audi", "Nissan", "Toyota", "Volkswagen", "Tata", "Land", "Mitsubishi", "Renault", "Benz", "BMW", "Mahindra", "Ford", "Porsche", "Datsun", "Jaguar", "Volvo", "Chevrolet", "Skoda", "Mini", "Fiat", "Jeep", "other"]
    fuel_list=["Diesel", "Petrol", "CNG", "LPG"]
    year_list=[2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998]
    message = "Choissisez votre statistique!"
    return render_template("stats.html", message = message, brands=brand_list, fuel_types=fuel_list, years=year_list)


@app.route("/plot")
def plot():
    x=request.args.get("x")
    y=request.args.get("y")
    message=request.args.get("message")
    return render_template("plot.html", message=message, x=x, y=y)


@app.route("/predictions", methods = ["GET", "POST"])
def predictions():
    return render_template("predictions.html")


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)