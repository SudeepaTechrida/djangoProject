from django.urls import path
from . import views
urlpatterns = [
   path('', views.BookList.as_view(), name='index'),
   path('book-create/', views.BookCreate.as_view(), name='book-create'),
   path('book-update/<int:book_id>/',views.BookUpdate.as_view(), name='book-update'),
   path('book-delete/<int:delete_id>/', views.BookDelete.as_view(), name='book-delete'),
   # path('', views.index , name='index'),
   # path('add/', views.add , name='add'),
   # path('edit/<int:book_id>', views.edit, name='edit'),
   # path('delete/<int:delete_id>', views.delete, name='delete'),
   path('accounts/login/', views.loginPage, name='login'),
   path('accounts/logout/', views.logoutPage, name='logout')
]