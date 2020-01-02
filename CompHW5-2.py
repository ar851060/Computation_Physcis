import matplotlib.pyplot as plt
import numpy as np
import math
import pdb

def phi(i,j,k,n,pp,h):
    tau = pow(h, 2) / 6 #I suppose tau = (h^2)/6
    t = n*tau
    xi =int(round((0.5-i)/h))
    yj =int(round((0.5-j)/h))
    zk =int(round((0.5-k)/h))
    if i == 0 and j == 0  and k == 0: # At the origin, there is a charge. I use Poisson equation here.
        ans = (pp[xi + 1, yj, zk, n - 1] + pp[xi - 1, yj, zk, n - 1] + pp[xi, yj + 1, zk, n - 1] + pp[
            xi, yj - 1, zk, n - 1] + pp[xi, yj, zk + 1, n - 1] + pp[xi, yj, zk - 1, n - 1]+(1*h*h)) / 6
    elif i == 0.5 or i == -0.5 or j == 0.5 or j == -0.5 or k == 0.5 or k == -0.5: #Boundary condition
        ans = 0
    elif t==0: #Initial condition
        ans = 0
    else: #other place in box, I use Laplace equation to solve.
        ans = (pp[xi+1,yj,zk,n-1]+pp[xi-1,yj,zk,n-1]+pp[xi,yj+1,zk,n-1]+pp[xi,yj-1,zk,n-1]+pp[xi,yj,zk+1,n-1]+pp[xi,yj,zk-1,n-1])/6
    return ans

def test_1():
    h = 0.1 #the space span is 0.1
    pp = np.zeros((11,11,11,101))
    for ndx in range(101): # 100 steps
        n = ndx
        for kdx in range(11): # 10 steps on z-axis
            k = 0.5-kdx*h # calculate the real distance
            for jdx in range(11):# 10 steps on y-axis
                j = 0.5-jdx*h # calculate the real distance
                for idx in range(11):# 10 steps on x-axis
                    i = 0.5-idx*h # calculate the real distance
                    temp = phi(i,j,k,n,pp,h)
                    pp[idx, jdx, kdx, ndx] = temp
        if ndx%10 == 0:
            plt.plot(pp[5,5,:,ndx]) # plot phi(0,0,z) on 99 steps
            plt.xticks([0,2.5,5,7.5,10],[-0.5,-0.25,0,0.25,0.5])
            plt.title("figure 1-1\nphi(0,0,z) on 10*10*10 grid")
            plt.xlabel("z")
            plt.show()
    return 0

#test_1()

def test_2():
    h = 0.01 #the space span is 0.01
    pp = np.zeros((101, 101, 101, 101))
    for ndx in range(101):# 100 steps on time
        n = ndx
        for kdx in range(101):# 100 steps on z-axis
            k = 0.5 - kdx * h
            for jdx in range(101):# 100 steps on y-axis
                j = 0.5 - jdx * h
                for idx in range(101):# 100 steps on x-axis
                    i = 0.5 - idx * h
                    temp = phi(i, j, k, n, pp, h)
                    pp[idx, jdx, kdx, ndx] = temp
        if ndx%10==0:
            plt.plot(pp[50, 50, :, ndx])
            plt.xticks([0, 25, 50, 75, 100], [-0.5, -0.25, 0, 0.25, 0.5])
            plt.title("figure 1-2\nphi(0,0,z) on 100*100*100 grid")
            plt.xlabel("z")
            plt.show()

    return 0

#test_2()

def test_3():
    h = 0.1
    pp = np.zeros((11,11,11,101))
    for ndx in range(101):
        n = ndx
        for kdx in range(11):
            k = 0.5-kdx*h
            for jdx in range(11):
                j = 0.5-jdx*h
                for idx in range(11):
                    i = 0.5-idx*h
                    temp = phi(i,j,k,n,pp,h)
                    pp[idx, jdx, kdx, ndx] = temp
    deltatemp =0
    deltamax = 0
    colmax = []

    for ndx in range(1,101):
        for jdx in range(11):
            for idx in range(11):
                for kdx in range(11):
                    if pp[idx,jdx,kdx,ndx]!=0 or pp[idx,jdx,kdx,ndx-1]!=0:
                        deltatemp = (pp[idx, jdx, kdx, ndx] - pp[idx, jdx, kdx, ndx - 1])/pp[idx, jdx, kdx, ndx - 1]
                    if deltatemp > deltamax:
                        deltamax = deltatemp
        print(ndx)
        print(deltamax)
        colmax.append(deltamax)
        deltamax = 0
    plt.plot(colmax)
    plt.title("error v.s. iteration")
    plt.xlabel("iteration")
    plt.ylabel("error")
    plt.show()
    plt.loglog(colmax)
    plt.title("log(error) v.s. log(iteration)")
    plt.xlabel("log(iteration)")
    plt.ylabel("log(error)")
    plt.show()


    return 0

