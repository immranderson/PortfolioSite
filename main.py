#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import sys
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import wsgiref.handlers

class IntroPage(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world!')
        
        template_values = { "generic": "generic" }
        path = os.path.join(os.path.dirname(__file__), 'templates/intropage.html')
        self.response.out.write(template.render(path, template_values))
        
        
class HackerDojoPage(webapp2.RequestHandler):
    def get(self):
        template_values = { "generic": "generic" }
        path = os.path.join(os.path.dirname(__file__), 'templates/hackerdojo.html')
        self.response.out.write(template.render(path, template_values))
        
class EmotionLinePage(webapp2.RequestHandler):
    def get(self):
        template_values = { "generic": "generic" }
        path = os.path.join(os.path.dirname(__file__), 'templates/emotionline.html')
        self.response.out.write(template.render(path, template_values))
        
class CoursesPage(webapp2.RequestHandler):
    def get(self):
        template_values = { "generic": "generic" }
        path = os.path.join(os.path.dirname(__file__), 'templates/courses.html')
        self.response.out.write(template.render(path, template_values))
        
class BadgePage(webapp2.RequestHandler):
    def get(self):
        template_values = { "generic": "generic" }
        path = os.path.join(os.path.dirname(__file__), 'templates/piratebadge.html')
        self.response.out.write(template.render(path, template_values))
        
class MovePage(webapp2.RequestHandler):
    def get(self):
        template_values = { "generic": "generic" }
        path = os.path.join(os.path.dirname(__file__), 'templates/testmove.html')
        self.response.out.write(template.render(path, template_values))
            

app = webapp2.WSGIApplication([('/', IntroPage),
                               ('/android/hackerdojo', HackerDojoPage),                               
                               ('/android/emotionline', EmotionLinePage),
                               ('/courses/', CoursesPage),
#                                ('/piratebadge', BadgePage),
#                                ('/testmove', MovePage),
                               ], debug=True)
