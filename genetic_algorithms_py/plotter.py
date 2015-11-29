import matplotlib.pyplot as plt
import pylab

def save_fitnesses(data):
    x = list(map(lambda x: int(x['seed'], 2), data))
    y = list(map(lambda x: x['weight'], data))
    f = open('./fitness_data.csv', 'a+')

    for i in range(len(x)):
        f.write("{a},{b}\n".format(a=x[i], b=y[i]))

def chart(target):
    f = open('./fitness_data.csv','r')
    data = f.readlines()

    x = []
    y = []
    for i in data:
        split_input = i.split(",")
        x.append(int(split_input[0]))
        y.append(int(split_input[1].strip()) / 100)

    plt.scatter(x,y)

    plt.show()

    plt.savefig('tests.png')





