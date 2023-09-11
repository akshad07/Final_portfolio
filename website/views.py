from django.shortcuts import render
from django.views.generic import CreateView ,ListView,DetailView
from .models import Contact,Blogs
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from . import forms
from django.contrib import messages
def index(request):

    return render(request, 'website/index.html',)


class HomePageView(CreateView):
    template_name = 'website/index.html'
    
    model = Contact
    fields = '__all__'

    def get_success_url(self):
        return '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'My Portfolio'
        context["Blogss"] = Blogs.objects.filter(Status = 1).order_by("id")
        return context
    
class singleblog (DetailView):
    model = Blogs
    template_name = "website/blog-single.html"
    context_object_name = 'Blog'
    
from django.contrib.auth import authenticate, login


def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect("dashboard:messages")
            else:
                message = 'Login failed!'
    return render(request, 'website/login.html', context={'form': form})