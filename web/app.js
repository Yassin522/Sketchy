// Drawing 
const sketchpad = new SketchPad(document.getElementById('sketchpad'), onUpdate);

function onUpdate(paths) {
  // classify drawing and update predicted label
}

// Chat
const messages = [];

function renderMessages() {
  // loop through messages and render HTML
}

const form = document.getElementById('chat-form');
form.addEventListener('submit', e => {
  e.preventDefault();
  
  // get message text
  // add new message to array
  // call renderMessages
});

renderMessages();