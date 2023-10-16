class MainSketchPad {
    constructor(container, onUpdate = null, size = 400) {
       this.canvas = document.createElement("canvas");
       this.canvas.width = size;
       this.canvas.height = size;
       this.canvas.style = `
          background-color:white;
          box-shadow: 0px 0px 10px 2px white;
          margin-bottom: 10px;
       `;
       container.appendChild(this.canvas);
       const padContainer = document.createElement("div");
       padContainer.classList.add("pad-container"); // Use the class name "pad-container"
       container.appendChild(padContainer);

       const colorButtonsContainer = document.createElement("div");
       colorButtonsContainer.style.display = "flex";
       padContainer.appendChild(colorButtonsContainer);


       this.undoBtn = document.createElement("button");
       this.undoBtn.innerHTML = '<i class="icon">↩️</i>Undo'; // Using the "undo" icon
       this.undoBtn.classList.add("undo-button"); // Add the "undo-button" class
       padContainer.appendChild(this.undoBtn);
       this.undoBtn.addEventListener("click", () => {
        this.undoBtn.classList.add("clicked");
        // You can add your undo functionality here
      });
      this.undoBtn.addEventListener("animationend", () => {
        this.undoBtn.classList.remove("clicked");
      });
 
       
      
       
       
       
 
       this.lineColor = "black";
 
       this.ctx = this.canvas.getContext("2d");
 
       this.onUpdate = onUpdate;
       this.reset();
 
       this.#addEventListeners();
       this.#createColorButtons(colorButtonsContainer);
    }
 
    reset() {
       this.paths = [];
       this.isDrawing = false;
       this.#redraw();
    }
     
    onColorButtonClick(event) {
        const colorButtons = document.querySelectorAll('.color-button');
        colorButtons.forEach(button => button.classList.remove('active'));
    
        const colorButton = event.target;
        colorButton.classList.add('active');
        this.setLineColor(color);
        // Toggle the 'active' class on the clicked color button
        colorButton.classList.toggle("active");
    
        const selectedColor = window.getComputedStyle(colorButton).backgroundColor;
        console.log('Selected Color:', selectedColor);
      }
    
 
    #addEventListeners() {
       this.canvas.onpointerdown = (evt) => {
          const mouse = this.#getMouse(evt);
          this.paths.push([mouse]);
          this.isDrawing = true;
          evt.preventDefault();
       };
       this.canvas.onpointermove = (evt) => {
          if (this.isDrawing) {
             const mouse = this.#getMouse(evt);
             const lastPath = this.paths[this.paths.length - 1];
             lastPath.push(mouse);
             this.#redraw();
          }
          evt.preventDefault();
       };
       document.onpointerup = () => {
          this.isDrawing = false;
       };
       this.undoBtn.onclick = () => {
          this.paths.pop();
          this.#redraw();
       };
    }
 
    #redraw() {
       this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
       draw.paths(this.ctx, this.paths, this.lineColor);
       if (this.paths.length > 0) {
          this.undoBtn.disabled = false;
       } else {
          this.undoBtn.disabled = true;
       }
       this.triggerUpdate();
    }
 
    triggerUpdate() {
       if (this.onUpdate) {
          this.onUpdate(this.paths);
       }
    }

    
 
    setLineColor(color) {
       this.lineColor = color;
    }
 
    #getMouse = (evt) => {
       const rect = this.canvas.getBoundingClientRect();
       return [
          Math.round(evt.clientX - rect.left),
          Math.round(evt.clientY - rect.top),
       ];
    };
 
    #createColorButtons(container) {
        const colors = ["black", "red", "green", "blue", "yellow", "orange", "purple"];
;
        for (const color of colors) {
          const colorButton = document.createElement("button");
          colorButton.classList.add("color-button"); // Add the "color-button" class
          colorButton.style.backgroundColor = color;
          colorButton.style.marginRight = "5px";
          colorButton.onclick = () => {
            this.setLineColor(color);
            // Update the lineColor property when a color button is clicked
            this.lineColor = color;
            // Toggle the 'active' class on the clicked color button
            colorButton.classList.toggle("active");
          };
          container.appendChild(colorButton);
        }
      } 
 }