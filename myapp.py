from flask import Flask, render_template,request
#import pyowm
app = Flask(__name__)

#def weather(place):
#    owm = pyowm.OWM("bc2ab34b16719508a9ba53b2ffbaa4f8")
#    obs = owm.weather_at_place(place)
#    w = obs.get_weather()
#    temp = w.get_temperature('celsius')
#    return [w.get_humidity(), temp['temp']]


@app.route('/',methods=['POST','GET']) 
def index():
    data = [3, 2.2]
    if request.method == 'POST':
        place = request.form['location']
        #data = weather(place)
        data = [345.3, 2472.2]
        return render_template('index.html',data = data)
    elif request.method == 'GET':
         return render_template('index.html',data=data)
   


# adding another route
#@app.route('/whereami')
#def whereami():
#   return 'Cape Coast !!'
# type http://127.0.0.1:5000/whereami in browser to see change

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')

