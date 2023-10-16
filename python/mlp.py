from functions import readFeatureFile
from sklearn.neural_network import MLPClassifier
hidden = (100,100)
mlp = MLPClassifier(
   hidden,
   max_iter=10000,
   random_state=1,
   activation='tanh'
)

X, y = readFeatureFile("C:\\Users\\Mahmoud\\Desktop\\study\\Project2\\New folder (2)\\New folder2\\drawing_ml\\data\\dataset\\training.csv")

mlp.fit(X, y)

X, y = readFeatureFile("C:\\Users\\Mahmoud\\Desktop\\study\\Project2\\New folder (2)\\New folder2\\drawing_ml\\data\\dataset\\testing.csv")

accuracy = mlp.score(X, y)
print("Accuracy:", accuracy)

classes = ["car", "fish", "house", "tree", "bicycle", "guitar", "pencil", "clock", "cloud", "snake", "star", "t_shirt", "bucket", "flower", "calculator", "pizza"]

jsonObj = {
    "neuronCounts": [len(X[0]), hidden, len(classes)],
    "classes": classes,
    "network": {
        "levels": []
    }
}

for i in range(0, len(mlp.coefs_)):
    level = {
        "weights": mlp.coefs_[i].tolist(),
        "biases": mlp.intercepts_[i].tolist(),
        "inputs": [0]*len(mlp.coefs_[i]),
        "outputs": [0]*len(mlp.intercepts_[i])
    }
    jsonObj["network"]["levels"].append(level)

import json
json_object = json.dumps(jsonObj, indent=2)

with open("C:\\Users\\Mahmoud\\Desktop\\study\\Project2\\New folder (2)\\New folder2\\drawing_ml\\data\\models\\model.json", "w") as outfile:
    outfile.write(json_object)
with open("C:\\Users\\Mahmoud\\Desktop\\study\\Project2\\New folder (2)\\New folder2\\drawing_ml\\common\\js_objects\\model.js", "w") as outfile:
    outfile.write("const model = "+json_object+";")
