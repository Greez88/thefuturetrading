from django.urls import path
from .views import HomeView, AboutView, PlanView, ServiceView, RoleView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('plans', PlanView.as_view(), name='plans'),
    path('service', ServiceView.as_view(), name='service'),
    path('role', RoleView.as_view(), name='role'),
    path('contact', ContactView.as_view(), name='contact'),
]

