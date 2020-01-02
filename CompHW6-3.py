import matplotlib.pyplot as plt
import numpy as np
import math
import pdb

acc = 0.01 #In the second question,the answer of accuracy are 0.01

def delta(x,y,w,gu): #Newton method; This function is create the delta
    s = math.sin(w*gu)
    c = math.cos(w*gu)
    ans = (pow(gu,2)+2*x*c+2*y*s-pow(x,2)-pow(y,2)-1)/(2*gu-2*w*x*s+2*w*y*c)
    return ans

def test_1():
    w=0.1
    degu = 0
    tret = np.zeros((51,51))
    xx = []
    for idx in range(51): #create the grid from x=-10~10
        x = -10+0.4*idx
        xx.append(x)
        for jdx in range(51): #create the grid from y=-10~10
            y = -10+0.4*jdx
            gu = -10
            i = 1
            while i >=0:
                gu-= degu
                temp = delta(x, y, w, gu)
                if abs(temp)>acc: #check delta accuracy
                    degu = temp
                else:
                    i = -1
            tret[idx, jdx] = gu
    plt.plot(xx,tret[:,25])
    plt.title("6-3-a\nwhen w = 0.1")
    plt.xlabel("x")
    plt.ylabel("t_ret")
    plt.show()
#test_1()

def test_2():
    w=0.9
    degu = 0
    tret = np.zeros((51,51))
    xx = []
    for idx in range(51):
        x = -10+0.4*idx
        xx.append(x)
        for jdx in range(51):
            y = -10+0.4*jdx
            gu = -10
            i = 1
            while i >=0:
                gu-= degu
                temp = delta(x, y, w, gu)
                if abs(temp)>acc:
                    degu = temp
                else:
                    i = -1
            tret[idx,jdx] = gu
    plt.plot(xx,tret[:,25])
    plt.title("6-3-a\nwhen w = 0.9")
    plt.xlabel("x")
    plt.ylabel("t_ret")
    plt.show()
#test_2()

def potential(x,y,w,tret,mu):#calculate the potential
    c = math.cos(w*tret)
    s = math.sin(w*tret)
    RU = tret-x*w*s+y*w*c
    if mu == 0: #electric potential
        ans = -1/RU
    elif mu == 1: #magnetic potential in x
        ans = (w*s)/RU
    elif mu == 2: #magnetic potential in y
        ans = -(w*c)/RU
    else:
        print("error")
        pdb.set_trace()
    return ans

def test_3():
    w = 0.1
    degu = 0
    A0 = np.zeros((51,51))
    Ax = np.zeros((51,51))
    Ay = np.zeros((51,51))
    for idx in range(51): #create the grid from x=-10~10
        x = -10 + 0.4 * idx
        for jdx in range(51): #create the grid from y=-10~10
            y = -10 + 0.4 * jdx
            gu = -10
            i = 1
            while i >= 0:
                gu -= degu
                temp = delta(x, y, w, gu)
                if abs(temp) > acc:
                    degu = temp
                else:
                    i = -1
            A0[idx, jdx] = potential(x, y, w, gu, 0)
            Ax[idx, jdx] = potential(x, y, w, gu, 1)
            Ay[idx, jdx] = potential(x, y, w, gu, 2)

    bb = plt.contourf(A0, cmap=plt.cm.hot)
    plt.colorbar(bb, orientation="vertical")
    plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.title("6-3-b\nElectric potential when w = 0.1")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    plt.quiver(Ax,Ay)
    plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.title("6-3-b\nMagnetic potential when w = 0.1")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
#test_3()

def test_4():
    w = 0.9
    degu = 0
    A0 = np.zeros((51,51))
    Ax = np.zeros((51,51))
    Ay = np.zeros((51,51))
    for idx in range(51):
        x = -10 + 0.4 * idx
        for jdx in range(51):
            y = -10 + 0.4 * jdx
            gu = -10
            i = 1
            while i >= 0:
                gu -= degu
                temp = delta(x, y, w, gu)
                if abs(temp) > acc:
                    degu = temp
                else:
                    i = -1
            A0[idx, jdx] = potential(x, y, w, gu, 0)
            Ax[idx, jdx] = potential(x, y, w, gu, 1)
            Ay[idx, jdx] = potential(x, y, w, gu, 2)

    bb = plt.contourf(A0, cmap=plt.cm.hot)
    plt.colorbar(bb, orientation="vertical")
    plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.title("6-3-b\nElectric potential when w = 0.9")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    plt.quiver(Ax,Ay)
    plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.title("6-3-b\nMagnetic potential when w = 0.9")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
