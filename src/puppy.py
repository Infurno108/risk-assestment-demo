
import numpy as np
import keras as kr
import random as r
np.set_printoptions(suppress=True)

# simple prototype of the prototype
# the only inputs it will take are (monthly rent overflow (rent cost - rent payd), salery ($/month), current bank amount ($))


# will create two lists, 1: [[rent, salery, bank], ...] 2: [yes,no,yes,yes,...] return both as a single list
def createData():
    data = []
    labels = []
    for i in range(0, 25000):
        yesNo = 0
        rent = r.randint(-1000, 500)
        if (rent > 0):
            rent = 0
        salery = r.randint(1000, 8000)
        bank = r.randint(0, 10000)
        if (((bank + salery) + (rent * 20)) > 0):  # this is where human tuning is needed
            yesNo = 1
        data.append([int(rent), int(salery), int(bank)])
        labels.append(yesNo)
    data = np.array(data)
    labels = np.array(labels)
    np.savetxt('labels.csv', labels, delimiter=',')
    np.savetxt('people.csv', data, delimiter=',')


# createData()

riskyBusiness = kr.models.Sequential()
# input layer of size 3 with a hidden layer of 16
riskyBusiness.add(kr.layers.Dense(16, input_dim=3, activation='relu'))
riskyBusiness.add(kr.layers.Dense(16, activation='relu'))
# output layer of size 1 to have a simple binary yes or no
riskyBusiness.add(kr.layers.Dense(1))

riskyBusiness.compile(loss='mean_squared_error',
                      optimizer='adam',
                      metrics=['binary_accuracy'])

data = np.loadtxt('people.csv', delimiter=',')
labels = np.loadtxt('labels.csv', delimiter=',')

# riskyBusiness.fit(data, labels, epochs=1000)

# riskyBusiness.save('riskyBusiness.h5')

runningModel = kr.models.load_model('riskyBusiness.h5')

x = 29
print(runningModel.predict(data[x].reshape(1, 3)))
print(labels[x])

for i in range(100, 400):
    totalFails = 0
    if (int(runningModel.predict(data[i].reshape(1, 3))) != labels[i]):
        print(i)
        totalFails += 1
print("fails: ", totalFails)
