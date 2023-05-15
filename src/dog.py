
import numpy as np
import keras as kr
import random as r
import tensorflowjs as tfjs
np.set_printoptions(suppress=True)

# simple prototype of the prototype
# the only inputs it will take are (monthly rent overflow (rent cost - rent payd), salary ($/month), current bank amount ($))
# rent check per month (rent cost - payed), length of paying such rent(months), salary (gross income per month), current bank balance($$$$), savings ($$$), do you have a gig job?, credit score]

# will create two lists, 1: [[rent, salary, bank], ...] 2: [yes,no,yes,yes,...] return both as a single list


# rent, length, salary, bank, savings, gig,

def createData():
    data = []
    labels = []
    for i in range(0, 25000):
        yesNo = 0
        rent = r.randint(-1000, 500)
        if (rent > 0):
            rent = 0
        salary = r.randint(1000, 8000)
        bank = r.randint(0, 5000)
        lengthofRent = r.randint(0, 24)
        savings = r.randint(0, 10000)
        gigJob = r.randint(0, 1)
        # this is where human tuning is needed
        if (((lengthofRent*rent) + (bank + salary + savings) + (rent * 20) + ((salary/2)*gigJob) > 0)):
            yesNo = 1
        data.append([rent, salary, bank, lengthofRent, savings, gigJob])
        labels.append(yesNo)
    data = np.array(data)
    labels = np.array(labels)
    np.savetxt('labels.csv', labels, delimiter=',')
    np.savetxt('people.csv', data, delimiter=',')


riskyBusiness = kr.models.Sequential()
# input layer of size 3 with a hidden layer of 16
riskyBusiness.add(kr.layers.Dense(30, input_dim=6, activation='relu'))
riskyBusiness.add(kr.layers.Dense(30, activation='relu'))
# output layer of size 1 to have a simple binary yes or no
riskyBusiness.add(kr.layers.Dense(1))

riskyBusiness.compile(loss='mean_squared_error',
                      optimizer='adam',
                      metrics=['binary_accuracy'])

data = np.loadtxt('people.csv', delimiter=',')
labels = np.loadtxt('labels.csv', delimiter=',')


def trainModel():
    riskyBusiness.fit(data, labels, epochs=1000)
    riskyBusiness.save('riskyBusiness.h5')
    tfjs.converters.save_keras_model(riskyBusiness, 'dog.json')


def runModel():
    runningModel = kr.models.load_model('riskyBusiness.h5')
    for i in range(0, 10):
        print("prediction: ", runningModel.predict(
            data[i].reshape(1, 6)), "actual: ", labels[i], "step: ", i)
        totalFails = 0
        if (int(runningModel.predict(data[i].reshape(1, 6))) != labels[i]):
            totalFails += 1
    print("fails: ", totalFails)


# createData()
# trainModel()
# runModel()
runningModel = kr.models.load_model('riskyBusiness.h5')

