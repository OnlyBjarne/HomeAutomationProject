from yr.libyr import Yr
import datetime

try:
    yr = Yr(location_name='Norge/Sør-Trøndelag/Trondheim/Trondheim')
except RuntimeWarning:
    print("Whoops, something went wrong with fetching your yr!")
    pass

class weather:

    def weatherNow(self):
        now = yr.now(as_json=False)
        weatherDict = {"temp": now['temperature']['@value'],
                       "precipitation": now['precipitation']['@value'],
                       "windDir": now['windDirection']['@code'],
                       "windSpeed": now['windSpeed']['@mps'],
                       "symbol": now['symbol']['@var']}
        return weatherDict

    def weatherForcast(self):
        forecastArray = []
        for forecast in yr.forecast():
            time = datetime.datetime.strptime(
                forecast['@from'], "%Y-%m-%dT%H:%M:%S")
            dayName = ["Man", "Tir", "Ons", "Tor", "Fre", "Lør", "Søn"]
            forecastArray.append({
                # readable datetime
                "time": "{} {:%H:%M}".format(str(dayName[time.weekday()-1]), time),
                "symbol": forecast['symbol']['@var'],
                "temp": forecast['temperature']['@value'],
                "precipitation": forecast['precipitation']['@value'],
                "windDir": forecast['windDirection']['@code'],
                "windSpeed": forecast['windSpeed']['@mps']
            })
        return forecastArray