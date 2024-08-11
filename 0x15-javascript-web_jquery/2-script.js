// jQuery script
$(document).ready(function () {

    // Target the div by its ID
    const triggerDiv = $('DIV#red_header');

    // Attach a click event listener
    triggerDiv.on('click', function () {
        // Locate the header element
        const headerEl = $('header');

        // Ensure the header element exists
        if (headerEl.length) {
            // Apply the red color using CSS
            headerEl.css('color', '#FF0000');
        } else {
            console.error('No header element detected');
        }
    });
});
