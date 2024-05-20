from django.db import models

# Create your models here.

class Cat(models.Model):
    cat_image = models.ImageField(upload_to='cats_img/', height_field=None, width_field=None, max_length=100)
    elo = models.IntegerField(default=0)
    cat_name = models.CharField(max_length=255)
    class Meta:
        app_label = 'catter_index'  
    
    def __str__(self):
        return str(self.id)  # Ensure string representation is the id

    
    


