import numpy as np
import keras as kr

# percepitron init:
percepitron = kr.models.Sequential()
input = kr.layers.Dense(32, input_shape=[1])


# We need to start by making some synthetic data
# We will need to have a few information per person, for this model to actually be able to show the concept I am going to squish the data to be smaller then it should be
# [rent check per month (rent cost - payed), length of paying such rent(months), salery (gross income per month), current bank balance($$$$), savings ($$$), do you have a gig job?, credit score]

examplePiece = [-2, 12, 1000, 2400, 3000, 0, 500]
anotherExamplePiece = [0, 6, 500, 4000, 1000, 1, 300]

# to create this data we will need to create a function that will create a list of lists
# this function will create a spectrum of data between the lower bound and upper bound of each piece of data
# this function will also create a list of labels for each piece of data, either 0 or 1, which will need to be created in a way that will make the data look like it is a real world example. Not to mention in the real test there has to be a way to acount for bias. No clue how.

exampleOne = np.array(examplePiece)
exampleTwo = np.array(anotherExamplePiece)


def createData(rent, lengthL, lengthU, saleryL, saleryU, bankL, bankU, savingsL, savingsU, creditL, creditU):
    print("hello dog!")


createData(rent=-1000, lengthL=0, lengthU=12, saleryL=0, saleryU=10000,
           bankL=0, bankU=10000, savingsL=0, savingsU=10000, creditL=0, creditU=1000)

# np.savetxt('data.csv', exampleOne, delimiter=',')
# data = np.loadtxt('data.csv', delimiter=',')
# print(data)
