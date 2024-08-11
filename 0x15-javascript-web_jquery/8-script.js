// jQuery AJAX request
$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (response) {
        // Extract movie titles from the response data
        const movieTitles = response.results.map(movie => movie.title);

        // Select the <ul> element with ID 'list_movies'
        const movieList = $('UL#list_movies');
        
        // Clear the list before appending new items
        movieList.empty();

        // Append each movie title as a list item
        $.each(movieTitles, function (index, title) {
            movieList.append(`<li>${title}</li>`);
        });
    }
});
