from django.db import models
from django.forms import ModelForm

# Create your models here.

class User(models.Model):
    profile_name = models.CharField(max_length=150, blank=False)
    img = models.ImageField(upload_to="img/", blank=True)
    likes = models.IntegerField(default = 0, blank=True)

    def __str__(self):
        return self.profile_name
    

    
#class UserForm(ModelForm):
#    class Meta:
#        model = User
#        fields = '__all__'
        
    