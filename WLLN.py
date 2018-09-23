import matplotlib.pyplot as plt
import numpy
from random import randint


'''
函数功能：模拟概率，Pr{X == 1} = 0.25, Pr{X == 0} = 0.75
'''
def getRVsValueTuple(sampleNumber):

    numberOfOnes = 0;
    numberOfZeros = 0;

    for i in range(0, sampleNumber):
        if randint(1, 4) == 1:
            numberOfOnes += 1;
        else:
            numberOfZeros += 1;
    return (numberOfOnes, numberOfZeros);

'''
N表示随机数的数量 X1 X2 ... XN
epoch 表示进行实验的次数
代码中使用epoch次实验的平均情况表示Zn的概率分布
'''
def drawCDFofWLLN(N, epoch):

    tempList = [];

    for i in range(0, epoch):

        temp = getRVsValueTuple(N);
        tempList.append(temp);

    zList = [];
    resultList = [];
    probaltiy = 0;

    for i in range(0, N + 1):

        tempPro = 0;    
        for j in range(len(tempList)):
            if tempList[j][0] == i:
                tempPro += 1;

        probaltiy += tempPro / float(epoch);
        resultList.append(probaltiy);
        zList.append( i / float(N));

    plt.xlabel('z')
    plt.ylabel('FZn(z)')
    plt.title('n = ' + str(N))
    plt.step(zList, resultList);
    plt.show();

### 画图
drawCDFofWLLN(1000, 1000);
