// jQuery script
$(document).ready(function () {
    // Attach click event handler to the translate button
    $('INPUT#btn_translate').on('click', translate);

    // Attach keydown event handler to the language code input
    $('INPUT#language_code').on('keydown', function (e) {
        // Check if the pressed key is Enter
        if (e.keyCode === 13) {
            translate();
        }
    });
});

// Function to perform translation
function translate() {
    // Construct the URL with query parameters
    const url = 'https://www.fourtonfish.com/hellosalut/';
    const languageCode = $('INPUT#language_code').val();
    
    $.get(url, { lang: languageCode }, function (data) {
        // Update the text of the div with the translation
        $('DIV#hello').html(data.hello);
    });
}

