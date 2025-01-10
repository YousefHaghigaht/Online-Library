from django.contrib import admin
from .models import Author,Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age')


admin.site.register(Book)