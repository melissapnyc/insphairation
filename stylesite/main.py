"""A simple webapp2 server."""
import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('latest_hairstyles_list')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

"""
import webapp2
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from hairstyles.models import Style, Image
from datetime import datetime, timedelta, tzinfo

class MainPage(webapp2.RequestHandler):

    def get(self):
        
        self.response.write('hello')
        latest_hairstyle_list = Style.objects.order_by('pub_date')[:]
        context = {'latest_hairstyle_list': latest_hairstyle_list}
        return render(request, 'hairstyles/index.html', context)
        


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

"""