from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SourceViewSet, StatViewSet, SourcesListView, SourceDetailView, SourceCreateView


router = DefaultRouter()
router.register('sources', SourceViewSet)
router.register('stats', StatViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('sources/', SourcesListView.as_view()),
    path('sources/<int:pk>/', SourceDetailView.as_view(), name='detail'),
    path('sources/create/', SourceCreateView.as_view(), name='create'),
]
