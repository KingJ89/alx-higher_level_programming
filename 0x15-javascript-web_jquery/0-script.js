// Target the Header Element

const headerE1 = document.querySelector('header');

//verify if header element Exists
if (headerE1) {
    headerE1.style.color = '#FF0000';
} else {
    console.error('No header element detected');
}
