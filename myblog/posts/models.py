from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=250)
    pub_data = models.DateTimeField()
    image = models.ImageField(upload_to='media')
    body = models.TextField()

    def __str__(self):
        return self.title

    def pub_data_pretty(self):
        return self.pub_data.strftime('%d %b %Y')

    def summary(self):
        return self.body[:100]
