from latex2sympy2 import latex2sympy
import math 
import sympy as sp
from scipy.optimize import minimize_scalar

def changingLatextosimple(func):
    data={}
    changed = latex2sympy(func)
    data["function"] = changed.args[0]
    data["variable"] = changed.args[1][0]
    data["starting"] = changed.args[1][1]
    data["ending"] = changed.args[1][2]
    return data

def derivativeFunction(func):
    data = {}
    changed = latex2sympy(func)
    changedlist = list(changed.args)
    print(changed)
    data["function"] = changedlist[0]
    data["variable"] = changedlist[1][0]
    variable = str(data.get("variable"))
    symbolinfunction = sp.Symbol(variable)
    firstDerivative = data.get("function").diff(symbolinfunction)
    return firstDerivative

def integrateFunction(func):
    data={}
    changed = latex2sympy(func)
    changedlist = list(changed.args)
    if(len(changedlist[1])==3):
        data["function"] =changedlist[0]
        data["variable"] = str(changedlist[1][0])
        data["starting"] = float(changedlist[1][1])
        data["ending"] = float(changedlist[1][2])
        result = float(sp.integrate(data.get("function"),(data.get("variable"), data.get("starting"),data.get("ending"))))
        return result 
    else:
        data["function"] =changedlist[0]
        data["variable"] = str(changedlist[1][0])  
        print(data)
        result = sp.integrate(data.get("function"),sp.Symbol(data.get("variable")))
        return result
        
   

class MidPoint:
    def __init__(self, function, starting, ending, interval=0, k=0, error = 0, variable="x"):
        
        self.function = function
        self.starting = float(starting)
        self.ending = float(ending)
        self.interval = float(interval)
        self.k = float(k)
        self.error = float(error)
        self.variable = str(variable)
        
        
    def midpointEvaluate(self):
        ans = 0
        deltax = (self.ending-self.starting)/self.interval
        left = self.starting
        right = self.starting+deltax
        while right<=self.ending:
            avg = round((left+right)/2,6)
            
            ans = ans + self.midpointFunction(avg)
            left = round(left+deltax,6)
            right=round(right+deltax,6)
        return round(ans*deltax,6)
    
    
    def midpointFunction(self,avg):
        
        x = sp.Symbol(self.variable)
        sol = self.function.subs(x, avg)
        return  round(sol,6)
    # =======================================================
    
    def midpointfbound(self):
        symbolinfunction = sp.Symbol(self.variable)
        firstDerivative = self.function.diff(symbolinfunction)
        secondDerivative = firstDerivative.diff(symbolinfunction)
        print(secondDerivative)
        solution1 = secondDerivative.subs(symbolinfunction,self.starting)
        print(solution1)
        solution2 = secondDerivative.subs(symbolinfunction,self.ending)
        sol3 = self.midpointmaxInainterval(secondDerivative)
        
        finalval = max(abs(solution1),abs(solution2),sol3)
        return float(finalval)
        
    def f(self,su, second):
        symbolinfunction = sp.Symbol(self.variable)
        return float(second.subs(symbolinfunction,su))

    def midpointmaxInainterval(self, secondDerivative):
        interval = (self.starting, self.ending)
        # max value
        res = minimize_scalar(lambda su: -self.f(su, secondDerivative), bounds=interval, method='bounded') 
        # min value
        res1 = minimize_scalar(lambda su: self.f(su, secondDerivative), bounds=interval, method='bounded')
        # print(-res.fun, res1.fun)
        if abs(res.fun)>abs(res1.fun):
            return abs(res.fun)
        else:
            return abs(res1.fun)
# ============================================================================================================================
    def midpointError(self):
        # k*(b-a)**3/(24*(n)**2)
        erroranswer =float(self.k*(self.ending-self.starting)**3)/(24*(self.interval)**2)
        return erroranswer
    
    def numberofInterval(self):
        numberofIntervalanswer = math.sqrt((self.k*(self.ending-self.starting)**3)/(24*self.error))
        return math.ceil(numberofIntervalanswer)
    
    
    
    
