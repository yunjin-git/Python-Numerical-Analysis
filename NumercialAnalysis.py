# This code is based on 'Numercial Methods For Engineers , Steven C.Chapra, Raymond P.Canale"
# code developer : yunjin Kyung, MyoungJi univerity


import math

class Bisect : #Bisection Method
    def __init__(self, xl, xu, tol):
        self.xl = xl
        self.xu = xu
        self.tol = tol
        self.equ = input("Please your Equation(Pythonic) : ")
      

    def show(self):
        print("Equ : {}  xl : {}  xu: {} tolerance: {}".format(self.equ, self.xl, self.xu,self.tol))

    def analysis(self):
        if (Bisect.fu(self)*Bisect.fn(self)) >= 0 :
            print("Please reset your range : xl,xu")

        else : 
            rep = 0
            eps = 1

            while eps > self.tol : 
                rep = rep + 1 
                xr = (self.xl + self.xu)/2

                if not (xr == 0) :
                    eps = abs((self.xl-xr)/xr)

                if self.fn()*self.fu() < 0 :
                 self.xl=xr
                 self.xm=xr
             
                elif self.fu()*self.fn() > 0 :
                 self.xu=xr
                 self.xm=xr

                else : 
                 eps = 0

                print('rep =',rep,'f(xm)=',self.fxm(),'xm=',xr,'eps=',format(eps,".4f"))

    def fu(self):
        x=self.xu
        self.valu = eval(self.equ)
        return self.valu

    def fn(self):
        x=self.xl
        self.vall = eval(self.equ)
        return self.vall
    
    def fxm(self):
        x=self.xm
        self.valxm = eval(self.equ)
        return self.valxm

class NR :                  # Newton-Raphson Method
    def __init__(self):
        pass
