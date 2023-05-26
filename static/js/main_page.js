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
	}
	else{
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
