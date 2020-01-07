from django.db import models


# Create your models here.
class Servant(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    class_name = models.ForeignKey('Class', on_delete=models.CASCADE)
    rarity = models.IntegerField(choices=((5, "★5"), (4, "★4"), (3, "★3"), (2, "★2"), (1, "★1"), (0, "★0")))

    def __str__(self):
        return f"{self.get_rarity_display()} {self.name} ({self.class_name})"


class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
