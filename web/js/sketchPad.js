class SketchPad {
   constructor(container, onUpdate = null, size = 400) {
      this.canvas = document.createElement("canvas");
      this.canvas.width = size;
      this.canvas.height = size;
      this.canvas.style = `
         background-color:white;
         box-shadow: 0px 0px 10px 2px white;
      `;
      container.appendChild(this.canvas);

      const buttonsContainer = document.createElement("div");
      buttonsContainer.style.display = "flex";
      container.appendChild(buttonsContainer);

      const colorButtonsContainer = document.createElement("div");
      colorButtonsContainer.style.display = "flex";
      buttonsContainer.appendChild(colorButtonsContainer);

      this.undoBtn = document.createElement("button");
      this.undoBtn.innerHTML = "UNDO";
      this.undoBtn.style.marginRight = "10px";
      buttonsContainer.appendChild(this.undoBtn);

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
      const colors = ["black","red", "green", "blue", "yellow", "orange"];
      for (const color of colors) {
         const colorButton = document.createElement("button");
         colorButton.style.backgroundColor = color;
         colorButton.style.width = "20px";
         colorButton.style.height = "20px";
         colorButton.style.border = "none";
         colorButton.style.marginRight = "5px";
         colorButton.onclick = () => {
            this.setLineColor(color);
         };
         container.appendChild(colorButton);
      }
   }
}
