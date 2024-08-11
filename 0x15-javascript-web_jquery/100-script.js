// jQuery script
$(document).ready(function () {
    // Select the <header> element
    const $header = $('header');

    // Check if the <header> element exists
    if ($header.length) {
        // Set the text color to red
        $header.css('color', '#FF0000');
    } else {
        console.error('Header element not found.');
    }
});
