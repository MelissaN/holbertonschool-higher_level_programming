$(function () {
  $.get('https://swapi.co/api/films/?format=json', function (resp, status) {
    if (status === 'success') {
      let films = resp.results;
      for (let idx in films) {
        $('#list_movies').append('<li>' + films[idx].title + '</li>');
      }
    }
  });
});
