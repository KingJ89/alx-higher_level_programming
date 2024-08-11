// jQuery script
$(document).ready(function () {
  // Select the header element using jQuery
  const headerElement = $('header');

  // Verify the presence of the header element
  if (headerElement.length) {
    // Set the text color using CSS
    headerElement.css('color', '#FF0000');
  } else {
    console.error('No header element detected');
  }
});
