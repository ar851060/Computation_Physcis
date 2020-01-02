import matplotlib.pyplot as plt
import numpy as np
tau = 0.01
h = 0.1
leng = int(1/h+1)

def press(jdx,idx,pp,vv):
    tt = jdx*tau
    xx = idx*h
    const = tau / (2 * h)
    if tt==0:#initial condition
        ans = 1
        return ans
    else:
        if xx == 0:#boundary condition
            ans = 0.5* (pp[(jdx - 1) * leng + idx + 1]) - const * 0.5 * (
                    pp[(jdx - 1) * leng + idx + 1] ) * (
                          vv[(jdx - 1) * leng + idx + 1]) - const * 0.5 * (
                          vv[(jdx - 1) * leng + idx + 1] ) * (
                          pp[(jdx - 1) * leng + idx + 1] )
        elif xx == 1:#boundary condition
            ans = 0.5 * (pp[(jdx - 1) * leng + idx - 1]) - const * 0.5 * (pp[(jdx - 1) * leng + idx - 1]) * (- vv[(jdx - 1) * leng + idx - 1]) - const * 0.5 * (vv[(jdx - 1) * leng + idx - 1]) * ( - pp[(jdx - 1) * leng + idx - 1])
        else:
            ans = 0.5 * (pp[(jdx - 1) * leng + idx + 1] + pp[(jdx - 1) * leng + idx - 1]) - const * 0.5 * (
                    pp[(jdx - 1) * leng + idx + 1] + pp[(jdx - 1) * leng + idx - 1]) * (
                          vv[(jdx - 1) * leng + idx + 1] - vv[(jdx - 1) * leng + idx - 1]) - const * 0.5 * (
                          vv[(jdx - 1) * leng + idx + 1] + vv[(jdx - 1) * leng + idx - 1]) * (
                          pp[(jdx - 1) * leng + idx + 1] - pp[(jdx - 1) * leng + idx - 1])
        return ans

def vol(jdx,idx,pp,vv):
    tt = jdx * tau
    xx = idx * h
    const = tau / (2 * h)
    if tt==0:#initial condition
        ans =0
    elif xx==0 or xx==1:#boundary condition
        ans = 0
    else:
        if pp[(jdx-1)*leng+idx+1]+pp[(jdx-1)*leng+idx-1] == 0:
            ans = 0
        else:
            ans = 0.5*(vv[(jdx-1)*leng+idx+1]+vv[(jdx-1)*leng+idx-1]) - const * 0.5*(vv[(jdx-1)*leng+idx+1]+vv[(jdx-1)*leng+idx-1]) * (vv[(jdx-1)*leng+idx+1]-vv[(jdx-1)*leng+idx-1]) - const * (pp[(jdx-1)*leng+idx+1]-pp[(jdx-1)*leng+idx-1]) /(0.5*(pp[(jdx-1)*leng+idx+1]+pp[(jdx-1)*leng+idx-1]))-10*tau
    return ans

def test():
    pp = []
    vv = []
    for jdx in range(61):
        for idx in range(11):
            resp = press(jdx, idx,pp,vv)
            resv = vol(jdx, idx,pp,vv)
            pp.append(resp)
            vv.append(resv)
    a = np.reshape(pp, (61, 11))
    b = np.reshape(vv, (61, 11))
    dn = np.linspace(0, 0.06, 61)
    dh = np.linspace(0, 1, 11)
    X, T = np.meshgrid(dh, dn)
    aa = plt.contourf(X, T, a, cmap=plt.cm.hot)
    plt.colorbar(aa, orientation="vertical")
    plt.show()
    bb = plt.contourf(X, T, b, cmap=plt.cm.hot)
    plt.colorbar(bb, orientation="vertical")
    plt.show()
test()