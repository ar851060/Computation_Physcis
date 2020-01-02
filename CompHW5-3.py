import matplotlib.pyplot as plt
import numpy as np

h = 0.1 #space span
tau = pow(h,2)/6 #time span, I suppose tau = h^2/6

def phi(i,j,k,n,pp):
    t = n*tau
    xi = int(round((1.5 - i) / h))
    yj = int(round((1.5 - j) / h))
    zk = int(round((1.5 - k) / h))
    if i == 1.5 or i == -1.5 or j == 1.5 or j == -1.5 or k == 1.5 or k == -1.5: #outside the outer box
        ans = 0
    elif i == -0.5 and j <= 0.5 and j >= -0.5 and k <=0.5 and k >= -0.5: #inside box, I use poisson equation
        ans = h*h/6+(pp[xi+1,yj,zk,n-1]+pp[xi-1,yj,zk,n-1]+pp[xi,yj+1,zk,n-1]+pp[xi,yj-1,zk,n-1]+pp[xi,yj,zk+1,n-1]+pp[xi,yj,zk-1,n-1])/6
    elif i ==0.5 and j <= 0.5 and j >= -0.5 and k <=0.5 and k >= -0.5:#inside box, I use poisson equation
        ans = h*h/6+(pp[xi+1,yj,zk,n-1]+pp[xi-1,yj,zk,n-1]+pp[xi,yj+1,zk,n-1]+pp[xi,yj-1,zk,n-1]+pp[xi,yj,zk+1,n-1]+pp[xi,yj,zk-1,n-1])/6
    elif j == -0.5 and i <= 0.5 and i >= -0.5 and k <=0.5 and k >= -0.5:#inside box, I use poisson equation
        ans = h*h/6+(pp[xi+1,yj,zk,n-1]+pp[xi-1,yj,zk,n-1]+pp[xi,yj+1,zk,n-1]+pp[xi,yj-1,zk,n-1]+pp[xi,yj,zk+1,n-1]+pp[xi,yj,zk-1,n-1])/6
    elif j == 0.5 and i <= 0.5 and i >= -0.5 and k <=0.5 and k >= -0.5:#inside box, I use poisson equation
        ans = h*h/6+(pp[xi+1,yj,zk,n-1]+pp[xi-1,yj,zk,n-1]+pp[xi,yj+1,zk,n-1]+pp[xi,yj-1,zk,n-1]+pp[xi,yj,zk+1,n-1]+pp[xi,yj,zk-1,n-1])/6
    elif k == -0.5 and j <= 0.5 and j >= -0.5 and i <=0.5 and i >= -0.5:#inside box, I use poisson equation
        ans = h*h/6+(pp[xi+1,yj,zk,n-1]+pp[xi-1,yj,zk,n-1]+pp[xi,yj+1,zk,n-1]+pp[xi,yj-1,zk,n-1]+pp[xi,yj,zk+1,n-1]+pp[xi,yj,zk-1,n-1])/6
    elif k == 0.5 and j <= 0.5 and j >= -0.5 and i <=0.5 and i >= -0.5:#inside box, I use poisson equation
        ans = h*h/6+(pp[xi+1,yj,zk,n-1]+pp[xi-1,yj,zk,n-1]+pp[xi,yj+1,zk,n-1]+pp[xi,yj-1,zk,n-1]+pp[xi,yj,zk+1,n-1]+pp[xi,yj,zk-1,n-1])/6
    elif t==0: #initial condition
        ans = 0
    else: #I use the laplace equation
        ans = (pp[xi+1,yj,zk,n-1]+pp[xi-1,yj,zk,n-1]+pp[xi,yj+1,zk,n-1]+pp[xi,yj-1,zk,n-1]+pp[xi,yj,zk+1,n-1]+pp[xi,yj,zk-1,n-1])/6
    return ans

