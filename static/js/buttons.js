document.addEventListener('DOMContentLoaded', function() {
    var isHide = document.getElementById('is-hide').value;
    hide_buttons(isHide);
  });
  
function hide_buttons(isHide) {
    var clean_button = document.querySelector('.clean_button');

    try{
        var drop_button = document.querySelector('.drop_button');
    }
    catch(err){
        return;
   }
    if (isHide === "true") {
        clean_button.classList.add('hide');
        try {
            drop_button.classList.add('hide');
          }
          catch(err) {
            return;
          }
    } else {
        clean_button.classList.remove('hide');
        try{
            drop_button.classList.remove('hide');  
        }
        catch(err) {
            return;
        }
    }
}
  

function clearTextarea() {
    var originTextElement = document.getElementById('originText');
    var translatedTextElement = document.getElementById('translatedText');

    // Update the text of the text area elements
    originTextElement.value = '';
    translatedTextElement.value = '';
}
  
function copyText(idElement) {
// Get the text area element
var textarea = document.getElementById(idElement);

// Select the text inside the text area
textarea.select();
textarea.setSelectionRange(0, 99999); // For mobile devices

// Copy the selected text to the clipboard using the Clipboard API
navigator.clipboard.writeText(textarea.value)
    .then(function() {
    // Notification 'copied'
    var notification = document.getElementById('notification');
    notification.innerText = 'Copied';
    notification.classList.add('show');

    setTimeout(function () {
        notification.classList.remove('show');
    }, 3000);
    })
    .catch(function(error) {
    console.error('Failed to copy text: ', error);
    });
}