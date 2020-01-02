import matplotlib.pyplot as plt
import numpy as np
import math

def test_1(): #Monte Carlo
   nn = []
   ee = []

   for idx in range(1,7):
       i=0
       nn.append(idx)
       N = pow(10,idx)
       xx = np.random.uniform(0,1,N)
       yy = np.random.uniform(0,1,N)
       for jdx in range(N):
           if (pow(xx[jdx],2)+pow(yy[jdx],2)) <= 1:
               i+=1
       numpi = 4*i/N
       err = abs((numpi-math.pi)/math.pi)
       ee.append(err)
   plt.plot(nn,ee)
   plt.title("error v.s. log(N)\nin Monte Carlo")
   plt.xlabel("log(N)")
   plt.ylabel("error")
   plt.show()

test_1()

def test_2(): #spaced points
   nn = []
   ee = []

   for idx in range(1,7):
       i=0
       nn.append(idx)
       N = pow(10,idx)
       num = int(math.sqrt(N))
       for adx in range(num):
           for bdx in range(num):
               x = (adx+0.5)/num
               y = (bdx+0.5)/num
               if (pow(x,2)+pow(y,2)) <= 1:
                i+=1
       numpi = 4*i/N
       err = abs((numpi-math.pi)/math.pi)
       ee.append(err)
   plt.plot(nn,ee)
   plt.title("error v.s. log(N)\nin evenly spaced points")
   plt.xlabel("log(N)")
   plt.ylabel("error")
   plt.show()

test_2()