from django.shortcuts import get_object_or_404,render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Book,Author
from django.urls import reverse
from django.contrib import messages
from .forms import SearchForm
from django.db.models import Q


class BooksListView(ListView):
    """
    1- List all the books
    2- List of author books by author ID
    3- List of books by their search name

    """
    template_name = 'books/books_list.html'
    model = Book
    context_object_name = 'books'

    def get_queryset(self):
        author_id = self.kwargs.get('author_id')
        books = Book.objects.all()
        if author_id:
            author = get_object_or_404(Author,id=author_id)
            return books.filter(author=author)

        if self.request.GET.get('search'):
            return books.filter(name__contains=self.request.GET['search'])
        return books

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm
        return context


class BookDetailView(DetailView):
    """
    Show details of a book
    """
    template_name = 'books/book_detail.html'
    model = Book
    context_object_name = 'book'


class AuthorsListView(ListView):
    """
    1-List of all authors
    2-List of authors by their first name, last name and search national code
    """

    template_name = 'books/authors_list.html'
    model = Author
    context_object_name = 'authors'

    def get_queryset(self):
        authors = Author.objects.all()
        if self.request.GET.get('search'):
            search = self.request.GET['search']
            authors = authors.filter(Q(first_name__contains=search) |
                                     Q(last_name__contains=search) |
                                     Q(national_code__contains=search))
            return authors
        return authors

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm
        return context


class BookCreateView(CreateView):
    """
    Create a new book
    """
    model = Book
    fields = '__all__'
    template_name = 'books/book_create.html'

    def get_success_url(self):
        messages.success(self.request, 'Author created successfully', 'success')
        return reverse('books:book_detail', args=[self.object.pk])


class AuthorCreateView(CreateView):
    """
    Create a new author
    """

    model = Author
    fields = '__all__'
    template_name = 'books/author_create.html'

    def get_success_url(self):
        messages.success(self.request,'Book created successfully','success')
        return reverse('books:books_list_author', args=[self.object.id])


class BookDeleteView(DeleteView):
    """
    Delete a book
    """

    model = Book
    template_name = 'books/object_delete.html'

    def get_success_url(self):
        messages.success(self.request,'The book was deleted','success')
        return reverse('books:books_list')


class AuthorDeleteView(DeleteView):
    """
    Delete a author
    """

    model = Author
    template_name = 'books/object_delete.html'

    def get_success_url(self):
        messages.success(self.request,'The Author was deleted','success')
        return reverse('books:authors_list')


class AuthorEditView(UpdateView):
    """
    Edit Author
    """

    model = Author
    fields = '__all__'
    template_name = 'books/object_edit.html'
    pk_url_kwarg = 'author_id'

    def get_success_url(self):
        messages.success(self.request,f'{self.object.first_name} updated','success')
        return reverse('books:authors_list')


class BookEditView(UpdateView):
    """
    Edit book
    """

    model = Book
    fields = '__all__'
    template_name = 'books/object_edit.html'
    pk_url_kwarg = 'book_id'

    def get_success_url(self):
        messages.success(self.request,f'{self.object.name} updated','success')
        return reverse('books:book_detail',args=[self.object.id])





