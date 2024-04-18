from django.shortcuts import render, HttpResponse
from .models import Blog, Comment
from .forms import ContactForm, CommentForm


# Create your views here.
def home_page(request):
    context = {}
    blogs = Blog.objects.all()
    context["blogs"] = blogs
    return render(request, "home.html", context)


def contact_us(request):
    errors = {}
    if request.method == "POST":
        my_form = ContactForm(request.POST)
        if my_form.is_valid():
            my_form.save()
        else:
            errors = my_form.errors

    return render(request, "contact_us.html", {"errors": errors})


def about_us(request):
    return render(request, "about_us.html", {})


def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            obj = comment_form.save(commit=False)
            obj.blog = blog
            obj.save()
    comments = Comment.objects.filter(blog=blog)

    return render(request, "blog_detail.html", {"blog": blog, 'comments': comments})
