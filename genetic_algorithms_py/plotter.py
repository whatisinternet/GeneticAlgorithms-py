import matplotlib.pyplot as plt

def chart(target, function_name="test"):
    f = open('./fitness_data.csv', 'r')
    data = f.readlines()
    fig = plt.figure()

    for i in data:
        split_input = i.split(",")
        y = (int(split_input[0]))
        x = (int(split_input[1].strip()))
        plt.scatter(x, y, color="#085DAD",
                    label=y, alpha=0.3, edgecolors='none')

    plt.axes().set_ylabel("Value")
    plt.axes().set_xlabel("Fitness")
    plt.grid(True)
    plt.show()

    fig.savefig("{a}.png".format(a=function_name))
