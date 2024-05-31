$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
  const films = data.results;

  $.each(films, function (index, value) {
    $('ul#list_movies').append('<li>' + value.title + '</li>');
  });
});
