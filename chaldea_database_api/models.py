from django.db import models


# Create your models here.
class Servant(models.Model):
    number = models.IntegerField(primary_key=True, verbose_name="No.")
    name = models.CharField(max_length=50, verbose_name="名前")
    name_en = models.CharField(max_length=50, verbose_name="英語名")
    class_name = models.ForeignKey('Class', on_delete=models.CASCADE, verbose_name="クラス")
    rarity = models.IntegerField(choices=((5, "★5"), (4, "★4"), (3, "★3"), (2, "★2"), (1, "★1"), (0, "★0")), verbose_name="レアリティ")

    def __str__(self):
        return f"{self.get_rarity_display()} {self.name} ({self.class_name})"


class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
