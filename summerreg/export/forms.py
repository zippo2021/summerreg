from django.forms import Form, BooleanField, ChoiceField
from dashboard.models import UserData
class showdb_form(Form):
    #dynamic form, fields: checkboxes 
    def __init__(self, *args, **kwargs):  
        CITY_CHOICES = list(UserData.objects.values_list('city', flat = True))+['all']
	super(showdb_form, self).__init__(*args, **kwargs)
	for each in CITY_CHOICES:
	    self.fields['city_%s' % each] = BooleanField(label = '%s' % each, required = False)
    #dynamic form, static fields
    accepted = ChoiceField(choices=(('accepted_all','all'),('accepted_not','not applyed')), required = False)
    #special
    def get_city_choices():
	return CITY_CHOICES[:].remove('all')
    
