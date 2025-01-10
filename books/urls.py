from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('list/',views.BooksListView.as_view(),name='books_list'),
    path('list/<int:author_id>/',views.BooksListView.as_view(),name='books_list_author'),
    path('detail/<int:pk>/',views.BookDetailView.as_view(),name='book_detail'),
    path('authors/',views.AuthorsListView.as_view(),name='authors_list'),
    path('create/',views.BookCreateView.as_view(),name='book_create'),
    path('author/create/',views.AuthorCreateView.as_view(),name='author_create'),
    path('delete/<int:pk>',views.BookDeleteView.as_view(),name='book_delete'),
    path('delete/author/<int:pk>',views.AuthorDeleteView.as_view(),name='author_delete'),
    path('author/edit/<int:author_id>/',views.AuthorEditView.as_view(),name='author_edit'),
    path('edit/<int:book_id>/',views.BookEditView.as_view(),name='book_edit'),
]