#test_4()

def Efield(x,y,w,tret,mu,fi): #calculate electric field
    c = math.cos(w * tret)
    s = math.sin(w * tret)
    a = w*(c*y-x*s)/tret
    if mu == 1: #Ex
        m = ((x-c)/tret)+w*s
        if fi == 1: #near field
            ans = (((1-pow(w,2))*m)/(pow(tret,2)*pow((1-a),3)))
        else: #far field
            ans =(a * m / (tret * pow((1 - a), 3))) + (pow(w, 2) * c / (tret * pow((1 - a), 2)))
    elif mu == 2: #Ey
        m = ((y-s)/tret)-w*c
        if fi ==1: #near field
            ans = (((1 - pow(w, 2)) * m) / (pow(tret, 2) * pow((1 - a), 3)))
        else: #far field
            ans = (a * m / (tret * pow((1 - a), 3))) + (pow(w, 2) * s / (tret * pow((1 - a), 2)))
    else:
        print("error")
        pdb.set_trace()
    return ans

def test_5():
    w = 0.1
    degu = 0
    Exn = np.zeros((51, 51))
    Exf = np.zeros((51, 51))
    Eyn = np.zeros((51, 51))
    Eyf = np.zeros((51, 51))
    for idx in range(51): #grid x=-10~10
        x = -10 + 0.4 * idx
        for jdx in range(51): #grid y=-10~10
            y = -10 + 0.4 * jdx
            gu = -10
            i = 1
            while i >= 0:
                gu -= degu
                temp = delta(x, y, w, gu)
                if abs(temp) > acc: #check the accuracy of delta
                    degu = temp
                else:
                    i = -1
            tempxn = Efield(x, y, w, gu, 1,1)
            tempxf = Efield(x, y, w, gu, 1, 2)
            tempyn = Efield(x, y, w, gu, 2,1)
            tempyf = Efield(x, y, w, gu, 2, 2)
            Exn[idx,jdx] = tempxn
            Exf[idx, jdx] = tempxf
            Eyn[idx, jdx] = tempyn
            Eyf[idx, jdx] = tempyf

    plt.quiver(Exn, Eyn)
    plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.title("6-3-c\nElectric near field in w = 0.1")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    plt.quiver(Exf, Eyf)
    plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.title("6-3-c\nElectric far field in w = 0.1")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

test_5()

def test_6():
    w = 0.9
    degu = 0
    Exn = np.zeros((51, 51))
    Exf = np.zeros((51, 51))
    Eyn = np.zeros((51, 51))
    Eyf = np.zeros((51, 51))
    for idx in range(51):
        x = -10 + 0.4 * idx
        for jdx in range(51):
            y = -10 + 0.4 * jdx
            gu = -10
            i = 1
            while i >= 0:
                gu -= degu
                temp = delta(x, y, w, gu)
                if abs(temp) > acc:
                    degu = temp
                else:
                    i = -1
            tempxn = Efield(x, y, w, gu, 1, 1)
            tempxf = Efield(x, y, w, gu, 1, 2)
            tempyn = Efield(x, y, w, gu, 2, 1)
            tempyf = Efield(x, y, w, gu, 2, 2)
            Exn[idx, jdx] = tempxn
            Exf[idx, jdx] = tempxf
            Eyn[idx, jdx] = tempyn
            Eyf[idx, jdx] = tempyf

    plt.quiver(Exn, Eyn)
    plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.title("6-3-c\nElectric near field in w = 0.9")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    plt.quiver(Exf, Eyf)
    plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.title("6-3-c\nElectric far field in w = 0.9")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

test_6()