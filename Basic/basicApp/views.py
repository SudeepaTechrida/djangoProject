from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404
from .models import Book
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

def loginPage(request):
  if request.method == 'POST':
    username= request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, "Login Successful")
      return redirect('index')
    else:
      messages.error(request, 'Invalid Credentials!!')
  return render(request, 'registration/login.html')

# @login_required(login_url= 'accounts/login/')
# def index(request):
#   # template = loader.get_template('index.html')
#   # return HttpResponse(template.render())
#   books = Book.objects.all()
#   return render(request,"basicApp/index.html", {'books':books})

# @csrf_exempt
# def add(request):
#   if request.method == 'POST':
#       name = request.POST.get("name")
#       author = request.POST.get("author")
#       publication = request.POST.get("publication")
#       description = request.POST.get("description")
#       books = Book.objects.create(name= name, author=author, publication=publication,description=description)
#       books.save()
#       messages.success(request, 'Book Added.')
#       return redirect('index')
#   return render(request, "basicApp/add.html")

# def edit(request, book_id):
#   book = get_object_or_404(Book, id= book_id)
#   if request.method == 'POST':
#     book.name = request.POST.get("name")
#     book.author = request.POST.get("author")
#     book.publication = request.POST.get("publication")
#     book.description = request.POST.get("description")
#     book.save()
#     messages.success(request, 'Book Updated')
#     return redirect('index')
  
#   return render(request, "basicApp/edit.html", {'book':book})

# def delete(request, delete_id):
#   book = get_object_or_404(Book, id= delete_id)
#   book.delete()
#   messages.success(request, 'Book Deleted')
#   return redirect('index')

def logoutPage(request):
  logout(request)
  messages.success(request, 'Logout successfully')
  return redirect('login')

class BookList(ListView):
  model = Book
  template_name = 'basicApp/index.html'
  context_object_name = 'books'


class BookDetail(DetailView):
  model = Book
  template_name = 'basicApp/edit.html'
  context_object_name = 'book'
  pk_url_kwarg = 'book_id'

class BookCreate(CreateView):
  model = Book
  fields = ['name', 'author', 'description', 'publication']
  success_url = reverse_lazy('index')
  template_name = 'basicApp/add.html'


class BookUpdate(UpdateView):
  model = Book
  fields = ['name', 'author', 'description', 'publication']
  success_url = reverse_lazy('index')
  template_name = 'basicApp/editform.html'
  pk_url_kwarg = 'book_id'
  context_object_name = 'book'

class BookDelete(DeleteView):
  model =  Book
  context_object_name = 'book'
  pk_url_kwarg = 'delete_id'
  success_url = reverse_lazy('index')
  