#test_3()

def phi_2(i,j,k,n,pp,h):
    tau = pow(h, 2) / 6
    t = n*tau
    xi = int(round((0.5 - i) / h))
    yj = int(round((0.5 - j) / h))
    zk = int(round((0.5 - k) / h))
    if i == 0.5 or i == -0.5 or j == 0.5 or j == -0.5 or k == 0.5 or k == -0.5:
        if i<-0.5 or i>0.5 or j<-0.5 or j>0.5 or k<-0.5 or k>0.5 :
            if t == 0:
                ans = 0
            elif i>=1.5 or i<=-1.5 or j>=1.5 or j<=-1.5 or k>=1.5 or k<=-1.5:
                ans =0
            else:
                ans = (pp[xi + 1, yj, zk, n - 1] + pp[xi - 1, yj, zk, n - 1] + pp[xi, yj + 1, zk, n - 1] + pp[
                    xi, yj - 1, zk, n - 1] + pp[xi, yj, zk + 1, n - 1] + pp[xi, yj, zk - 1, n - 1]) / 6
        elif i<-0.5 or i>0.5 or j<-0.5 or j>0.5 or k<-0.5 or k>0.5:
            ans = (pp[xi+1,yj,zk,n-1]+pp[xi-1,yj,zk,n-1]+pp[xi,yj+1,zk,n-1]+pp[xi,yj-1,zk,n-1]+pp[xi,yj,zk+1,n-1]+pp[xi,yj,zk-1,n-1])/6
        else:#source term
            ans = (1)/(math.sqrt(pow(i,2)+pow(j,2)+pow(k,2)))
    elif t==0:# initial condition
        ans = 0
    #boundary term
    elif k >= 1.5:
        if j >= 1.5:
            if i>=1.5:
                ans = (pp[xi + 1, yj, zk, n - 1] + pp[
                    xi, yj + 1, zk, n - 1] + pp[xi, yj, zk + 1, n - 1]) / 6
            elif i<=-1.5:
                ans =(pp[xi - 1, yj, zk, n - 1]  + pp[
                    xi, yj + 1, zk, n - 1]  + pp[xi, yj, zk + 1, n - 1]) / 6
            else :
                ans =(pp[xi + 1, yj, zk, n - 1] + pp[xi - 1, yj, zk, n - 1] + pp[
                    xi, yj + 1, zk, n - 1]  + pp[xi, yj, zk + 1, n - 1]) / 6
        elif j<=-1.5:
            if i>=1.5:
                ans =( pp[xi + 1, yj, zk, n - 1] + pp[xi, yj - 1, zk, n - 1]  + pp[xi, yj, zk + 1, n - 1]) / 6
            elif i<=-1.5:
                ans =(pp[xi - 1, yj, zk, n - 1] + pp[xi, yj - 1, zk, n - 1] + pp[xi, yj, zk + 1, n - 1]) / 6
            else:
                ans = (pp[xi + 1, yj, zk, n - 1] + pp[xi - 1, yj, zk, n - 1] + pp[xi, yj - 1, zk, n - 1]  + pp[xi, yj, zk + 1, n - 1]) / 6
        elif i>=1.5:
            ans = (pp[xi + 1, yj, zk, n - 1] + pp[xi, yj + 1, zk, n - 1] + pp[
                xi, yj - 1, zk, n - 1]  + pp[xi, yj, zk + 1, n - 1]) / 6
        elif i <=-1.5:
            ans = (pp[xi - 1, yj, zk, n - 1] + pp[xi, yj + 1, zk, n - 1] + pp[
                xi, yj - 1, zk, n - 1] + pp[xi, yj, zk + 1, n - 1]) / 6
        else:
            ans = (pp[xi + 1, yj, zk, n - 1] + pp[xi - 1, yj, zk, n - 1] + pp[xi, yj + 1, zk, n - 1] + pp[
                xi, yj - 1, zk, n - 1] + pp[xi, yj, zk+ 1, n - 1]) / 6
    elif k <= -1.5:
        if j >= 1.5:
            if i>=1.5:
                ans = (pp[xi + 1, yj, zk, n - 1] + pp[
                    xi, yj + 1, zk, n - 1] + pp[xi, yj, zk - 1, n - 1]) / 6
            elif i<=-1.5:
                ans =(pp[xi - 1, yj, zk, n - 1]  + pp[
                    xi, yj + 1, zk, n - 1]  + pp[xi, yj, zk - 1, n - 1]) / 6
            else :
                ans =(pp[xi + 1, yj, zk, n - 1] + pp[xi - 1, yj, zk, n - 1] + pp[
                    xi, yj + 1, zk, n - 1]  + pp[xi, yj, zk - 1, n - 1]) / 6
        elif j<=-1.5:
            if i>=1.5:
                ans =( pp[xi + 1, yj, zk, n - 1] + pp[xi, yj - 1, zk, n - 1]  + pp[xi, yj, zk - 1, n - 1]) / 6
            elif i<=-1.5:
                ans =(pp[xi - 1, yj, zk, n - 1] + pp[xi, yj - 1, zk, n - 1] + pp[xi, yj, zk - 1, n - 1]) / 6
            else:
                ans = (pp[xi + 1, yj, zk, n - 1] + pp[xi - 1, yj, zk, n - 1] + pp[xi, yj - 1, zk, n - 1]  + pp[xi, yj, zk - 1, n - 1]) / 6
        elif i>=1.5:
            ans = (pp[xi + 1, yj, zk, n - 1] + pp[xi, yj + 1, zk, n - 1] + pp[
                xi, yj - 1, zk, n - 1]  + pp[xi, yj, zk - 1, n - 1]) / 6
        elif i <=-1.5:
            ans = (pp[xi - 1, yj, zk, n - 1] + pp[xi, yj + 1, zk, n - 1] + pp[
                xi, yj - 1, zk, n - 1] + pp[xi, yj, zk - 1, n - 1]) / 6
        else:
            ans = (pp[xi + 1, yj, zk, n - 1] + pp[xi - 1, yj, zk, n - 1] + pp[xi, yj + 1, zk, n - 1] + pp[
                xi, yj - 1, zk, n - 1] + pp[xi, yj, zk - 1, n - 1]) / 6
    elif i>=1.5 or i<=-1.5 or j>=1.5 or j<=-1.5 or k>=1.5 or k<=-1.5:
        ans = 0
    else:
        ans = (pp[xi+1,yj,zk,n-1]+pp[xi-1,yj,zk,n-1]+pp[xi,yj+1,zk,n-1]+pp[xi,yj-1,zk,n-1]+pp[xi,yj,zk+1,n-1]+pp[xi,yj,zk-1,n-1])/6
    return ans

