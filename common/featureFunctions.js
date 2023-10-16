if (typeof geometry === "undefined") {
   geometry = require("./geometry.js");
}

if (typeof draw === "undefined") {
   draw = require("./draw.js");
}
const featureFunctions = {};

featureFunctions.getPathCount = (paths) => {
   return paths.length;
};

featureFunctions.getPointCount = (paths) => {
   const points = paths.flat();
   return points.length;
};

featureFunctions.getWidth = (paths) => {
   const points = paths.flat();
   if(points.length==0){
      return 0;
   }
   const x = points.map((p) => p[0]);
   const min = Math.min(...x);
   const max = Math.max(...x);
   return max - min;
};

featureFunctions.getHeight = (paths) => {
   const points = paths.flat();
   if(points.length==0){
      return 0;
   }
   const y = points.map((p) => p[1]);
   const min = Math.min(...y);
   const max = Math.max(...y);
   return max - min;
};

featureFunctions.getElongation = (paths) => {
   const points = paths.flat();
   const { width, height } = geometry.minimumBoundingBox({ points });
   return (Math.max(width, height) + 1) /
      (Math.min(width, height) + 1);
};

featureFunctions.getRoundness = (paths) => {
   const points = paths.flat();
   const { hull } = geometry.minimumBoundingBox({ points });
   return geometry.roundness(hull);
};

featureFunctions.getPixels = (paths, size = 400, expand = true) => {
   let canvas = null;

   try {
      canvas = document.createElement("canvas");
      canvas.width = size;
      canvas.height = size;
   } catch (err) {
      const { createCanvas } = require("../node/node_modules/canvas");
      canvas = createCanvas(size, size);
   }

   const ctx = canvas.getContext("2d");

   if (expand) {
      const points = paths.flat();

      const bounds = {
         left: Math.min(...points.map((p) => p[0])),
         right: Math.max(...points.map((p) => p[0])),
         top: Math.min(...points.map((p) => p[1])),
         bottom: Math.max(...points.map((p) => p[1]))
      };

      const newPaths = [];
      for (const path of paths) {
         const newPoints = path.map(p =>
            [
               utils.invLerp(bounds.left, bounds.right, p[0]) * size,
               utils.invLerp(bounds.top, bounds.bottom, p[1]) * size
            ]
         );
         newPaths.push(newPoints);
      }
      draw.paths(ctx, newPaths);
   } else {
      draw.paths(ctx, paths);
   }

   const imgData = ctx.getImageData(0, 0, size, size);
   return imgData.data.filter((val, index) => index % 4 == 3);
};

featureFunctions.getComplexity = (paths) => {
   const pixels = featureFunctions.getPixels(paths);
   return pixels.filter((a) => a != 0).length;
};

featureFunctions.getSymmetry = (paths) => {
   const points = paths.flat();
   const xValues = points.map(p => p[0]);
   const midX = (Math.min(...xValues) + Math.max(...xValues)) / 2;
   const sumDistances = points.reduce((sum, p) => sum + Math.abs(p[0] - midX), 0);
   const avgDistance = sumDistances / points.length;

   return 1 / (1 + avgDistance);
};

function euclideanDistance(p1, p2) {
   const dx = p1[0] - p2[0];
   const dy = p1[1] - p2[1];
   return Math.sqrt(dx * dx + dy * dy);
}

featureFunctions.getAverageNearestNeighborDistance = (paths) => {
   const points = paths.flat();
   const distances = [];
   if(points.length==0){
      return 0;
   }

   for (let i = 0; i < points.length; i++) {
      let nearestDistance = Number.MAX_VALUE;
      for (let j = 0; j < points.length; j++) {
         if (i !== j) {
            const distance = euclideanDistance(points[i], points[j]);
            nearestDistance = Math.min(nearestDistance, distance);
         }
      }
      distances.push(nearestDistance);
   }

   const averageDistance = distances.reduce((sum, distance) => sum + distance, 0) / distances.length;
   return averageDistance;
};

featureFunctions.getMaximumNearestNeighborDistance = (paths) => {
   const points = paths.flat();
   let maxDistance = 0;

   for (let i = 0; i < points.length; i++) {
      for (let j = 0; j < points.length; j++) {
         if (i !== j) {
            const distance = euclideanDistance(points[i], points[j]);
            maxDistance = Math.max(maxDistance, distance);
         }
      }
   }

   return maxDistance;
};


function calculateBoxCount(points, boxSize) {
   const boxes = new Map();

   for (const point of points) {
      const boxX = Math.floor(point[0] / boxSize);
      const boxY = Math.floor(point[1] / boxSize);
      const boxKey = `${boxX}_${boxY}`;
      boxes.set(boxKey, true);
   }

   return boxes.size;
}

featureFunctions.getFractalDimension = (paths) => {
   const points = paths.flat();
   const maxBoxSize = Math.max(featureFunctions.getWidth(paths), featureFunctions.getHeight(paths));

   const boxSizes = [];
   let boxSize = maxBoxSize;

   while (boxSize >= 1) {
      boxSizes.push(boxSize);
      boxSize /= 2;
   }

   const counts = boxSizes.map((size) => calculateBoxCount(points, size));
   const logSizes = boxSizes.map((size) => Math.log(1 / size));

   // Use linear regression to estimate the fractal dimension
   const sumLogCounts = counts.reduce((sum, count) => sum + Math.log(count), 0);
   const sumLogSizes = logSizes.reduce((sum, logSize) => sum + logSize, 0);
   const slope = sumLogCounts / sumLogSizes;

   return -slope;
};




   featureFunctions.inUse = [
      //{name:"Path Count",function:featureFunctions.getPathCount},
      //{name:"Point Count",function:featureFunctions.getPointCount},
      { 
         name: "Pixel Array", function: (paths) => {
            return featureFunctions.getPixels(paths, 20) 
         }
      }

      // { name: "Width", function: featureFunctions.getWidth },
      // { name: "Height", function: featureFunctions.getHeight },
      // { name: "Elongation", function: featureFunctions.getElongation },
      // { name: "Roundness", function: featureFunctions.getRoundness },
      // { name: "Complexity", function: featureFunctions.getComplexity },
      // // { name: "Symmetry", function: featureFunctions.getSymmetry },
      // { name: "Average Nearest Neighbor Distance", function: featureFunctions.getAverageNearestNeighborDistance },
      // { name: "Maximum Nearest Neighbor Distance", function: featureFunctions.getMaximumNearestNeighborDistance },
      // //{ name: "Fractal Dimension", function: featureFunctions.getFractalDimension },


   ];


if (typeof module !== "undefined") {
   module.exports = featureFunctions;
}
