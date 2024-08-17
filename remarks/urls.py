from django.urls import path

from .views import HomePageView, CreateRemarkView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('remark', CreateRemarkView.as_view(), name='add_remark')
]