from flask import Flask, render_template, request
import pickle
import pickle

# Assuming model_rb is your trained model
with open("./car_price_prediction.pkl", "wb") as file:
    pickle.dump(render_template, file)


# load the model
with open("./car_price_prediction.pkl", "rb") as file:
    model_rf = pickle.load(file)


app = Flask(__name__)



@app.route("/", methods=["GET"])
def index():
    # sends the file car_price_prediction.html from templates directory
    return render_template("car_price_prediction.html")


@app.route("/predict", methods=["GET"])
def predict_price(model_rf=None):
    # get values from request
    try:
        print(request.args)
        year = int(request.args.get("year"))
        age = 2022 - year
        odom = float(request.args.get("odom"))
        cylin = int(request.args.get("cylin"))
        manuf = int(request.args.get("slct1"))
        model = int(request.args.get("slct2"))
        fueltyp = int(request.args.get("fueltyp"))
        title = int(request.args.get("title"))
        transm = int(request.args.get("transm"))
        cond = int(request.args.get("cond"))
        drivetype = int(request.args.get("drivetype"))
        type = int(request.args.get("type"))
        color = int(request.args.get("color"))
        state = int(request.args.get("state"))

        price = model_rf.predict([[year, age, odom, cylin, manuf, model, fueltyp, title, transm, cond, drivetype, type, color, state]])
        car_price = "{:.2f}".format(price[0])

        #return f"<h1>Predicted price of the car = ${price[0]}</style></h1>"
        return render_template("result.html", prediction=car_price)


    except:
        return f"<h1>It seems you have not selected the required inputs...Please try again !!</h1>"



app.run(host="localhost", port=4500, debug=True)
