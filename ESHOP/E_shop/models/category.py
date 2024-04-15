from django.db import models

class Catagories(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    class Meta:
        db_table = 'category'

    @staticmethod
    def get_all_catagories():
        return Catagories.objects.all()


    