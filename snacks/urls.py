from django.urls import path

from .views import HomePage, SnacksListView,SnacksDetailView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('snacks/', SnacksListView.as_view(), name='snacks_list'),
    path('snacks/<int:pk>/', SnacksDetailView.as_view(), name='snacks_detail')
]