import matplotlib.pyplot as plt
import numpy as np

def f1():
    print(f'This is f1')

def f2():
    print(f'This is f2')

def f3():
    x = np.linspace(0, 20, 100)
    plt.plot(x, np.sin(x))
    plt.show(block=False)
    input('press <ENTER> to continue')