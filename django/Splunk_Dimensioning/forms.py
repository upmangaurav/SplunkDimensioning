from splunkdj.setup import forms   # Replaces 'from django import forms'
from django.template.defaultfilters import default
from splunk.field_extractor.FieldLearning import MAX_VALUE_REGEX

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

CHOICES = (('0', 'No. of concurrent searches',), ('1', 'No. of Splunk users',))

class SetupForm(forms.Form):
    # The input fields are saved in a custom mysetup.conf file
    data = forms.IntegerField(
        label="Amount of incoming data per day(GB)", required=True, max_value=3000, min_value=20,
        endpoint="configs/conf-mysetup", entity="inputdata", field="data")
    usersorcons = forms.ChoiceField(
        label="Choose search paramater:",
        required=True, endpoint="configs/conf-mysetup", entity="inputdata", field="usersorcons", 
        widget=forms.RadioSelect, choices=CHOICES)
    number = forms.IntegerField(
        label="Number of users/concurrent-searches:",
        endpoint="configs/conf-mysetup", entity="inputdata", field="number")
    ssearches = forms.IntegerField(
        required=True, label="Number of scheduled searches",
        endpoint="configs/conf-mysetup", entity="inputdata", field="ssearches")