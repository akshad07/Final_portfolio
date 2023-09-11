from website.models import Blogs
from django.views import generic

class DashboardView (generic.ListView):
    model = Blogs
    template_name = "dashboard/contacts.html"
    context_object_name = 'contacts'
