import matplotlib.pyplot as plt
import numpy
from random import randint

def getRVsValueTuple(sampleNumber):

    numberOfOnes = 0;
    numberOfZeros = 0;

    for i in range(0, sampleNumber):
        if randint(1, 4) == 1:
            numberOfOnes += 1;
        else:
            numberOfZeros += 1;
    return (numberOfOnes, numberOfZeros);



def drawCDFofWLLN(N, epoch):

    tempList = [];

    for i in range(0, epoch):

        temp = getRVsValueTuple(N);
        tempList.append(temp);

    zList = [];
    resultList = [];
    probaltiy = 0;

    arverageX = 0.25;
    sigma = pow( 0.25 * 0.75 , 0.5);

    for i in range(0, N + 1):

        tempPro = 0;    
        for j in range(len(tempList)):
            if tempList[j][0] == i:
                tempPro += 1;

        probaltiy += tempPro / float(epoch);
        resultList.append(probaltiy);
        #zList.append( i / float(N));
        tempFU =  i / float(N) - arverageX;
        #zList.append(tempFU);
        zList.append( (tempFU  * pow(N, 0.5)  /  float(sigma) ) );
        #zList.append( ( i / float(N)  - arverageX) * pow(N, 0.5) / float(sigma));

    plt.xlabel('z')
    plt.ylabel('FZn(z)')
    plt.title('n = ' + str(N))
    plt.step(zList, resultList);
    plt.show();

    #print(len(resultList));

drawCDFofWLLN(50, 500);
