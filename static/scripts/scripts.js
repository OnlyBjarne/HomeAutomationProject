$(document).ready(function () {

    //check which page we are on to just load one of the weather elements
    if (document.location.pathname == "/forecast") {
        getForecast();
    }
    if (document.location.pathname == "/") {
        getWeatherNow();
        getForecast();

    }
    if (document.location.pathname == "/timepicker") {
        alarmSet();
    }

});

/* 
function getWeatherNow() {
    $.getJSON('/weather/now', function (data) {
        var result = [
            data['symbol']['@var'],
            data['temperature']['@value'],
            data['precipitation']['@value'],
            data['windSpeed']['@mps'],
            getArrowAngle(data['windDirection']['@deg'])
        ];


        $("#weathericon").attr("src", "static/images/weatherIcons/" + result[0] + ".png");
        $("#tempData").html(result[1] + "&degC");
        $("#perciData").html(result[2] + " mm");
        $("#windData").html(result[3] + "m/s fra <img src=\"http://fil.nrk.no/yr/grafikk/vindpiler/32/vindpil.0000." +
            padString(result[4], 3) + ".png\">");
    });
    setTimeout(getWeatherNow, 10 * 60 * 1000);
} */
/* 
function getForecast() {

    $.getJSON('/weather/forecast', function (data) {
        //loop for x number of days
        for (let i = 0; i < 7 * 4; i++) {
            //convert yr's timeformat to something more pleasing for the eye
            var date = new Date(parseInt(Date.parse(data['items'][i]['@from'])));
            var hour = date.getHours() < 10 ? '0' + date.getHours() : date.getHours();
            var minutes = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes();
            var day = date.getDay();
            var dayName = ["Søn", "Man", "Tir", "Ons", "Tor", "Fre", "Lør"];
            var time = dayName[day] + " " + hour + ":" + minutes;
            var windDeg = getArrowAngle(data['items'][i]['windDirection']['@deg']);

            $('#weatherForcastTable').append(
                "<tr>" +
                "<td>" + time + "</td>" +
                "<td><img style=\"width:50px;\" src=static/images/weatherIcons/"
                + data['items'][i]['symbol']['@var'] + ".png></td>" +
                "<td class=\"text-center\">" + data['items'][i]['temperature']['@value'] + "&degC</td>" +
                "<td>" + data['items'][i]['precipitation']['@value'] + "mm</td>" +
                "<td>" + data['items'][i]['windSpeed']['@mps'] + "m/s " +
                "<img src=\"http://fil.nrk.no/yr/grafikk/vindpiler/32/vindpil.0000." +
                padString(windDeg, 3) +
                ".png\"></td>" +
                "</tr>"
            );
        }
    });
} */

function padString(string, lenght) {
    return ("0000" + string).substr(-lenght);
}

function getArrowAngle(angle) {
    angle = Math.round(parseInt(angle) / 5) * 5;
    if (angle == 360) {
        angle = 0;
    }
    return angle;
}

function alarmSet() {
    $('#time').bootstrapMaterialDatePicker({ date: false });
}