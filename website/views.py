from django.shortcuts import render
from django.views.generic import CreateView ,ListView,DetailView
from .models import Contact,Blogs


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
    