from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from website.models import Contact,Blogs
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from dashboard.forms import BlogForm
from django.contrib.auth.forms import User

class DashboardView (generic.ListView):
    model = Contact
    template_name = "dashboard/contacts.html"
    context_object_name = 'contacts'

    def get_queryset(self):
        return Contact.objects.order_by("id")

class Receivedmsg(generic.DetailView):
    model=Contact
    template_name = "dashboard/receivedmsg.html"
    context_object_name = "message"

class deletemsg(generic.DeleteView):
    model=Contact
    template_name = "dashboard/delete_msg.html"
    success_url="/dashboard"


class BlogView (generic.ListView):
    model = Blogs
    template_name = "dashboard/blogs.html"
    context_object_name = 'Blogs'
    def get_queryset(self):
        return Blogs.objects.order_by("id")

class Blogscontent(generic.DetailView):
    model=Blogs
    template_name = "dashboard/blogcontent.html"
    context_object_name = "content"


def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            q = Blogs()
            q.title= form.cleaned_data["title"]
            q.save()
            q.category= form.cleaned_data["category"]
            q.save()
            q.content= form.cleaned_data["content"]
            q.save()
            q.Status= form.cleaned_data["status"]
            q.save()
            form = BlogForm()
            


    else:
        form = BlogForm()

    return render(request, "dashboard/Blogadd.html", {"blogadd": form})


class deleteblog(generic.DeleteView):
    model=Blogs
    template_name = "dashboard/deleteblog.html"
    success_url="/dashboard/blogs"


class updateblog(generic.UpdateView):
     model=Blogs
     template_name = "dashboard/Blogadd.html"
     success_url="/"
     fields = "__all__"

