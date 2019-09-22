from django.db import migrations, models

# Create your models here.
class Book(models.Model):
    """取扱店"""
    name = models.CharField('会社名', max_length=255)
    publisher = models.CharField('店舗名', max_length=255, blank=True)
    page = models.IntegerField('取扱店CD', blank=True, default=0)

    def __str__(self):
        return self.name


class Impression(models.Model):
    """感想"""
    book = models.ForeignKey(Book, verbose_name='書籍', related_name='impressions', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment

class Customer(models.Model):
    """取扱店"""
    code = models.IntegerField('取扱店CD', blank=True, unique=True)
    company = models.CharField('会社名', max_length=255, blank=True)
    shop = models.CharField('店舗名', max_length=255, blank=True)
    area = models.CharField('管轄', max_length=255, blank=True)
    staff = models.CharField('担当', max_length=255, blank=True)
    Correspondence = models.BooleanField('対応', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer