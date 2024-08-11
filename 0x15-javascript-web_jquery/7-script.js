// jQuery AJAX request
$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (response) {
        // Extract the character's name from the response data
        const characterName = response.name;

        // Display the character's name in the div with ID 'character'
        $('DIV#character').text(characterName);
    }
});