class TrapezoidEvaluate:
    def __init__(self, function, starting, ending, interval=0, k=0, error = 0,variable = "x"):
        self.function = function
        self.starting = float(starting)
        self.ending = float(ending)
        self.interval = float(interval)
        self.k=float(k)
        self.error = float(error)
        self.variable = str(variable)
        
    def evaluate(self):
        deltax = (self.ending-self.starting)/self.interval
        
        i = self.starting
        ans = 0
        fans = 0
        while i <self.ending or i==self.ending:
    
            if i==self.starting or i==self.starting:
                fans = self.myfun(i)
            else:
                fans = 2 * self.myfun(i)
            ans = ans + fans
            print(ans)
            i= round(i+deltax,6)
            
        return round((ans * deltax)/2,6)
    

    
    
        
            
    def myfun(self,avg):
        
        x = sp.Symbol(self.variable)
        sol = self.function.subs(x, avg)
        return  round(sol,6)
            
    # =======================================================
    
    def trapezoidfbound(self):
        symbolinfunction = sp.Symbol(self.variable)
        firstDerivative = self.function.diff(symbolinfunction)
        secondDerivative = firstDerivative.diff(symbolinfunction)
        # thirdDerivative = secondDerivative.diff(symbolinfunction)
        # fourthDerivative = thirdDerivative.diff(symbolinfunction)
        solution1 = secondDerivative.subs(symbolinfunction,self.starting)
        solution2 = secondDerivative.subs(symbolinfunction,self.ending)
        sol3 = self.trapezoidMaxValueoffunction(secondDerivative)
        finalval = max(abs(solution1),abs(solution2),sol3)
        return float(finalval)
        
    def f(self,su, second):
        symbolinfunction = sp.Symbol(self.variable)
        return float(second.subs(symbolinfunction,su))

    def trapezoidMaxValueoffunction(self, secondDerivative):
        interval = (self.starting, self.ending)
        res = minimize_scalar(lambda su: -self.f(su, secondDerivative), bounds=interval, method='bounded')
        res1 = minimize_scalar(lambda su: -self.f(su, secondDerivative), bounds=interval, method='bounded')
        if(abs(res.fun>abs(res1.fun))):
            return abs(res.fun)
        else:
            return abs(res1.fun)
# ============================================================================================================================
    def trapezoidError(self):
        # k*(b-a)**3/(24*(n)**2)
        erroranswer =(self.k*(self.ending-self.starting)**3)/(12*(self.interval)**2)
        return erroranswer
    
    def numberofInterval(self):
        numberofIntervalanswer = math.sqrt((self.k*(self.ending-self.starting)**3)/(12*self.error))
        return math.ceil(numberofIntervalanswer)
    


class SimpsonEvaluate:
    
    def __init__(self, function, starting, ending, interval=0, k=0, error = 0, variable="x"):
        self.function = function
        self.starting = float(starting)
        self.ending = float(ending)
        self.interval = float(interval)
        self.k=float(k)
        self.error = float(error)
        self.variable = str(variable)
        
    def evaluate(self):
        deltax = (self.ending-self.starting)/self.interval
        i =self.starting
        ans = 0
        mul = 4
        while i <=self.ending:
            if i == self.starting or i ==self.ending:
                fans = self.myfun(i)
            elif mul == 4:
                fans = 4 * self.myfun(i)
                mul = 2
            else:
                fans = 2 * self.myfun(i)
                mul = 4
            ans = round(ans+fans,6)
            i = round(i+deltax,6)
        return round((ans*deltax)/3,6)
            
    def myfun(self, avg):
        x = sp.Symbol(self.variable)
        sol = self.function.subs(x, avg)
        return  round(sol,6)
    
    def simpsonfbound(self):
        symbolinfunction = sp.Symbol(self.variable)
        firstDerivative = self.function.diff(symbolinfunction)
        secondDerivative = firstDerivative.diff(symbolinfunction)
        thirdDerivative = secondDerivative.diff(symbolinfunction)
        fourthDerivative = thirdDerivative.diff(symbolinfunction)
        solution1 = fourthDerivative.subs(symbolinfunction,self.starting)
        print(solution1)
        solution2 = fourthDerivative.subs(symbolinfunction,self.ending)
        sol3 = self.simpsonMaxValueFunction(fourthDerivative)
        finalval = max(abs(solution1),abs(solution2),sol3)
        return float(finalval)
        
    def f(self,su, fourth):
        symbolinfunction = sp.Symbol(self.variable)
        return float(fourth.subs(symbolinfunction,su))

    def simpsonMaxValueFunction(self, secondDerivative):
        interval = (self.starting, self.ending)
        res = minimize_scalar(lambda su: -self.f(su, secondDerivative), bounds=interval, method='bounded')
        res1 = minimize_scalar(lambda su: -self.f(su, secondDerivative), bounds=interval, method='bounded')
        if(abs(res.fun>abs(res1.fun))):
            return abs(res.fun)
        else:
            return abs(res1.fun)
# ============================================================================================================================
    def simpsonError(self):
        # k*(b-a)**3/(24*(n)**2)
        erroranswer =(self.k*(self.ending-self.starting)**5)/(180*(self.interval)**4)
        return erroranswer
    
    def numberofInterval(self):
        numberofIntervalanswer = ((self.k*(self.ending-self.starting)**5)/(180*self.error))**(1/4)
        return numberofIntervalanswer
    

    
                