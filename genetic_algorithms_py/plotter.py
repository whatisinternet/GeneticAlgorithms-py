import matplotlib.pyplot as plt
import reproduction


def save_fitnesses(data, number_of_variables):
    if _is_debugging():
        x = list(map(lambda x:
                    reproduction._build_params(x['seed'], 0, number_of_variables),
                    data))
        y = list(map(lambda x: x['weight'], data))
        f = open('./fitness_data.csv', 'a+')

        for i in range(len(x)):
            for idx in range(len(x[i])):
                f.write("{a},{b}\n".format(a=int(x[i][idx], 2), b=y[i]))


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

def _is_debugging():
    f = open('./debug', 'r')
    debug = f.readline()
    if debug == "True\n":
        return True
    else:
        return False
