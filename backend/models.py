from django.db import models
from django.utils.translation import gettext_lazy as _



# category model

class Category (models.Model):

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'

# brand model

class BrandStatus(models.TextChoices):

    PUBLISHED = 'PUBLISHED', _('PUBLISHED')
    DRAFT = 'DRAFT', _('DRAFT')
    PENDING = 'PENDING', _('PENDING')

class Brand(models.Model):

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=255)

    image_path = models.ImageField(upload_to='brand', null=True, blank=True, default='No_image_available.jpg')

    status = models.CharField(
        max_length=255,
        choices=BrandStatus.choices,
        default=BrandStatus.PUBLISHED
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'brand'

# product model

class Product(models.Model):

    id = models.BigAutoField(primary_key= True)

    name = models.CharField(max_length=255)

    image_path = models.ImageField(upload_to='product', null=True, blank=True, default='No_image_available.jpg' )

    description =models.TextField()

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)

    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    qty = models.IntegerField(null=True, blank=True)

    alert_stock = models.IntegerField(null=True, blank=True)

    image_path = models.ImageField(upload_to='product', null=True, blank=True, default='no-image-available.jpg')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
