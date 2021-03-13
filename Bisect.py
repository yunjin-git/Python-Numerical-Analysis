import math as mt

def Bisect(xl,xu):
    eps = 1
    rep = 0
    tol = 1.0e-3
    if (f(xl)*f(xu)) >=0 :
     print(" 구간을 다시 설정 해주세요 ") 
    else :
        
     while eps > tol :
        rep = rep+ 1
        xm = (xl+xu)/2
        
        if not(xm == 0) :
            eps = abs((xl-xm)/xm)
            
        print('반복횟수 =',rep,'f(xm)=',f(xm),'xm=',xm,'eps=',format(eps,".4f"))
        
        if f(xl)*f(xm) > 0 :
             xl=xm
             
        elif f(xl)*f(xm) < 0 :
             xu=xm
             
        else : 
             eps = 0

def f(x):
    value = x-mt.exp(-x) # 구하고 싶은 방정식을 입력
    return value
            
            
           
Bisect(-2,2) # 구간을 지정하여 이분법 사용시작
