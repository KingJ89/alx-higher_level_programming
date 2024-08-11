// jQuery script
$(document).ready(function () {
    // Add a new list item when 'add_item' div is clicked
    $('DIV#add_item').on('click', function () {
        $('UL.my_list').append('<li>Item</li>');
    });

    // Remove the last list item when 'remove_item' div is clicked
    $('DIV#remove_item').on('click', function () {
        $('UL.my_list li:last').remove();
    });

    // Clear all list items when 'clear_list' div is clicked
    $('DIV#clear_list').on('click', function () {
        $('UL.my_list').empty();
    });
});
