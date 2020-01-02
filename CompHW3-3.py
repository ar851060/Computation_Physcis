import math
import matplotlib.pyplot as plt


def get_dt():
    dt_0 = 0.0001
    return dt_0

def Temp(jdx,idx,w,dx):

    xx = jdx*dx
    tt = idx*get_dt()
    if xx==0 and tt==0:
        ans = 1
        return ans
    elif xx==1 and tt!=0:
        ans = 0
        return ans
    elif xx!=0 and tt==0:
        ans = 0
        return ans
    elif tt!=0 and xx==0:
        return math.cos(w*tt)
    elif xx<0:
        ans = 0
        return ans
    elif tt<0:
        ans =0
        return ans
    else:
        ans = Temp(jdx-1,idx,w,dx)+get_dt() * math.pow(dx,-2)*(Temp(jdx-1,idx+1,w,dx)+Temp(jdx-1,idx,w,dx)-2*Temp(jdx-1,idx-1,w,dx))
        return ans

def find_ct():
    w = 2*math.pi
    dx = 0.1
    txp = []
    ttp = []
    style = [":", "--", "o", "-"]
    for jdx in range(6):
        n = jdx * dx
        for idx in range(1, 101):
            if idx % 1000 == 0:
                print("iter : {0}".format(idx))
            i = idx * get_dt()
            res1 = Temp(jdx, idx, w, dx)
            ttp.append(i)
            txp.append(res1)
        if jdx == 5:
            plt.plot(ttp, txp, style[jdx % 4])
            plt.show()

#find_ct()


def test_1():
    w = 2*math.pi
    dx = 0.1
    txp = []
    ttp = []
    for idx in range(11):
        i = idx * get_dt()
        for jdx in range(11):
            res1 = Temp(jdx, idx, w, dx)
            txp.append(res1)
            ttp.append(i)
        plt.plot(ttp, txp)
    plt.show()
    dx = 0.01
    tx = []
    tt = []
    for idx in range(11):
        ii = idx * get_dt()
        for jdx in range(11):
            res2 = Temp(jdx, idx, w, dx)
            tx.append(res2)
            tt.append(ii)
        plt.plot(tt, tx,"--")
    plt.show()


#test_1()

def test_2():
    dx = 0.1
    print('this is the result of w<tc. we suppose w = 0.01, and tc = 1')
    w=0.1
    for idx in range(3):
        i = idx*get_dt()
        for jdx in range(11):
            n = jdx * dx
            resl = Temp(jdx,idx,w,dx)
            print(n,i,resl)
    print('*********')
    print('this is the result of w<tc. we suppose w = 100. ')
    w=10
    for idx in range(3):
        i = idx*get_dt()
        for jdx in range(11):
            n = jdx * dx
            resl = Temp(jdx,idx,w,dx)
            print(n,i,resl)
    print('************')
    print('this is the result of w<tc. we suppose w = 1.')
    w = 1
    for idx in range(3):
        i = idx*get_dt()
        for jdx in range(11):
            n = jdx * dx
            resl = Temp(jdx,idx,w,dx)
            print(n,i,resl)

    return 0

#test_2()

def test_3():
    w = 100
    dx = 0.1
    txp = []
    ttp = []
    style = [":","--","o","-"]
    for jdx in range(1,10):
        n = jdx * dx
        for idx in range(1,101):
            i = idx * get_dt()
            res1 = Temp(jdx, idx, w, dx)
            ttp.append(i)
            txp.append(res1)
        plt.plot(ttp,txp,style[jdx%4])
    plt.show()

    w = 1
    dx = 0.1
    txp = []
    ttp = []
    style = [":", "--", "o", "-"]
    for jdx in range(1,10):
        n = jdx * dx
        for idx in range(1,101):
            i = idx * get_dt()
            res1 = Temp(jdx, idx, w, dx)
            ttp.append(i)
            txp.append(res1)
        plt.plot(ttp, txp, style[jdx % 4])
    plt.show()

    w = 0.01
    dx = 0.1
    txp = []
    ttp = []
    style = [":", "--", "o", "-"]
    for jdx in range(1,10):
        n = jdx * dx
        for idx in range(1,101):
            i = idx * get_dt()
            res1 = Temp(jdx, idx, w, dx)
            ttp.append(i)
            txp.append(res1)
        plt.plot(ttp, txp, style[jdx % 4])
    plt.show()

    return 0

test_3()

