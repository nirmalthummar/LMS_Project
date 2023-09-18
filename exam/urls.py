from exam import views
from django.urls import re_path

urlpatterns = [
    re_path('test/',views.showTest),
    re_path('result/',views.showResult),
]
