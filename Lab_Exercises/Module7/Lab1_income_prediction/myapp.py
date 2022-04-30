from flask import Flask, render_template,request
# create an app
app = Flask(__name__)
import joblib
model = joblib.load("incomeprediction.pkl")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def main2():
    data = dict(request.form)
    data2 = [data["age"],data["w_class"],data["edu"],data["martial_stat"], data['occup'], data['relation'], data['race'], data['gender'], data['c_gain'], data['c_loss'], data['hours_per_week'], data['native-country']]
    data2 = [int(i) for i in data2]
    output = model.predict([data2])
    data["Prediction"] = output[0]
    return render_template("output.html",output=data)

if __name__=="__main__":
    app.run()
