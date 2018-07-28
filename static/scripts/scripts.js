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