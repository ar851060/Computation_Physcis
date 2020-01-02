import matplotlib.pyplot as plt
import numpy as np
import math

acc = 0.01

def analytic(ry,t):
    ans = ((2*t-ry)+math.sqrt(4*pow(ry,2)+pow(t,2)-4*ry*t+3))/1.5
    if ans >t:
        ans = ((2 * t - ry) - math.sqrt(4 * pow(ry, 2) + pow(t, 2) - 4 * ry * t + 3)) / 1.5
    return ans

def delta(ry,t,gu):
    ans = (0.75*pow(gu,2)+(ry-2*t)*gu+pow(t,2)-pow(ry,2)-1)/(1.5*gu+ry-2*t)
    return ans

def test_1():
    ry = 1
    degu = 0
    ana = []
    new = []
    tt = []
    for idx in range(21):
        t = -10+idx
        tempa = analytic(ry,t)
        temp = t-tempa
        ana.append(temp)
        tt.append(t)

    for jdx in range(21):
        idx = 1
        t = -10 + jdx
        gu = t-10
        while idx>=0:
            gu -= degu
            tempnew = delta(ry,t,gu)
            if abs(tempnew) > acc:
                degu = tempnew
            else:
                idx = -1
        temp = t-gu
        new.append(temp)
    plt.plot(tt, new, "o", label="$Newton$")
    plt.plot(tt, ana, "r", label="$Analytic$")
    plt.title("6-2\nwhen r = (1,1)")
    plt.xlabel("t")
    plt.ylabel("t-t_ret")
    plt.legend()
    plt.show()

test_1()

def test_2():
    ry = 0
    degu = 0
    ana = []
    new = []
    tt = []
    for idx in range(21):
        t = -10+idx
        tempa = analytic(ry,t)
        temp = t-tempa
        ana.append(temp)
        tt.append(t)

    for jdx in range(21):
        idx = 1
        t = -10 + jdx
        gu = t-10
        while idx>=0:
            gu -= degu
            tempnew = delta(ry,t,gu)
            if abs(tempnew) > acc:
                degu = tempnew
            else:
                idx = -1
        temp = t-gu
        new.append(temp)

    plt.plot(tt, new, "o", label="$Newton$")
    plt.plot(tt, ana, "r", label="$Analytic$")
    plt.title("6-2\nwhen r = (1,0)")
    plt.xlabel("t")
    plt.ylabel("t-t_ret")
    plt.legend()
    plt.show()

test_2()

def test_3():
    ry = -1
    degu = 0
    ana = []
    new = []
    tt = []
    for idx in range(21):
        t = -10+idx
        tempa = analytic(ry,t)
        temp = t-tempa
        ana.append(temp)
        tt.append(t)

    for jdx in range(21):
        idx = 1
        t = -10 + jdx
        gu = t-10
        while idx>=0:
            gu -= degu
            tempnew = delta(ry,t,gu)
            if abs(tempnew) > acc:
                degu = tempnew
            else:
                idx = -1
        temp = t - gu
        new.append(temp)

    plt.plot(tt,new,"o",label = "$Newton$")
    plt.plot(tt, ana, "r", label="$Analytic$")
    plt.title("6-2\nwhen r = (1,-1)")
    plt.xlabel("t")
    plt.ylabel("t-t_ret")
    plt.legend()
    plt.show()

test_3()

