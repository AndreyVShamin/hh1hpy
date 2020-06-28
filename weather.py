#!/root/python/hh1h/bin/python

import pyowm
#from pyowm import OWM

place = input("В каком городе/стране?(Bryansk,RU): ")
owm = pyowm.OWM('b48a4a000a364c85f529c1e47f73b192', language = "ru")
#owm = pyowm.OWM('e013060cda7a779313548cf059d42309')
#mgr = owm.weather_manager()
observation = owm.weather_at_place(place)
w = observation.get_weather()
temp = w.get_temperature('celsius')["temp"]

print( "В городе " + " сейчас " + w.get_detailed_status() )
print( "Температура сейчас в районе " + str(temp) )

if temp < 10:
	print( "Холодина" )
elif temp < 20:
	print( "Холодновато")
else:
	print( "Нормуль" )

