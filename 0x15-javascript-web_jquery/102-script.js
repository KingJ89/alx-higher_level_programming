// jQuery script
$(document).ready(function () {
    // Add a click event handler to the translate button
    $('#btn_translate').on('click', function () {
        // Get the language code entered by the user
        const languageCode = $('#language_code').val();

        // Use AJAX to fetch translation data
        $.ajax({
            url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
            method: 'GET',
            dataType: 'json',
            success: function (response) {
                // Extract translation of "hello" from the fetched data
                const translation = response.hello;
                $('#hello').text(translation);
            },
            error: function () {
                // Handle any errors here
                $('#hello').text('Translation not found.');
            }
        });
    });
});
