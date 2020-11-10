from django.shortcuts import render, HttpResponse,redirect
from .models import Books,Authors

def index(request):
    context = {
    "books" : Books.objects.all(),
    "authors" : Authors.objects.all()
    }
    return render(request, 'index.html', context)

def add_book(request):
    new_book = Books(title=request.POST['title'], desc=request.POST['desc'])
    new_book.save()
    return redirect('/')

def show_book(request, book_id):
    context = {
    "book" : Books.objects.get(id=book_id),
    "authors" : Authors.objects.all(),
    }
    return render(request, 'book.html', context)

def add_book_author(request):
    the_book_id = int( request.POST['book_id'] )
    author_id = int( request.POST['author_id'] )
    author = Authors.objects.get(id=author_id)
    book = Books.objects.get(id=the_book_id)
    book.written_by.add(author)
    book.save()
    return redirect(show_book, book_id=the_book_id)

def index2(request):
    context = {
    "books" : Books.objects.all(),
    "authors" : Authors.objects.all()
    }
    return render(request, 'authors.html', context)



def show_author(request, author_id):
    context = {
    "author" : Authors.objects.get(id=author_id),
    "books" : Books.objects.all(),
    }
    return render(request, 'author.html', context)

def add_author(request):
    new_author = Authors(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    new_author.save()
    return redirect('/authors')


def add_book_to_author(request):
    the_author_id = int( request.POST['author_id'] )
    book_id = int( request.POST['the_book_id'] )
    book = Books.objects.get(id=book_id)
    author = Authors.objects.get(id=the_author_id)
    author.books.add(book)
    author.save()
    return redirect(show_author, author_id=the_author_id)