$(function () {
  $.get('https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json', function (resp, status) {
    if (status === 'success') {
      $('#sf_wind_speed').text(resp.query.results.channel.wind.speed);
    }
  });
});
