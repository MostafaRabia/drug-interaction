"""
URL configuration for drug_interaction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from models import views as models_views
from interaction import views as interaction_views

router = routers.DefaultRouter()
router.register(r'drugs', models_views.DrugViewSet)
router.register(r'active-substances', models_views.ActiveSubstanceViewSet)
router.register(r'diseases', models_views.DiseaseViewSet)
router.register(r'active-substance-disease', models_views.ActiveSubstanceDiseaseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('check-drug-disease-interaction', interaction_views.check_if_drug_interaction_disease),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("__debug__/", include("debug_toolbar.urls")),
]
