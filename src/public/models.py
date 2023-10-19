from django.db import models


class Certificate(models.Model):
    picture = models.ImageField(upload_to='images/certificates')


