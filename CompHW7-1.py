import matplotlib.pyplot as plt
import numpy as np
import math

def h(n): #create bins
    a = -10
    b = 10
    ans = (b-a)/pow(2,n)
    return ans

Fun = lambda x: math.exp(-pow(x,2))/(pow(10,-3)+pow(x,2)) #Voigt integration

def test_1():
    tempans = []
    nn = []
    ii = []
    ndx = 0
    err = 1
    while err > pow(10,-3): #accuracy
        nn.append(ndx)
        limi = pow(2,ndx)+1
        for idx in range(limi):
            x = -10+h(ndx)*idx
            temp = Fun(x)
            tempans.append(temp)
        tempsum = (sum(tempans)-0.5*tempans[0]-0.5*tempans[-1])*h(ndx) #Trapezoidal method
        ii.append(tempsum)
        print(tempsum)
        if ndx >3:
            err = abs((ii[ndx]-ii[ndx-1])/ii[ndx])
        ndx+=1
    print(ndx)
    plt.plot(nn,ii)
    plt.title("f(h) v.s. n\nin Trapezoidal method")
    plt.xlabel("n")
    plt.ylabel("f(h)")
    plt.show()

#test_1()

def test_2():
    tempans = []
    nn = []
    ii = np.zeros(1000)
    rr = []
    kdx = 0
    err = 1
    while err>pow(10,-3):
        nn.append(kdx)
        num = kdx
        for ndx in range(num+1): #Trapezoidal method
            limi = pow(2, ndx) + 1
            for idx in range(limi):
                x = -10 + h(ndx) * idx
                temp = Fun(x)
                tempans.append(temp)
            tempsum = (sum(tempans) - 0.5 * tempans[0] - 0.5 * tempans[-1]) * h(ndx)
            ii[ndx] = tempsum
        while(num!=0): #Romberg method
            jj = 1
            for idx in range(1,num+1): #R
                tempr = ii[idx]+(ii[idx]-ii[idx-1])/(pow(4,jj)-1)
                ii[idx-1] = tempr
            num -=1
            jj+=1
        rr.append(ii[0])
        print(ii[0])
        if kdx!=0:
            err = abs((rr[kdx]-rr[kdx-1])/rr[kdx])
        kdx+=1
    print(kdx)
    plt.plot(nn, rr)
    plt.title("f(h) v.s. n\nin Romberg integration method")
    plt.xlabel("n")
    plt.ylabel("f(h)")
    plt.show()

#test_2()