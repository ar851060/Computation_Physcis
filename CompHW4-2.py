import matplotlib.pyplot as plt
import numpy as np
tau = 0.001 #time span
h = 0.1#space span
leng = int(1/h+1)
def press(jdx,idx,pp,vv): #I create the function to produce p
    tt = jdx*tau
    xx = idx*h
    const = tau / (2 * h)
    if tt==0:#initial condition
        if xx>=0.4 and xx<0.7:
            ans = 1
        else:
            ans = 0
        return ans
    else:
        if xx == 0:#I suppose there is no anything pressure outside the boundary
            ans = 0.5* (pp[(jdx - 1) * leng + idx + 1]) - const * 0.5 * (
                    pp[(jdx - 1) * leng + idx + 1] ) * (
                          vv[(jdx - 1) * leng + idx + 1]) - const * 0.5 * (
                          vv[(jdx - 1) * leng + idx + 1] ) * (
                          pp[(jdx - 1) * leng + idx + 1] )
        elif xx == 1:
            ans = 0.5 * (pp[(jdx - 1) * leng + idx - 1]) - const * 0.5 * (pp[(jdx - 1) * leng + idx - 1]) * (- vv[(jdx - 1) * leng + idx - 1]) - const * 0.5 * (vv[(jdx - 1) * leng + idx - 1]) * ( - pp[(jdx - 1) * leng + idx - 1])
        else:
            ans = 0.5 * (pp[(jdx - 1) * leng + idx + 1] + pp[(jdx - 1) * leng + idx - 1]) - const * 0.5 * (
                    pp[(jdx - 1) * leng + idx + 1] + pp[(jdx - 1) * leng + idx - 1]) * (
                          vv[(jdx - 1) * leng + idx + 1] - vv[(jdx - 1) * leng + idx - 1]) - const * 0.5 * (
                          vv[(jdx - 1) * leng + idx + 1] + vv[(jdx - 1) * leng + idx - 1]) * (
                          pp[(jdx - 1) * leng + idx + 1] - pp[(jdx - 1) * leng + idx - 1])
        return ans

def vol(jdx,idx,pp,vv):#I create the function to produce v
    tt = jdx * tau
    xx = idx * h
    const = tau / (2 * h)
    if tt==0:#initial condition
        ans =0
    elif xx==0 or xx==1:#boundary condition
        ans = 0
    else:
        if pp[(jdx-1)*leng+idx+1]+pp[(jdx-1)*leng+idx-1] == 0:#to avoid divdied by 0, so I put this before the function
            ans = 0
        else:
            ans = 0.5*(vv[(jdx-1)*leng+idx+1]+vv[(jdx-1)*leng+idx-1]) - const * 0.5*(vv[(jdx-1)*leng+idx+1]+vv[(jdx-1)*leng+idx-1]) * (vv[(jdx-1)*leng+idx+1]-vv[(jdx-1)*leng+idx-1]) - const * (pp[(jdx-1)*leng+idx+1]-pp[(jdx-1)*leng+idx-1]) /(0.5*(pp[(jdx-1)*leng+idx+1]+pp[(jdx-1)*leng+idx-1]))
    return ans

def find_sound():#this function is to find sound speed and speed crossing time
    pp = []
    vv = []
    for jdx in range(101):
        dn = jdx * tau
        for idx in range(11):
            dh = idx * h
            resp = press(jdx, idx,pp,vv)
            resv = vol(jdx, idx,pp,vv)
            pp.append(resp)
            vv.append(resv)
        if resp != 0:
            break
    print(dn)
    sound_speed = 0.4/dn
    print(sound_speed)
    if resp == 0:
        print("it's not real answer")

#find_sound()

def test2():
    pp = []
    vv = []
    for jdx in range(12):#loop for time
        for idx in range(11):#loop for space
            resp = press(jdx, idx,pp,vv)
            resv = vol(jdx, idx,pp,vv)
            pp.append(resp)
            vv.append(resv)
    a = np.reshape(pp,(12,11))#reshape the list to 12*11
    b = np.reshape(vv,(12,11))
    dn = np.linspace(0,0.011,12)
    dh = np.linspace(0,1,11)
    X, T = np.meshgrid(dh, dn)#make a grid
    aa = plt.contourf(X, T, a,cmap = plt.cm.hot)#plot contour
    plt.colorbar(aa,orientation = "vertical")
    plt.show()
    bb = plt.contourf(X, T, b,cmap = plt.cm.hot)
    plt.colorbar(bb, orientation="vertical")
    plt.show()

test2()