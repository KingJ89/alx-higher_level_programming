// jQuery script
$(document).ready(function () {
    // Target the div with ID 'add_item'
    const addItemBtn = $('DIV#add_item');

    // Attach a click event listener
    addItemBtn.on('click', function () {
        // Append a new list item to the unordered list
        $('UL.my_list').append('<li>Item</li>');
    });
});

