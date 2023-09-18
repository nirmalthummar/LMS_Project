# from django.conf.urls import url
from django.urls import re_path
from testapp import views

urlpatterns = [
    re_path('^$',views.greeting),
    re_path('about/',views.about),
    re_path('contact/',views.showContact),
    re_path('employee/',views.employee_info_view),
]
