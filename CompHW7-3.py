import matplotlib.pyplot as plt
import numpy as np
import math
import random
import statistics

def test_1():
    N = 10000 #10000 particles
    vx = []
    vy = []
    vz = []
    phi = np.random.uniform(0,2*math.pi,N) #randomly create direction
    c = np.random.uniform(-1,1,N)
    M = 100*N #number of collides
    for jdx in range(N):
        vx.append(math.cos(phi[jdx])*math.sqrt(1-pow(c[jdx],2)))
        vy.append(math.cos(phi[jdx]) * c[jdx])
        vz.append(math.sin(phi[jdx]))

    for idx in range(M):
        v1 = random.randint(0,N-1) #randomly pick 2 particles
        v2 = random.randint(0,N-1)
        if v1 == v2:
            idx -=1
            continue
        vxcm = 0.5 * vx[v1] + 0.5 * vx[v2] #center of mass
        vycm = 0.5 * vy[v1] + 0.5 * vy[v2]
        vzcm = 0.5 * vz[v1] + 0.5 * vz[v2]
        v1_xcm = vx[v1]-vxcm
        v1_ycm = vy[v1] - vycm
        v1_zcm = vz[v1]-vzcm
        v1_cm = math.sqrt(pow(v1_xcm,2)+pow(v1_ycm,2)+pow(v1_zcm,2))
        nphi = np.random.uniform(0,2*math.pi,1)
        nc = np.random.uniform(-1,1,1)
        v1fx = v1_cm*math.cos(nphi)*math.sqrt(1-pow(nc,2))
        v1fy = v1_cm*math.cos(nphi)*nc
        v1fz = v1_cm*math.sin(nphi)
        vx[v1] = v1fx+vxcm
        vy[v1] = v1fy+vycm
        vz[v1] = v1fz+vzcm
        vx[v2] = -v1fx + vxcm
        vy[v2] = -v1fy + vycm
        vz[v2] = -v1fz + vzcm

    v_fin = []
    for kdx in range(N):
        value = math.sqrt(pow(vx[kdx],2)+pow(vy[kdx],2)+pow(vz[kdx],2))
        v_fin.append(value)

    step = 0.01
    x = np.arange(0,max(v_fin),step)
    mean = statistics.mean(v_fin)
    a = mean*math.sqrt(math.pi*0.5)*0.5
    dis = 60*np.sqrt(np.pi*0.5)*x**2*np.exp(-x**2/(2*a**2))/a**3
    plt.xlim(0,max(v_fin))
    plt.hist(v_fin,bins = x)
    plt.ylabel("Number particle in bins")
    plt.xlabel("v")
    plt.plot(x,dis)
    plt.show()

test_1()