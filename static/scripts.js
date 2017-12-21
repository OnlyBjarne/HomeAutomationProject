$(document).ready(function () {
    getForecast();
    getWeatherNow();
});

function getWeatherNow() {
    $.getJSON('/weather/now', function (data) {
        var result = [
            data['symbol']['@var'],
            data['temperature']['@value'],
            data['precipitation']['@value'],
            data['windSpeed']['@mps'],
            data['windDirection']['@code']
        ];

        $( "#weathericon" ).attr("src", "https://www.yr.no/grafikk/sym/v2017/png/100/"+result[0]+".png");
        $( "#tempData" ).html(result[1]+"&degC");
        $( "#perciData" ).html(result[2]+" mm");
        $( "#windData" ).html(result[3]+"m/s fra "+result[4]);
    });
    setTimeout(getWeatherNow, 10*60*1000);
}

function getForecast(){
    $.getJSON('/weather/forcast',function(data){
        for (let i = 0; i < data['items'].length; i++) {
            $('#weatherForcastTable').append(
                "<tr>"+
                "<td>"+data['items'][i]['@from']+"</td>"+
                "<td><img style=\"width:50px;\" src=https://www.yr.no/grafikk/sym/v2017/png/100/"
                        +data['items'][i]['symbol']['@var']+".png></td>"+
                "<td>"+data['items'][i]['temperature']['@value']+"&degC</td>"+
                "<td>"+data['items'][i]['precipitation']['@value']+"mm</td>"+
                "<td>"+data['items'][i]['windSpeed']['@mps']+"m/s fra "+
                data['items'][i]['windDirection']['@code']+"</td>"+
                "</tr>"
        );      
        }
    });
}
