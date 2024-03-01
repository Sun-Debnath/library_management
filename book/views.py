from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,DetailView
from accounts.models import UserBankAccount



class DetailBookView(DetailView):
    model = models.Book
    pk_url_kwarg = 'id'
    template_name = 'book_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        book = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        comments = book.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
class CommentView(DetailView):
    model = models.Book
    pk_url_kwarg = 'id'
    template_name = 'comment.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        book = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        comments = book.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context



def ByeNow(request,id):
    book = models.Book.objects.get(pk=id)
    user_balance = request.user.account.balance
    # user_balance = UserBankAccount.objects.get(account=request.user.account)
    if user_balance >= book.price:
        book.quantity -= 1
        # amount -= book.price
        request.user.account.balance -= book.price
        # user_balance -= book.price
        request.user.account.save()
        history = models.History(
            name=book.name, 
            category=book.category, 
            quantity=1,
            image = book.image,
            price=book.price,
            book = models.Book.objects.get(pk=id),
            books_id = book.id,
            description = book.description,
            author=request.user)
        print(book.id)
            # author=request.user
        history.save()
        print(history.books_id)
        book.save()
    #     # Transaction.save()
        # UserBankAccount.save()

    print(request.user.account.balance)
    print(book.id)
    
    return redirect("detail_book",id=book.id)