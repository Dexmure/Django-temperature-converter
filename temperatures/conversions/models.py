from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


def validate_choice(value):
    if (value!="C" and value !="F"):
     raise ValidationError("the unit must be either 'C' our 'F' ")
 
 
class User (models.Model):
    id = models.AutoField(primary_key=True)
    username= models.CharField( max_length=50)
    
class Historic(models.Model): 
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add=True) 
    val_initial = models.FloatField()
    val_final = models.FloatField()
    
    CONV_CHOICES =(("C","CELSIUS"),("F","FAHRENHEIT"))
    initial_conv = models.CharField(max_length=1, choices=CONV_CHOICES, validators= [validate_choice])
    final_conv = models.CharField(max_length=1, choices=CONV_CHOICES, validators=[validate_choice])

    def save(self,*args, **kwargs):
        self.full_clean() 
        super(Historic, self).save(*args, **kwargs)
    
        
    

        
        
    
    
        
    
