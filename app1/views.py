from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import MidPoint, changingLatextosimple, TrapezoidEvaluate, SimpsonEvaluate,  TrapezoidEvaluate, derivativeFunction, integrateFunction
# ========================================================

class Home(APIView):
    def get(self,request,format=None):
        return Response({"msg":"successful"})
class DerivativeView(APIView):
    def post(self, request, format=None):
        print("DERIVATIVE")
        incoming_Latexfunction = request.data.get("function")
        result= derivativeFunction(incoming_Latexfunction)
        return Response({"msg":f"{result}"})
        # =================================================================================
class IntegrationView(APIView):
    def post(self,request, format=None):
        incoming_Latexfunction = request.data.get("function")
        result = integrateFunction(incoming_Latexfunction)
        
        return Response({"msg":f"{result}"})
        
# ============================================================================================

class Midpoint(APIView):
    def post(self,request, format =None):
        incoming_Latexfunction = request.data.get("function")
        simple_MathIntegral= changingLatextosimple(incoming_Latexfunction)
        mathfunction = simple_MathIntegral.get("function")
        variable = simple_MathIntegral.get("variable")
        incoming_starting = simple_MathIntegral.get("starting")
        incoming_ending = simple_MathIntegral.get("ending")
        incoming_interval = request.data.get("interval")
        
        midpoint1 = MidPoint(function=mathfunction, starting=incoming_starting, ending=incoming_ending, interval=incoming_interval, k=0, variable=variable)
        result = midpoint1.midpointEvaluate()
        
        return Response({"msg": f"{result}"})
class MidPointFbound(APIView):
    def post(self,request, format=None):
        incoming_Latexfunction = request.data.get("function")
        simple_MathIntegral = changingLatextosimple(incoming_Latexfunction)
        mathfunction = simple_MathIntegral.get("function")
        variable = simple_MathIntegral.get("variable")
        incoming_starting = simple_MathIntegral.get("starting")
        incoming_ending = simple_MathIntegral.get("ending")
        
        midpointFbound1 = MidPoint(function=mathfunction,starting=incoming_starting,ending = incoming_ending, variable=variable)
        result = midpointFbound1.midpointfbound()
        return Response({"msg":f"{result}"})
    
class MidPointError(APIView):
    def post(self,request, format=None):
        incoming_Latexfunction = request.data.get("function")
        simple_MathIntegral = changingLatextosimple(incoming_Latexfunction)
        mathfunction = simple_MathIntegral.get("function")
        variable = simple_MathIntegral.get("variable")
        incoming_starting = simple_MathIntegral.get("starting")
        incoming_ending = simple_MathIntegral.get("ending")
        incoming_interval = request.data.get("interval")
        incoming_k = request.data.get("k")
        midpointFbound1 = MidPoint(function=mathfunction,starting=incoming_starting,ending = incoming_ending, interval=incoming_interval, k=incoming_k, variable=variable)
        result = midpointFbound1.midpointError()
        return Response({"msg":f"{result}"})
    
class MidPointInterval(APIView):
        def post(self,request, format=None):
            incoming_Latexfunction = request.data.get("function")
            simple_MathIntegral = changingLatextosimple(incoming_Latexfunction)
            mathfunction = simple_MathIntegral.get("function")
            variable = simple_MathIntegral.get("variable")
            incoming_starting = simple_MathIntegral.get("starting")
            incoming_ending = simple_MathIntegral.get("ending")
            incoming_interval = request.data.get("interval")
            incoming_k = request.data.get("k")
            incoming_error = request.data.get("error")
            midpointFbound1 = MidPoint(function=mathfunction,starting=incoming_starting,ending = incoming_ending, interval=incoming_interval, k=incoming_k, error=incoming_error, variable=variable)
            result = midpointFbound1.numberofInterval()
            return Response({"msg":f"{result}"})
    
        
    


# =============================================================================================================================
class Trapezoid(APIView):
    def post(self,request,format=None):
        incoming_Latexfunction = request.data.get("function")
        simple_MathIntegral = changingLatextosimple(incoming_Latexfunction)
        mathfunction = simple_MathIntegral.get("function")
        variable = simple_MathIntegral.get("variable")
        incoming_starting = simple_MathIntegral.get("starting")
        incoming_ending = simple_MathIntegral.get("ending")
        incoming_interval = request.data.get("interval")
        trapezoid1 = TrapezoidEvaluate(mathfunction, incoming_starting, incoming_ending, incoming_interval, variable=variable)
        result = trapezoid1.evaluate()
        
        return Response({"msg":f"{result}"})

class TrapezoidFbound(APIView):
    def post(self,request, format=None):
        incoming_Latexfunction = request.data.get("function")
        simple_MathIntegral = changingLatextosimple(incoming_Latexfunction)
        mathfunction = simple_MathIntegral.get("function")
        variable = simple_MathIntegral.get("variable")
        incoming_starting = simple_MathIntegral.get("starting")
        incoming_ending = simple_MathIntegral.get("ending")
        
        trapezoidFbound = TrapezoidEvaluate(function=mathfunction,starting=incoming_starting,ending = incoming_ending, variable=variable)
        result = trapezoidFbound.trapezoidfbound()
        return Response({"msg":f"{result}"})
        
