// jQuery AJAX request
$.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function (response) {
        // Extract the translation of "hello" from the response data
        const translation = response.hello;

        // Display the translation in the <div> with ID 'hello'
        $('DIV#hello').text(translation);
    }
});
