from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        null=True,
    )

    def __str__(self):
        return f'{self.username} - {self.password} - {self.email} - {self.first_name} - {self.last_name}  - {self.age}'