class TrapezoidError(APIView):
    def post(self,request, format=None):
        incoming_Latexfunction = request.data.get("function")
        simple_MathIntegral = changingLatextosimple(incoming_Latexfunction)
        mathfunction = simple_MathIntegral.get("function")
        variable = simple_MathIntegral.get("variable")
        incoming_starting = simple_MathIntegral.get("starting")
        incoming_ending = simple_MathIntegral.get("ending")
        incoming_interval = request.data.get("interval")
        incoming_k = request.data.get("k")
        trapezoidError1 = TrapezoidEvaluate(function=mathfunction,starting=incoming_starting,ending = incoming_ending, interval=incoming_interval, k=incoming_k, variable=variable)
        result = trapezoidError1.trapezoidError()
        return Response({"msg":f"{result}"})
    
        
class TrapezoidInterval(APIView):
        def post(self,request, format=None):
            incoming_Latexfunction = request.data.get("function")
            simple_MathIntegral = changingLatextosimple(incoming_Latexfunction)
            mathfunction = simple_MathIntegral.get("function")
            variable = simple_MathIntegral.get("variable")
            incoming_starting = simple_MathIntegral.get("starting")
            incoming_ending = simple_MathIntegral.get("ending")
            incoming_interval = request.data.get("interval")
            incoming_k = request.data.get("k")
            incoming_error = request.data.get("error")
            trapezoidInterval1 = TrapezoidEvaluate(function=mathfunction,starting=incoming_starting,ending = incoming_ending, interval=incoming_interval, k=incoming_k, error=incoming_error, variable=variable)
            result = trapezoidInterval1.numberofInterval()
            return Response({"msg":f"{result}"})
    
    
class Simspson(APIView):
    def post(self,request, format=None):
        incoming_Latexfunction = request.data.get("function")
        simple_MathIntegral = changingLatextosimple(incoming_Latexfunction)
        mathfunction = simple_MathIntegral.get("function")
        variable = simple_MathIntegral.get("variable")
        incoming_starting = simple_MathIntegral.get("starting")
        incoming_ending = simple_MathIntegral.get("ending")
        incoming_interval = request.data.get("interval")
        simpson1 = SimpsonEvaluate(mathfunction,incoming_starting,incoming_ending, incoming_interval, variable=variable)
        result = simpson1.evaluate()
        return Response({"msg":f"{result}"})
    
class SimpsonFbound(APIView):
    def post(self,request, format=None):
        incoming_Latexfunction = request.data.get("function")
        simple_MathIntegral = changingLatextosimple(incoming_Latexfunction)
        mathfunction = simple_MathIntegral.get("function")
        variable = simple_MathIntegral.get("variable")
        incoming_starting = simple_MathIntegral.get("starting")
        incoming_ending = simple_MathIntegral.get("ending")
        
        simpsonFbound = SimpsonEvaluate(function=mathfunction,starting=incoming_starting,ending = incoming_ending,variable=variable)
        result = simpsonFbound.simpsonfbound()
        return Response({"msg":f"{result}"})
        
class SimpsonError(APIView):
    def post(self,request, format=None):
        incoming_Latexfunction = request.data.get("function")
        simple_MathIntegral = changingLatextosimple(incoming_Latexfunction)
        mathfunction = simple_MathIntegral.get("function")
        variable = simple_MathIntegral.get("variable")
        incoming_starting = simple_MathIntegral.get("starting")
        incoming_ending = simple_MathIntegral.get("ending")
        incoming_interval = request.data.get("interval")
        incoming_k = request.data.get("k")
        simpsonError1 = SimpsonEvaluate(function=mathfunction,starting=incoming_starting,ending = incoming_ending, interval=incoming_interval, k=incoming_k, variable=variable)
        result = simpsonError1.simpsonError()
        return Response({"msg":f"{result}"})
    
        
class SimpsonInterval(APIView):
        def post(self,request, format=None):
            incoming_Latexfunction = request.data.get("function")
            simple_MathIntegral = changingLatextosimple(incoming_Latexfunction)
            mathfunction = simple_MathIntegral.get("function")
            variable = simple_MathIntegral.get("variable")
            incoming_starting = simple_MathIntegral.get("starting")
            incoming_ending = simple_MathIntegral.get("ending")
            incoming_interval = request.data.get("interval")
            incoming_k = request.data.get("k")
            incoming_error = request.data.get("error")
            simpsonInterval1 = SimpsonEvaluate(function=mathfunction,starting=incoming_starting,ending = incoming_ending, k=incoming_k, error=incoming_error, variable=variable)
            result = simpsonInterval1.numberofInterval()
            return Response({"msg":f"{result}"})
    