def test_1():
    pp = np.zeros((31,31,31,1001))
    ex = np.zeros((31,31))
    ey = np.zeros((31,31))
    for ndx in range(1001):#1000 time steps
        n = ndx
        for kdx in range(31):#30 space steps
            k = 1.5-kdx*h
            for jdx in range(31):#30 space steps
                j = 1.5-jdx*h
                for idx in range(31):#30 space steps
                    i = 1.5-idx*h
                    temp = phi(i,j,k,n,pp)
                    pp[idx, jdx, kdx, ndx] = temp

    #Fined the E
    for idx in range(31):
        for jdx in range(31):
            if idx == 0 or jdx == 0:
                if jdx >= 30 or idx >= 30: #outside the outer box
                    ex[idx, jdx] = 0
                    ey[idx, jdx] = 0
                else:
                    ex[idx,jdx] = -(pp[idx+1,jdx,15,1000])/(2*h)
                    ey[idx,jdx] = -(pp[idx,jdx+1,15,1000])/(2*h)
            elif jdx >= 30 or idx >= 30:
                if idx == 0 or jdx == 0:
                    ex[idx, jdx] = 0
                    ey[idx, jdx] = 0
                else:
                    ex[idx,jdx] = -(-pp[idx-1,jdx,15,1000])/(2*h)
                    ey[idx,jdx] = -(-pp[idx,jdx-1,15,1000])/(2*h)
            else:
                ex[idx,jdx] = -(pp[idx+1,jdx,15,1000]-pp[idx-1,jdx,15,1000])/(2*h)
                ey[idx,jdx] = -(pp[idx,jdx+1,15,1000]-pp[idx,jdx-1,15,1000])/(2*h)

    plt.quiver(ey,ex)
    plt.xticks([0,5,10,15,20,25,30],[-1.5,-1.0,-0.5,0,0.5,1.0,1.5])
    plt.yticks([0,5,10,15,20,25,30],[-1.5,-1.0,-0.5,0,0.5,1.0,1.5])
    plt.title("figure 3-1")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    return 0

#test_1()

