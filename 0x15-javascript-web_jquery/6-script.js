// jQuery script
$(document).ready(function () {
    // Select the div with ID 'update_header'
    const updateHeaderDiv = $('DIV#update_header');

    // Add a click event handler
    updateHeaderDiv.on('click', function () {
        // Update the text of the header element
        $('header').text('New Header!!!');
    });
});

