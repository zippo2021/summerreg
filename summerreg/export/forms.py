from django.forms import Form, BooleanField, ChoiceField
from dashboard.models import UserData
class showdb_form(Form):
    def __init__(self, *args, **kwargs):  
        CITY_CHOICES = list(UserData.objects.values_list('city', flat = True))+['all']
	super(showdb_form, self).__init__(*args, **kwargs)
        for each in CITY_CHOICES:
            self.fields['%s' % each] = BooleanField()
    accepted = ChoiceField(choices=(('all','all'),('not_accepted','not applyed')), label="Show")
