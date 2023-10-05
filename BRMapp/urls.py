from BRMapp import views
# from django.conf.urls import url
from django.urls import re_path, path

urlpatterns = [
    path('view-books',views.viewBooks),
    path('edit-book',views.editBook),
    path('delete-book',views.deleteBook),
    path('search-book',views.search),
    path('new-book',views.newBook),
    path('add',views.add),
    re_path('search',views.search),
    path('edit',views.edit),
    re_path('login',views.userLogin),
    path('logout',views.userLogout),
    ]
