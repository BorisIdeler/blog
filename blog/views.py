from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

from .models import Post, Categorie, Contact, Comment
from .forms import ContactForm, CommentForm
from .tasks import send_mail
from .utils import validate_captcha, get_logger

logger = get_logger(__name__)

def index(request):
    logger.info(request)
    logger.info('Index')
    logger.debug('Getting all index posts')
    posts = Post.objects.all().order_by('-date_published')
    logger.debug('Getting all categories')
    categories = Categorie.objects.all()
    logger.debug('Rendering and returning index request')
    return render(request, 'index.html', { 'posts': posts, 'categories': categories })

def categorie(request, pk):
    logger.info(request)
    logger.info('Categorie')
    logger.debug('Getting all posts in {}'.format(pk))    
    posts = Post.objects.filter(categories=pk).order_by('-date_published')
    logger.debug('Getting all categorie categories')
    categories = Categorie.objects.all()
    logger.debug('Rendering and returning categorie request')    
    return render(request, 'index.html', { 'posts': posts, 'categories': categories })

def contact(request):
    logger.info(request)
    logger.info('Contact')
    logger.debug('Checking contact request method')
    if request.method == 'POST':
        logger.debug('Contact request method is POST')
        form = ContactForm(request.POST)

        logger.debug('Checking if contact form is valid')
        if form.is_valid():
            logger.debug('Contact form is valid')
            logger.debug('Validating contact captcha')
            result = validate_captcha(request)
            if result['success']:
                logger.debug('Contact captcha is valid')
                logger.debug('Cleaning and saving contact form data')
                contact = Contact(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], email=form.cleaned_data['email'], question=form.cleaned_data['question'])
                contact.save()
                logger.debug('Contact form data saved')
                logger.debug('Sending contact mail')
                send_mail(form.cleaned_data['question'])
                logger.debug('Redirecting to question_submitted')                
                return HttpResponseRedirect(reverse('blog:question-submitted'))
            else:
                logger.error('Contact form captcha is not valid')
                logger.error(result)                       
    else:
        logger.debug('Contact request method is not POST.')
        form = ContactForm()

    logger.debug('Returning contact form')
    return render(request, 'contact.html', { 'form': form })

def question_submitted(request):
    logger.info(request)
    logger.info('Question submitted')
    logger.debug('Rendering and returning question_submitted request') 
    return render(request, 'question_submitted.html')

def post(request, pk):
    logger.info(request)
    logger.info('Post request')
    logger.debug('Getting post {}'.format(pk))
    post = Post.objects.get(pk=pk)
    logger.debug('Getting all comments in {}'.format(pk))
    comments = post.comment_set.all()
    count = comments.count()
    logger.debug('Getting all categories')
    categories = Categorie.objects.all()

    logger.debug('Getting post request method')
    if request.method == 'POST':
        logger.debug('Request method is POST')
        form = CommentForm(request.POST)
        if form.is_valid():
            logger.debug('Post request form is valid')
            logger.debug('Validating post captcha')
            result = validate_captcha(request)
            if result['success']:
                logger.debug('Post captcha is valid')
                logger.debug('Cleaning post data')
                comment = Comment(name=form.cleaned_data['name'], comment=form.cleaned_data['comment'], post_id=post)
                logger.debug('Saving post comment')
                comment.save()
                logger.debug('Sending post comment mail')
                send_mail(form.cleaned_data['comment'])
                logger.debug('Rendering and returning post request') 
                return redirect('blog:post', post.id)
            else:
                logger.error('Post captcha is not valid')
    else:
        logger.debug('Post request method is not POST.')
        form = CommentForm()

    return render(request, 'post.html', { 'post': post, 'comments': comments, 'form': form, 'count': count, 'categories': categories })