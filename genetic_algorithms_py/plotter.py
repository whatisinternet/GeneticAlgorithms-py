import matplotlib.pyplot as plt
from decimal import *

def chart(target, function_name="test"):
    f = open('./data/fitness_data{a}.csv'.format(a=function_name), 'r')
    data = f.readlines()
    fig = plt.figure()

    for i in data:
        split_input = i.split(",")
        y = (Decimal(split_input[0]))
        x = (Decimal(split_input[1].strip()))
        plt.scatter(x, y, color="#085DAD",
                    label=y, alpha=0.3, edgecolors='none')

    plt.axes().set_ylabel("Value")
    plt.axes().set_xlabel("Fitness")
    plt.grid(True)
    # plt.show()

    fig.savefig("images/{a}.png".format(a=function_name))
