// swiching 'translate' and 'text and translate' mode
const single = document.querySelector('input[value="single"]');
const double = document.querySelector('input[value="double"]');
const container1 = document.querySelector('.container-1');
const container2 = document.querySelector('.container-2');
const container2InitialMarginLeft = container2.style.marginLeft;
const container2InitialMarginRight = container2.style.marginRight;
const breakpoint = 900; // Adjust this value as needed

function toggleFields() {
  if (single.checked) {
    container1.classList.add('hide');
    updateContainer2Margins();
  } else {
    container1.classList.remove('hide');
    updateContainer2Margins();
  }
}

function updateContainer2Margins() {
  if (window.innerWidth <= breakpoint) {
    container2.style.marginLeft = '10px';
    container2.style.marginRight = '10px';
  } else {
    if (container1.classList.contains('hide')) {
      container2.style.marginLeft = '30px';
    } else {
      container2.style.marginLeft = container2InitialMarginLeft;
      container2.style.marginRight = container2InitialMarginRight;
    }
  }
}

// Set initial state
toggleFields();

// Add event listeners for radio buttons
document.querySelectorAll('input[name="display"]').forEach(function (input) {
  input.addEventListener('change', toggleFields);
});

// Add event listener for window resize
window.addEventListener('resize', updateContainer2Margins);

// ...

// Function to count the symbols in the textarea
function countSymbols() {
  var textarea = document.getElementById('originText');
  var countElement = document.getElementById('symbolCount');

  var value = textarea.value;
  var symbolCount = value.length;

  countElement.textContent = symbolCount + '/5000';

  // Check if symbolCount exceeds the maximum limit
  if (symbolCount >= 5000) {
    countElement.style.color = "red"
  } else {
    countElement.style.color = "inherit"
  }
}

// Call the countSymbols function after the page is fully loaded
window.addEventListener('DOMContentLoaded', function() {
  countSymbols();
});

// Add event listener for input changes in the textarea
document.getElementById('originText').addEventListener('input', countSymbols);

// ...



