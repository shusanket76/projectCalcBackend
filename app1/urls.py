from django.urls import path
from .views import Midpoint, Trapezoid, Simspson, MidPointFbound, MidPointError,MidPointInterval, DerivativeView, IntegrationView, TrapezoidFbound, TrapezoidError, TrapezoidInterval, SimpsonFbound,SimpsonError, SimpsonInterval, Home

urlpatterns = [
    path("", Home.as_view()),
    path("midpoint", Midpoint.as_view()),
    path("trapezoid", Trapezoid.as_view()),
    path("simpson", Simspson.as_view()),
    path("midpointFbound", MidPointFbound.as_view()),
    path("midpointError", MidPointError.as_view()),
    path("midpointInterval",MidPointInterval.as_view()),
    path("derivative", DerivativeView.as_view()),
    path("integration", IntegrationView.as_view()),
    path("trapezoidFbound", TrapezoidFbound.as_view()),
    path("trapezoidError", TrapezoidError.as_view()),
    path("trapezoidInterval", TrapezoidInterval.as_view()),
    path("simpsonFbound", SimpsonFbound.as_view()),
    path("simpsonError", SimpsonError.as_view()),
    path("simpsonInterval", SimpsonInterval.as_view()),
]
