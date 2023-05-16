const single = document.querySelector('input[value="single"]');
		const double = document.querySelector('input[value="double"]');
		const container1 = document.querySelector('.container-1');
	
		function toggleFields() {
			if (single.checked) {
				container1.classList.add('hide');
				document.querySelector('.container-2').style.marginLeft = '30px';
			} else {
				container1.classList.remove('hide');
				document.querySelector('.container-2').style.marginLeft = '0';
				
    			
    			
			}
		}
	
		// Set initial state
		toggleFields();
	
		// Add event listeners for radio buttons
		document.querySelectorAll('input[name="display"]').forEach(function(input) {
			input.addEventListener('change', toggleFields);
		});