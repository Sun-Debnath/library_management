from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# class HomeView(TemplateView):
#     template_name = 'index.html'



from book.models import Book
from category.models import Category



def home(request, category_slug = None):
    data = Book.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Book.objects.filter(category  = category)
    category = Category.objects.all()
    return render(request, 'index.html', {'data' : data, 'category' : category})