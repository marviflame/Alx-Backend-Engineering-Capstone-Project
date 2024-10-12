from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, LibraryUserViewSet, TransactionViewSet
from . import views

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', LibraryUserViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('', views.index),
]