def test_2():
    pp = np.zeros((31, 31, 31, 1001))
    ex = np.zeros((31, 31))
    ey = np.zeros((31, 31))
    exo = np.zeros((31, 31))
    eyo = np.zeros((31, 31))
    qi = np.zeros((31,31))
    qo = np.zeros((31,31))
    #calculate electric potential
    for ndx in range(101):
        n = ndx
        for kdx in range(31):
            k = 1.5 - kdx * h
            for jdx in range(31):
                j = 1.5 - jdx * h
                for idx in range(31):
                    i = 1.5 - idx * h
                    temp = phi(i, j, k, n, pp)
                    pp[idx, jdx, kdx, ndx] = temp
    # calculate inner plane electric field
    for idx in range(31):
        for jdx in range(31):
            if idx == 0 or jdx == 0:
                if jdx >= 30 or idx >= 30:
                    ex[idx, jdx] = 0
                    ey[idx, jdx] = 0
                else:
                    ex[idx,jdx] = -(pp[idx+1,jdx,10,100])/(2*h)
                    ey[idx,jdx] = -(pp[idx,jdx+1,10,100])/(2*h)
            elif jdx >= 30 or idx >= 30:
                if idx == 0 or jdx == 0:
                    ex[idx, jdx] = 0
                    ey[idx, jdx] = 0
                else:
                    ex[idx,jdx] = -(-pp[idx-1,jdx,10,100])/(2*h)
                    ey[idx,jdx] = -(-pp[idx,jdx-1,10,100])/(2*h)
            else:
                ex[idx,jdx] = -(pp[idx+1,jdx,10,100]-pp[idx-1,jdx,10,100])/(2*h)
                ey[idx,jdx] = -(pp[idx,jdx+1,10,100]-pp[idx,jdx-1,10,100])/(2*h)
    # calculate outer plane electric field
    for idx in range(31):
        for jdx in range(31):
            if idx == 0 or jdx == 0:
                if jdx >= 30 or idx >= 30:
                    exo[idx, jdx] = 0
                    eyo[idx, jdx] = 0
                else:
                    exo[idx,jdx] = -(pp[idx+1,jdx,1,99])/(2*h*6)
                    eyo[idx,jdx] = -(pp[idx,jdx+1,1,99])/(2*h*6)
            elif jdx >= 30 or idx >= 30:
                if idx == 0 or jdx == 0:
                    exo[idx, jdx] = 0
                    eyo[idx, jdx] = 0
                else:
                    exo[idx,jdx] = -(-pp[idx-1,jdx,1,99])/(2*h*6)
                    eyo[idx,jdx] = -(-pp[idx,jdx-1,1,99])/(2*h*6)
            else:
                exo[idx,jdx] = -(pp[idx+1,jdx,1,99]-pp[idx-1,jdx,1,99])/(2*h*6)
                eyo[idx,jdx] = -(pp[idx,jdx+1,1,99]-pp[idx,jdx-1,1,99])/(2*h*6)

    # calculate inner plane charge distribution
    for idx in range(10,21):# the inner plane only on 1 length unit long
        for jdx in range(10,21):
                qi[idx,jdx] = ((ex[idx+1,jdx]-ex[idx-1,jdx])/(2*h))+((ey[idx,jdx+1]-ey[idx,jdx-1])/(2*h))
    # calculate outer plane charge distribution
    for idx in range(31):
        for jdx in range(31):
            if idx == 0 :
                if jdx >= 30:
                    qo[idx, jdx] = ((exo[idx + 1, jdx]) / (2 * h)) + (
                            (- eyo[idx, jdx - 1]) / (2 * h))
                elif jdx ==0:
                    qo[idx, jdx] = ((exo[idx + 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1]) / (2 * h))
                else:
                    qo[idx, jdx] = ((exo[idx + 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1] - eyo[idx, jdx - 1]) / (2 * h))
            elif jdx == 0:
                if idx >= 30:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1]) / (2 * h))
                else:
                    qo[idx, jdx] = ((exo[idx + 1, jdx] - exo[idx - 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1]) / (2 * h))
            elif idx >= 30:
                if jdx == 0:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1]) / (2 * h))
                elif jdx >= 30:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (- eyo[idx, jdx - 1]) / (2 * h))
                else:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1] - eyo[idx, jdx - 1]) / (2 * h))
            elif jdx >= 30:
                if idx == 0:
                    qo[idx, jdx] = ((exo[idx + 1, jdx]) / (2 * h)) + (
                            ( - eyo[idx, jdx - 1]) / (2 * h))
                elif idx>=30:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (- eyo[idx, jdx - 1]) / (2 * h))
                else:
                    qo[idx, jdx] = ((exo[idx + 1, jdx] - exo[idx - 1, jdx]) / (2 * h)) + (
                            (- eyo[idx, jdx - 1]) / (2 * h))
            else:
                qo[idx, jdx] = ((exo[idx + 1, jdx] - exo[idx - 1, jdx]) / (2 * h)) + (
                    (eyo[idx, jdx + 1] - eyo[idx, jdx - 1]) / (2 * h))
    bb = plt.contourf(qi, cmap=plt.cm.hot)
    plt.colorbar(bb,orientation = "vertical")
    plt.xticks([0, 5, 10, 15, 20, 25, 30], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    plt.yticks([0, 5, 10, 15, 20, 25, 30], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    plt.title("figure 3-2-1\ninner plane")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    aa = plt.contourf(-qo, cmap = plt.cm.hot)
    plt.colorbar(aa, orientation="vertical")
    plt.xticks([0, 5, 10, 15, 20, 25, 30], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    plt.yticks([0, 5, 10, 15, 20, 25, 30], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    plt.title("figure 3-2-2\nouter plane")
    plt.show()

    return 0

#test_2()

def phi_2(i,j,k,n,pp):
    t = n*tau
    xi =int(round((1.5-i)/h))
    yj =int(round((1.5-j)/h))
    zk =int(round((1.5-k)/h))
    if i == 1.5 or i == -1.5 or j == 1.5 or j == -1.5 or k == 1.5 or k == -1.5:
        ans = 0
    elif i == 1.2 and j <= 0.5 and j >= -0.5 and k <=0.5 and k >= -0.5:#we change the box in to (1.2~0.2,0.5~-0.5,0.5~-0.5)
        ans = h * h / 6 + (pp[xi + 1, yj, zk, n - 1] + pp[xi - 1, yj, zk, n - 1] + pp[xi, yj + 1, zk, n - 1] + pp[
            xi, yj - 1, zk, n - 1] + pp[xi, yj, zk + 1, n - 1] + pp[xi, yj, zk - 1, n - 1]) / 6
    elif xi == 13 and j <= 0.5 and j >= -0.5 and k <=0.5 and k >= -0.5:
        ans = h * h / 6 + (pp[xi + 1, yj, zk, n - 1] + pp[xi - 1, yj, zk, n - 1] + pp[xi, yj + 1, zk, n - 1] + pp[
            xi, yj - 1, zk, n - 1] + pp[xi, yj, zk + 1, n - 1] + pp[xi, yj, zk - 1, n - 1]) / 6
    elif j == -0.5 and i <= 1.2 and i >= 0.2 and k <=0.5 and k >= -0.5:
        ans = h * h / 6 + (pp[xi + 1, yj, zk, n - 1] + pp[xi - 1, yj, zk, n - 1] + pp[xi, yj + 1, zk, n - 1] + pp[
            xi, yj - 1, zk, n - 1] + pp[xi, yj, zk + 1, n - 1] + pp[xi, yj, zk - 1, n - 1]) / 6
    elif j == 0.5 and i <= 1.2 and i >= 0.2 and k <=0.5 and k >= -0.5:
        ans = h * h / 6 + (pp[xi + 1, yj, zk, n - 1] + pp[xi - 1, yj, zk, n - 1] + pp[xi, yj + 1, zk, n - 1] + pp[
            xi, yj - 1, zk, n - 1] + pp[xi, yj, zk + 1, n - 1] + pp[xi, yj, zk - 1, n - 1]) / 6
    elif k == -0.5 and j <= 0.5 and j >= -0.5 and i <=1.2 and i >= -0.2:
        ans = h * h / 6 + (pp[xi + 1, yj, zk, n - 1] + pp[xi - 1, yj, zk, n - 1] + pp[xi, yj + 1, zk, n - 1] + pp[
            xi, yj - 1, zk, n - 1] + pp[xi, yj, zk + 1, n - 1] + pp[xi, yj, zk - 1, n - 1]) / 6
    elif k == 0.5 and j <= 0.5 and j >= -0.5 and i <=1.2 and i >= 0.2:
        ans = h * h / 6 + (pp[xi + 1, yj, zk, n - 1] + pp[xi - 1, yj, zk, n - 1] + pp[xi, yj + 1, zk, n - 1] + pp[
            xi, yj - 1, zk, n - 1] + pp[xi, yj, zk + 1, n - 1] + pp[xi, yj, zk - 1, n - 1]) / 6
    elif t==0:
        ans = 0
    else:
        ans = (pp[xi+1,yj,zk,n-1]+pp[xi-1,yj,zk,n-1]+pp[xi,yj+1,zk,n-1]+pp[xi,yj-1,zk,n-1]+pp[xi,yj,zk+1,n-1]+pp[xi,yj,zk-1,n-1])/6
    return ans

def test_3():
    pp = np.zeros((31,31,31,1001))
    ex = np.zeros((31,31))
    ey = np.zeros((31,31))
    for ndx in range(1001):
        n = ndx
        for kdx in range(31):
            k = 1.5 - kdx * h
            for jdx in range(31):
                j = 1.5 - jdx * h
                for idx in range(31):
                    i = 1.5 - idx * h
                    temp = phi_2(i, j, k, n, pp)
                    pp[idx, jdx, kdx, ndx] = temp


    for idx in range(31):
        for jdx in range(31):
            if idx == 0 or jdx == 0:
                if jdx >= 30 or idx >= 30:
                    ex[idx, jdx] = 0
                    ey[idx, jdx] = 0
                else:
                    ex[idx,jdx] = -(pp[idx+1,jdx,15,1000])/(2*h)
                    ey[idx,jdx] = -(pp[idx,jdx+1,15,1000])/(2*h)
            elif jdx >= 30 or idx >= 30:
                if idx == 0 or jdx == 0:
                    ex[idx, jdx] = 0
                    ey[idx, jdx] = 0
                else:
                    ex[idx,jdx] = -(-pp[idx-1,jdx,15,1000])/(2*h)
                    ey[idx,jdx] = -(-pp[idx,jdx-1,15,1000])/(2*h)
            else:
                ex[idx,jdx] = -(pp[idx+1,jdx,15,1000]-pp[idx-1,jdx,15,1000])/(2*h)
                ey[idx,jdx] = -(pp[idx,jdx+1,15,1000]-pp[idx,jdx-1,15,1000])/(2*h)

    plt.quiver(ey,ex)
    plt.xticks([0, 5, 10, 15, 20, 25, 30], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    plt.yticks([0, 5, 10, 15, 20, 25, 30], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    plt.title("figure 3-3")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.show()

    return 0

#test_3()

def test_4():
    pp = np.zeros((31, 31, 31, 101))
    ex = np.zeros((31, 31))
    ey = np.zeros((31, 31))
    exo = np.zeros((31, 31))
    eyo = np.zeros((31, 31))
    qi = np.zeros((31,31))
    qo = np.zeros((31,31))
    #calculate electric potential
    for ndx in range(101):
        n = ndx
        for kdx in range(31):
            k = 1.5 - kdx * h
            for jdx in range(31):
                j = 1.5 - jdx * h
                for idx in range(31):
                    i = 1.5 - idx * h
                    temp = phi_2(i, j, k, n, pp)
                    pp[idx, jdx, kdx, ndx] = temp
    # calculate inner box electric field
    for idx in range(31):
        for jdx in range(31):
            if idx == 0 or jdx == 0:
                if jdx >= 30 or idx >= 30:
                    ex[idx, jdx] = 0
                    ey[idx, jdx] = 0
                else:
                    ex[idx,jdx] = -(pp[idx+1,jdx,10,100])/(2*h)
                    ey[idx,jdx] = -(pp[idx,jdx+1,10,100])/(2*h)
            elif jdx >= 30 or idx >= 30:
                if idx == 0 or jdx == 0:
                    ex[idx, jdx] = 0
                    ey[idx, jdx] = 0
                else:
                    ex[idx,jdx] = -(-pp[idx-1,jdx,10,100])/(2*h)
                    ey[idx,jdx] = -(-pp[idx,jdx-1,10,100])/(2*h)
            else:
                ex[idx,jdx] = -(pp[idx+1,jdx,10,100]-pp[idx-1,jdx,10,100])/(2*h)
                ey[idx,jdx] = -(pp[idx,jdx+1,10,100]-pp[idx,jdx-1,10,100])/(2*h)
    # calculate outer box electric field
    for idx in range(31):
        for jdx in range(31):
            if idx == 0 or jdx == 0:
                if jdx >= 30 or idx >= 30:
                    exo[idx, jdx] = 0
                    eyo[idx, jdx] = 0
                else:
                    exo[idx,jdx] = -(pp[idx+1,jdx,1,99])/(2*h*6)
                    eyo[idx,jdx] = -(pp[idx,jdx+1,1,99])/(2*h*6)
            elif jdx >= 30 or idx >= 30:
                if idx == 0 or jdx == 0:
                    exo[idx, jdx] = 0
                    eyo[idx, jdx] = 0
                else:
                    exo[idx,jdx] = -(-pp[idx-1,jdx,1,99])/(2*h*6)
                    eyo[idx,jdx] = -(-pp[idx,jdx-1,1,99])/(2*h*6)
            else:
                exo[idx,jdx] = -(pp[idx+1,jdx,1,99]-pp[idx-1,jdx,1,99])/(2*h*6)
                eyo[idx,jdx] = -(pp[idx,jdx+1,1,99]-pp[idx,jdx-1,1,99])/(2*h*6)
    # calculate inner box charge distribution
    for idx in range(3,14):
        for jdx in range(10,21):
                qi[idx,jdx] = ((ex[idx+1,jdx]-ex[idx-1,jdx])/(2*h))+((ey[idx,jdx+1]-ey[idx,jdx-1])/(2*h))
    # calculate outer box charge distribution
    for idx in range(31):
        for jdx in range(31):
            if idx == 0 :
                if jdx >= 30:
                    qo[idx, jdx] = ((exo[idx + 1, jdx]) / (2 * h)) + (
                            (- eyo[idx, jdx - 1]) / (2 * h))
                elif jdx ==0:
                    qo[idx, jdx] = ((exo[idx + 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1]) / (2 * h))
                else:
                    qo[idx, jdx] = ((exo[idx + 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1] - eyo[idx, jdx - 1]) / (2 * h))
            elif jdx == 0:
                if idx >= 30:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1]) / (2 * h))
                else:
                    qo[idx, jdx] = ((exo[idx + 1, jdx] - exo[idx - 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1]) / (2 * h))
            elif idx >= 30:
                if jdx == 0:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1]) / (2 * h))
                elif jdx >= 30:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (- eyo[idx, jdx - 1]) / (2 * h))
                else:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1] - eyo[idx, jdx - 1]) / (2 * h))
            elif jdx >= 30:
                if idx == 0:
                    qo[idx, jdx] = ((exo[idx + 1, jdx]) / (2 * h)) + (
                            ( - eyo[idx, jdx - 1]) / (2 * h))
                elif idx>=30:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (- eyo[idx, jdx - 1]) / (2 * h))
                else:
                    qo[idx, jdx] = ((exo[idx + 1, jdx] - exo[idx - 1, jdx]) / (2 * h)) + (
                            (- eyo[idx, jdx - 1]) / (2 * h))
            else:
                qo[idx, jdx] = ((exo[idx + 1, jdx] - exo[idx - 1, jdx]) / (2 * h)) + (
                    (eyo[idx, jdx + 1] - eyo[idx, jdx - 1]) / (2 * h))
    bb = plt.contourf(qi, cmap=plt.cm.hot)
    plt.colorbar(bb, orientation="vertical")
    plt.xticks([0, 5, 10, 15, 20, 25, 30], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    plt.yticks([0, 5, 10, 15, 20, 25, 30], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    plt.title("figure 3-4-1\ninner plane")
    plt.show()
    aa = plt.contourf(-qo, cmap=plt.cm.hot)
    plt.colorbar(aa, orientation="vertical")
    plt.xticks([0, 5, 10, 15, 20, 25, 30], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    plt.yticks([0, 5, 10, 15, 20, 25, 30], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    plt.title("figure 3-4-2\nouter plane")
    plt.show()

    return 0

#test_4()

def test_5():
    pp = np.zeros((31, 31, 31, 1001))
    ex = np.zeros((31, 31))
    ey = np.zeros((31, 31))
    exo = np.zeros((31, 31))
    eyo = np.zeros((31, 31))
    qi = np.zeros((31,31))
    qo = np.zeros((31,31))
    for ndx in range(101):
        n = ndx
        for kdx in range(31):
            k = 1.5 - kdx * h
            for jdx in range(31):
                j = 1.5 - jdx * h
                for idx in range(31):
                    i = 1.5 - idx * h
                    temp = phi_2(i, j, k, n, pp)
                    pp[idx, jdx, kdx, ndx] = temp


    for idx in range(31):
        for jdx in range(31):
            if idx == 0 or jdx == 0:
                if jdx >= 30 or idx >= 30:
                    ex[idx, jdx] = 0
                    ey[idx, jdx] = 0
                else:
                    ex[idx,jdx] = -(pp[10,jdx,idx+1,100])/(2*h)
                    ey[idx,jdx] = -(pp[10,jdx+1,idx,100])/(2*h)
            elif jdx >= 30 or idx >= 30:
                if idx == 0 or jdx == 0:
                    ex[idx, jdx] = 0
                    ey[idx, jdx] = 0
                else:
                    ex[idx,jdx] = -(-pp[10,jdx,idx-1,100])/(2*h)
                    ey[idx,jdx] = -(-pp[10,jdx-1,idx,100])/(2*h)
            else:
                ex[idx,jdx] = -(pp[10,jdx,idx+1,100]-pp[10,jdx,idx-1,100])/(2*h)
                ey[idx,jdx] = -(pp[10,jdx+1,idx,100]-pp[10,jdx-1,idx,100])/(2*h)

    for idx in range(31):
        for jdx in range(31):
            if idx == 0 or jdx == 0:
                if jdx >= 30 or idx >= 30:
                    exo[idx, jdx] = 0
                    eyo[idx, jdx] = 0
                else:
                    exo[idx,jdx] = -(pp[1,jdx,idx+1,99])/(2*h*6)
                    eyo[idx,jdx] = -(pp[1,jdx+1,idx,99])/(2*h*6)
            elif jdx >= 30 or idx >= 30:
                if idx == 0 or jdx == 0:
                    exo[idx, jdx] = 0
                    eyo[idx, jdx] = 0
                else:
                    exo[idx,jdx] = -(-pp[1,jdx,idx-1,99])/(2*h*6)
                    eyo[idx,jdx] = -(-pp[1,jdx-1,idx,99])/(2*h*6)
            else:
                exo[idx,jdx] = -(pp[1,jdx,idx+1,99]-pp[1,jdx,idx-1,99])/(2*h*6)
                eyo[idx,jdx] = -(pp[1,jdx+1,idx,99]-pp[1,jdx-1,idx,99])/(2*h*6)



    for idx in range(10,21):
        for jdx in range(10,21):
                qi[idx,jdx] = ((ex[idx+1,jdx]-ex[idx-1,jdx])/(2*h))+((ey[idx,jdx+1]-ey[idx,jdx-1])/(2*h))

    for idx in range(31):
        for jdx in range(31):
            if idx == 0 :
                if jdx >= 30:
                    qo[idx, jdx] = ((exo[idx + 1, jdx]) / (2 * h)) + (
                            (- eyo[idx, jdx - 1]) / (2 * h))
                elif jdx ==0:
                    qo[idx, jdx] = ((exo[idx + 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1]) / (2 * h))
                else:
                    qo[idx, jdx] = ((exo[idx + 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1] - eyo[idx, jdx - 1]) / (2 * h))
            elif jdx == 0:
                if idx >= 30:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1]) / (2 * h))
                else:
                    qo[idx, jdx] = ((exo[idx + 1, jdx] - exo[idx - 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1]) / (2 * h))
            elif idx >= 30:
                if jdx == 0:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1]) / (2 * h))
                elif jdx >= 30:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (- eyo[idx, jdx - 1]) / (2 * h))
                else:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (eyo[idx, jdx + 1] - eyo[idx, jdx - 1]) / (2 * h))
            elif jdx >= 30:
                if idx == 0:
                    qo[idx, jdx] = ((exo[idx + 1, jdx]) / (2 * h)) + (
                            ( - eyo[idx, jdx - 1]) / (2 * h))
                elif idx>=30:
                    qo[idx, jdx] = ((- exo[idx - 1, jdx]) / (2 * h)) + (
                            (- eyo[idx, jdx - 1]) / (2 * h))
                else:
                    qo[idx, jdx] = ((exo[idx + 1, jdx] - exo[idx - 1, jdx]) / (2 * h)) + (
                            (- eyo[idx, jdx - 1]) / (2 * h))
            else:
                qo[idx, jdx] = ((exo[idx + 1, jdx] - exo[idx - 1, jdx]) / (2 * h)) + (
                    (eyo[idx, jdx + 1] - eyo[idx, jdx - 1]) / (2 * h))
    bb = plt.contourf(qi, cmap=plt.cm.hot)
    plt.colorbar(bb, orientation="vertical")
    plt.xticks([0, 5, 10, 15, 20, 25, 30], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    plt.yticks([0, 5, 10, 15, 20, 25, 30], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    plt.title("figure 3-5-1\ninner plane")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    aa = plt.contourf(-qo, cmap=plt.cm.hot)
    plt.colorbar(aa, orientation="vertical")
    plt.xticks([0, 5, 10, 15, 20, 25, 30], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    plt.yticks([0, 5, 10, 15, 20, 25, 30], [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    plt.title("figure 3-5-2\nouter plane")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    return 0

test_5()