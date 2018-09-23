import random
import matplotlib.pyplot as plt

def fun():


    mylist = [0]
    t = 0;
    for j in range(0, 10):
        t += random.expovariate(1);
        mylist.append(t);

    #print(mylist);

    secondList = [0,1,2,3,4,5,6,7,8,9,10]

    plt.xlabel('t');
    plt.ylabel('N(t)');
    plt.title('N = 10' )
    plt.step(mylist, secondList, where = 'post');
    plt.show();

fun()

