"""iitsh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from cloud import views

urlpatterns = [
    path('root/', admin.site.urls),
    path('', views.index_page),
    path('admin/', views.admin_page),

    path('cabinet/<num>', views.Cabinet_page, name='Cabinet_page'),
    path('admin/addcabinet', views.addcabinet_page),

    # path('cabinet/', views.cabinet_page),

    # path('brands/<shopnmae>', views.sertCardBrend_page, name='sertCardBrend_page'),

]
