$(document).ready(function () {
    getWeatherNow();
});

function getWeatherNow() {
    $.getJSON('/weather', function (data) {
        var result = [
            data['symbol']['@var'],
            data['temperature']['@value'],
            data['windDirection']['@code'],
            data['windSpeed']['@mps'],
            data['precipitation']['@value']
        ];
        $( "#weathericon" ).attr("src", "https://www.yr.no/grafikk/sym/v2017/png/100/"+result[0]+".png");
        $( "#tempData" ).html(result[1]+"&degC");
        $( "#perciData" ).html(result[4]+" mm");
        $( "#windData" ).html(result[3]+"m/s fra "+result[2]);
    });
    setTimeout(getWeatherNow, 10*60*1000);
}
