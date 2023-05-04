from django.db import models

# Create your models here.
class store(models.Model):
    category_list = ('Phone & Computers','Phone & Computers'),('Television','Television'),('Wearables & Accessories', 'Wearables & Accessories'),('Home Appliances','Home Appliances')
    title = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False , default=0)
    Strikethrough_pricing = models.PositiveBigIntegerField(null=True, blank=True)
    description = models.TextField(max_length=1500)
    category = models.CharField( choices=category_list, default='Phone & Computers' , max_length=100, null=False)
    image = models.CharField(max_length=1500, null=False )
    rating = models.FloatField(null=False , default=0)
    count = models.PositiveBigIntegerField(null=False, default=1)
    product_quanity = models.PositiveBigIntegerField(null=False, default=1)



class customerDetails(models.Model):
    First_Name = models.CharField(max_length=100, null=False)
    last_Name = models.CharField(max_length=100, null=False)
    Street_address = models.CharField(max_length=300, null=False)
    Street_address_2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=False)
    State = models.CharField(max_length=100, null=False)
    zip_code = models.PositiveBigIntegerField(null=False, blank=False)
    country = models.CharField(max_length=100, null=False)
    phone_number = models.PositiveBigIntegerField(null=False)
    email = models.EmailField()


    



