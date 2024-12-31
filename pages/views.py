from django.views import generic


class AboutUsView(generic.TemplateView):
    template_name = 'pages/about_us.html'
