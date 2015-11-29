import matplotlib.pyplot as plt
import pylab

def save_fitnesses(data):
    x = list(map(lambda x: int(x['seed'], 2), data))
    y = list(map(lambda x: x['weight'], data))
    f = open('./fitness_data.csv', 'a+')

    for i in range(len(x)):
        f.write("{a},{b}\n".format(a=x[i], b=y[i]))

def chart(target, function_name = "test"):
    f = open('./fitness_data.csv','r')
    data = f.readlines()

    for i in data:
        split_input = i.split(",")
        y = (int(split_input[0]))
        x = (int(split_input[1].strip()))
        plt.scatter(x,y, color="#085DAD", label=y, alpha=0.3, edgecolors='none')

    plt.axhline(int(target,2), color="red")

    plt.axes().set_ylabel("Value")
    plt.axes().set_xlabel("Fitness")
    plt.grid(True)
    plt.show()

    plt.savefig("{a}.png".format(a=function_name))





