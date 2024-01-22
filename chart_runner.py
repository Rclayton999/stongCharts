import csv
import matplotlib.pyplot as plt

import numpy


def getData():
    # numpy.zeros()
    repsArr = []
    weights = []
    strData = []

    with open('strong.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            if spamreader.line_num != 1:
                weight = float(row[4]) if len(row[4]) > 0 else 0
                reps = float(row[6]) if len(row[6]) > 0 else 0
                date = row[0].split(" ")[0]
                name = row[2]

                strData.append([date, name])
                weights.append(weight)
                repsArr.append(reps)
        numpyWeights = numpy.array(weights)
        numpyReps = numpy.array(repsArr)

        oneRepMax = numpy.round(numpy.divide(numpyWeights, 1.0278 + (-0.0278 * numpyReps)), decimals=1)

        ORMDict = {}

        for i in range(len(oneRepMax)):
            if strData[i][1] not in ORMDict.keys():
                ORMDict[strData[i][1]] = {}
            if strData[i][0] not in ORMDict[strData[i][1]].keys() or ORMDict[strData[i][1]][strData[i][0]] < oneRepMax[i]:
                if(oneRepMax[i]) == 0:
                    ORMDict[strData[i][1]][strData[i][0]] = numpyReps[i]
                else:
                    ORMDict[strData[i][1]][strData[i][0]] = oneRepMax[i]

        return ORMDict

def plotData(data):
    for key in data.keys():
        lst = [(x, data[key][x]) for x in data[key]]
        xaxis = numpy.take(numpy.array(lst), 0, axis=1)
        yaxis = numpy.take(numpy.array(lst), 1, axis=1)
        print(key, yaxis)
        plt.scatter(numpy.array(xaxis, dtype=numpy.datetime64), numpy.array(yaxis, dtype=numpy.float_), label=key)

        plt.title(key)
        plt.savefig('./plots/' + key.strip("\"") + '.png')
        plt.close()

if __name__ == '__main__':

        plotData(getData())
