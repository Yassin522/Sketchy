// JavaScript code can be added here if you have specific functionality to implement.
// For now, this is an empty file.
function toggleInput() {
    if (inputContainer.style.display == "none") {
       inputContainer.style.display = "block";
       sketchPad.triggerUpdate();
    } else {
       inputContainer.style.display = "none";
    }
 }
// Get the container element

