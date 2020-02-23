from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=40, db_column="title")
    publish_date = models.DateField()
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=5, max_digits=6)

    # class Meta:
    #     db_table = "book"
