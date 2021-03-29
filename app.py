from flask import Flask, render_template, request
from openweathermap import OpenWeatherMap
from capteur import Capteur

app = Flask(__name__)

meteo = OpenWeatherMap()
sense= Capteur()
PORT=8080

#
@app.route('/', methods=['GET'])
def home():
    sense.mesure()
    sense.get_cpu_temp()
    sense.renderText(str(sense.datas.get("temperature")))
    return render_template("home.html",datas=sense.datas)

#
@app.route('/weather', methods=['GET','POST'])
def weather():
    
    if request.method=="POST":
        city=request.form.get("city")
        if city is not None:
            if meteo.fetchDatas(city):
                # print(meteo.datas.get("name"))
                # print(meteo.datas.get("temperature"))
                # print(meteo.datas.get("pressure"))
                # print(meteo.datas.get("humidity"))
                # print(meteo.datas.get("description"))
                #print(meteo.datas.get("icon_url"))

                return render_template("weather.html", datas=meteo.datas)

        return render_template("weather.html",datas=None)

    if request.method=="GET":
        return render_template("weather.html",datas=None)

#
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
