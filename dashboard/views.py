from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView


class DashboardView(TemplateView):
    val = 1
    template_name ="dashboard/index.html"