def test_4():
    h = 0.1
    pp = np.zeros((31,31,31,10001))
    for ndx in range(10001):
        n = ndx
        for kdx in range(31):
            k = 1.5-kdx*h
            for jdx in range(31):
                j = 1.5-jdx*h
                for idx in range(31):
                    i = 1.5-idx*h
                    temp = phi_2(i,j,k,n,pp,h)
                    pp[idx, jdx, kdx, ndx] = temp
        if ndx%1000 == 0:
            plt.plot(pp[15,15,:,ndx])
            plt.xticks([0,5,10,15,20, 25, 30], [-1.5,-1.0, -0.5, 0, 0.5, 1.0, 1.5])
            plt.title("figure 2-1\nphi(0,0,z) on 10*10*10 grid")
            plt.xlabel("z")
    plt.show()

    return 0

#test_4()

def test_5():
    h = 0.01
    pp = np.zeros((301, 301, 301, 11))
    for ndx in range(11):
        n = ndx
        for kdx in range(301):
            k = 1.5 - kdx * h
            for jdx in range(301):
                j = 1.5 - jdx * h
                for idx in range(301):
                    i = 1.5 - idx * h
                    temp = phi_2(i, j, k, n, pp, h)
                    pp[idx, jdx, kdx, ndx] = temp
        print(ndx)
        plt.plot(pp[150, 150, :, ndx])
        plt.xticks([0, 50, 100, 150, 200, 250, 300], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
        plt.title("figure 2-2\nphi(0,0,z) on 100*100*100 grid")
        plt.xlabel("z")
        plt.show()

    return 0

#test_5()

def test_6():
    h = 0.1
    pp = np.zeros((11,11,11,101))
    for ndx in range(101):
        n = ndx
        for kdx in range(11):
            k = 0.5-kdx*h
            for jdx in range(11):
                j = 0.5-jdx*h
                for idx in range(11):
                    i = 0.5-idx*h
                    temp = phi_2(i,j,k,n,pp,h)
                    pp[idx, jdx, kdx, ndx] = temp
    deltamax = 0
    colmax = []

    for ndx in range(1,101):
        for jdx in range(11):
            for idx in range(11):
                for kdx in range(11):
                    if pp[idx,jdx,kdx,ndx]!=0 or pp[idx,jdx,kdx,ndx-1]!=0:
                        deltatemp = (pp[idx, jdx, kdx, ndx] - pp[idx, jdx, kdx, ndx - 1])/pp[idx,jdx,kdx,ndx-1]
                    if deltatemp > deltamax:
                        deltamax = deltatemp
        colmax.append(deltamax)
        deltamax = 0
    plt.plot(colmax)
    plt.title("error v.s. iteration")
    plt.xlabel("iteration")
    plt.ylabel("error")
    plt.show()
    plt.loglog(colmax)
    plt.title("log(error) v.s. log(iteration)")
    plt.xlabel("log(iteration)")
    plt.ylabel("log(error)")
    plt.show()

    return 0

#test_6()