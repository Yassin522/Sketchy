document.addEventListener("DOMContentLoaded", function() {
    // Find the start button element
    var startButton = document.getElementById("start-button");
 
    // Add click event listener to the button
    startButton.addEventListener("click", function() {
       // Redirect to the viewer page
       window.location.href = "viewer.html"; // Replace "viewer.html" with the actual viewer page file name
    });
 });
 