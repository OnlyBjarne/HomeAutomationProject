$(document).ready(function () {
    getWeatherNow();
});

function getWeatherNow() {
    $.get('/weather', function (result) {
        var symbol = result['symbol']['@numberEx'];
        var temp = result['temperature']['@value'];
        var windDir = result['windDirection']['@code'];
        var  windSpeed = result['windSpeed']['@mps'];
        var downfall = result['precipitation']['@value'];
        alert(symbol);
    });
}
