"""
URL configuration for abcdosaber project.

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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tipodeatividade/', include('tipodeatividade.urls')),
    path('instrutor/', include('instrutor.urls')),
    path('aluno/', include('aluno.urls', namespace='aluno')),
    path('turma/', include('turma.urls')),
    path('titulo/', include('titulo.urls', namespace='titulo')),
    path('', TemplateView.as_view(template_name="escola.html")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
