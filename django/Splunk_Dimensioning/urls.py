from django.conf.urls import patterns, include, url
from splunkdj.utility.views import render_template as render

urlpatterns = patterns('',
    url(r'^home/$', 'Splunk_Dimensioning.views.home', name='home'),
    url(r'^setup/$', 'Splunk_Dimensioning.views.setup', name='setup'),
    url(r'^page1/$', 'Splunk_Dimensioning.views.page1', name='page1')
)
