
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analyse_sentiment/', include('sentimental_analysis.urls')),]
