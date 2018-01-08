from django.contrib.auth.decorators import login_required
from splunkdj.decorators.render import render_to
# from django.conf import settings
from ConfigParser import SafeConfigParser

# Imports for the setup view
from .forms import SetupForm
from django.core.urlresolvers import reverse
from splunkdj.setup import config_required
from splunkdj.setup import create_setup_view_context

Input_Data_Choices = (
    ('1', 'Less than 20GB'),
    ('2', '20GB-100GB'),
    ('3', '100GB-250GB'),
    ('4', '250GB-500GB'),
    ('5', '500GB-750GB'),
    ('6', '750GB-1TB'),
    ('7', '1TB-2TB'),
    ('8', '2TB-3TB')
)

@render_to('Splunk_Dimensioning:home.html')
@login_required
@config_required
def home(request):   
    return { 
            'message': "Hello world from inside the application",
            }

@render_to('Splunk_Dimensioning:setup.html')
@login_required
def setup(request):
    return create_setup_view_context(
        request,
        SetupForm,  # The form class to use
        reverse('Splunk_Dimensioning:page1'))  # Where to redirect the user after completing setup

 
@render_to('Splunk_Dimensioning:page1.html')
@login_required
@config_required
def page1(request): 
    config = SafeConfigParser()
    config.read('/opt/splunk/etc/apps/Splunk_Dimensioning/local/mysetup.conf')
    DailyData = int(config.get('inputdata', 'data'))
    users = int(config.get('inputdata', 'usersorcons'))
    Number = int(config.get('inputdata', 'number'))
    sch_src = int(config.get('inputdata', 'ssearches'))
    
    #initialization
    src_head = 0
    indexers = 0
    
    if (users == 1) :
        tcon_src = Number + sch_src/2
    else:
        tcon_src = (Number + sch_src)/2
    
    if tcon_src < 4:
        if DailyData <= 2:
            src_head = 0  
            indexers = 1
        elif DailyData <= 250:
            src_head = 0  
            indexers = 1
        elif DailyData <= 500:
            src_head = 1  
            indexers = 2
        elif DailyData <= 750:
            src_head = 1  
            indexers = 3
        elif DailyData <= 1000:
            src_head = 1  
            indexers = 4
        elif DailyData <= 2000:
            src_head = 1  
            indexers = 8
        elif DailyData <= 3000:
            src_head = 1  
            indexers = 12
 
    elif tcon_src < 8:
        if DailyData <= 2:
            src_head = 0  
            indexers = 1
        elif DailyData <= 250:
            src_head = 1  
            indexers = 1
        elif DailyData <= 500:
            src_head = 1  
            indexers = 2
        elif DailyData <= 750:
            src_head = 1  
            indexers = 4
        elif DailyData <= 1000:
            src_head = 1  
            indexers = 5
        elif DailyData <= 2000:
            src_head = 1  
            indexers = 10
        elif DailyData <= 3000:
            src_head = 1  
            indexers = 15
  
    elif tcon_src < 16:
        if DailyData <= 2:
            src_head = 1  
            indexers = 1
        elif DailyData <= 250:
            src_head = 1  
            indexers = 1
        elif DailyData <= 500:
            src_head = 1  
            indexers = 3
        elif DailyData <= 750:
            src_head = 1  
            indexers = 4
        elif DailyData <= 1000:
            src_head = 2  
            indexers = 6
        elif DailyData <= 2000:
            src_head = 2  
            indexers = 12
        elif DailyData <= 3000:
            src_head = 2  
            indexers = 18

    elif tcon_src <24:
        if DailyData <= 2:
            src_head = 1  
            indexers = 1
        elif DailyData <= 250:
            src_head = 1  
            indexers = 2
        elif DailyData <= 500:
            src_head = 2  
            indexers = 3
        elif DailyData <= 750:
            src_head = 2  
            indexers = 4
        elif DailyData <= 1000:
            src_head = 2  
            indexers = 6
        elif DailyData <= 2000:
            src_head = 2  
            indexers = 12
        elif DailyData <= 3000:
            src_head = 2  
            indexers = 18
    
    elif tcon_src <48:
        if DailyData <= 2:
            src_head = 1  
            indexers = 2
        elif DailyData <= 250:
            src_head = 1  
            indexers = 2
        elif DailyData <= 500:
            src_head = 2  
            indexers = 3
        elif DailyData <= 750:
            src_head = 2  
            indexers = 4
        elif DailyData <= 1000:
            src_head = 3  
            indexers = 8
        elif DailyData <= 2000:
            src_head = 3  
            indexers = 16
        elif DailyData <= 3000:
            src_head = 3  
            indexers = 24
            
            
    return { 
            'daily_data': DailyData,
            'search_heads': src_head,
            'indexrs': indexers,
            'sch_src': sch_src,
            'totcon_src': tcon_src,
            'Number': Number
            }
