from django.db import models



def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


# Create your models here.
class Party(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Party'
        verbose_name_plural = 'Parties'


    def __str__(self):
        return self.name
