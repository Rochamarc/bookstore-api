"""bookstore URL Configuration

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
from django.urls import path, include

from rest_framework import routers
from mybooks.views import AuthorViewSet, BookViewSet, BookGenreViewSet, BookLiteratureViewSet, ClassificationViewSet, FormatViewSet, LiteratureViewSet, PublisherViewSet, GenreViewSet, EditionViewSet

router = routers.DefaultRouter()

router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'classsifications', ClassificationViewSet)
router.register(r'formats', FormatViewSet)
router.register(r'literatures', LiteratureViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'book-literatures', BookLiteratureViewSet)
router.register(r'book-genres', BookGenreViewSet)
router.register(r'editions', EditionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls