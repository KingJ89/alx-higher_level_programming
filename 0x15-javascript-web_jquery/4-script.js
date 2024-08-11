// jQuery script
$(document).ready(function () {
    // Target the div by its ID
    const toggleTrigger = $('DIV#toggle_header');
    const headerEl = $('header');

    // Attach a click event listener
    toggleTrigger.on('click', function () {
        // Toggle between 'red' and 'green' classes
        headerEl.toggleClass('red green');
    });
});
