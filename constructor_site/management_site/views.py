from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin, View 
class MainView(TemplateResponseMixin,View):
    template_name = 'management-site/index.html'
    def get (self, request):

        return self.render_to_response({})

