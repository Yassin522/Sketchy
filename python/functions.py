classes = {
    "car": 1,
    "fish": 2,
    "house": 3,
    "tree": 4,
    "bicycle": 5,
    "guitar": 6,
    "pencil": 7,
    "clock": 8, "cloud": 9, "snake": 10,
    "star": 11, "t_shirt": 12, "bucket": 13, "flower": 14, "calculator": 15, "pizza": 16

}


def readFeatureFile(filePath):
    f = open(filePath, 'r')
    lines = f.readlines()

    X = []
    y = []
    for i in range(1, len(lines)):
        row = lines[i].split(",")
        X.append(
            [float(row[j]) for j in range(len(row)-1)]
        )
        y.append(classes[row[-1].strip()])

    return (X, y)
