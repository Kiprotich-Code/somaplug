from django.db import models

# Create your models here.
class AddQuote(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.PositiveIntegerField()
    service = models.CharField(max_length=100)
    expected_time = models.CharField(max_length=20)
    details = models.TextField()
    quote = models.IntegerField()

    def __str__(self):
        return f'{self.quote} from {self.name}'
    

class ContactList(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'Message from {self.email}.'