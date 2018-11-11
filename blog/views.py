from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post, Categorie, Contact, Comment
from .forms import ContactForm, CommentForm
from .tasks import send_mail
from .utils import validate_captcha

def index(request):
    posts = Post.objects.all().order_by('-date_published')
    categories = Categorie.objects.all()
    return render(request, 'index.html', { 'posts': posts, 'categories': categories })

def projects(request):
    return render(request, 'projects.html')

def categorie(request, pk):    
    posts = Post.objects.filter(categories=pk).order_by('-date_published')
    categories = Categorie.objects.all()    
    return render(request, 'index.html', { 'posts': posts, 'categories': categories })

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            result = validate_captcha(request)
            if result['success']:
                contact = Contact(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], email=form.cleaned_data['email'], question=form.cleaned_data['question'])
                contact.save()
                send_mail(form.cleaned_data['question'])                
                return HttpResponseRedirect(reverse('blog:question-submitted'))           
    else:
        form = ContactForm()

    return render(request, 'contact.html', { 'form': form })

def question_submitted(request):
    return render(request, 'question_submitted.html')

def post(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comment_set.all()
    count = comments.count()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            result = validate_captcha(request)
            if result['success']:
                comment = Comment(name=form.cleaned_data['name'], comment=form.cleaned_data['comment'], post_id=post)
                comment.save()
                send_mail(form.cleaned_data['comment'])
                return redirect('blog:post', post.id)
    else:
        form = CommentForm()

    return render(request, 'post.html', { 'post': post, 'comments': comments, 'form': form, 'count': count })