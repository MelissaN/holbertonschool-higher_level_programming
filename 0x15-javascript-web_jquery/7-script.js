$(function () {
  $.get('https://swapi.co/api/people/5/?format=json', function (resp, status) {
    if (status === 'success') {
      $('#character').text(resp.name);
    }
  });
});
