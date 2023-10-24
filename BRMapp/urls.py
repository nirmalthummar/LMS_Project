from BRMapp import views
# from django.conf.urls import url
from django.urls import re_path, path

urlpatterns = [
    re_path('view-books',views.viewBooks),
    re_path('edit-book',views.editBook),
    re_path('delete-book',views.deleteBook),
    re_path('search-book',views.search),
    re_path('new-book',views.newBook),
    re_path(r'^add',views.add),
    re_path('search',views.search),
    re_path('edit',views.edit),
    re_path('login',views.userLogin),
    path('logout',views.userLogout),
    ]
