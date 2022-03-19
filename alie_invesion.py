import matplotlib.pyplot as plt
import numpy as np
class N():
    
    def __init__(self,r,a,n0):
        self.r = r;self.a = a;self.n0 = n0
        def f(t,n):
            return self.a*n*(1-n/r)
        self.f = f

    def solve(self,t):
        n = [self.n0]*len(t)
        for k in range(len(t)-1):
            h = t[k+1] - t[k]
            n[k+1] = n[k] + h*self.f(t[k],n[k])

        return np.array(n)
def f_2(t):
    return 30000*1000/(1000+(30000-1000)*np.exp(-0.1*t))
xp = N(30000,0.1,1000)
t = np.linspace(0,100,99)
                    
plt.plot(t,xp.solve(t))
plt.plot(t,f_2(t))
plt.legend(['moni','real'])
plt.show()
