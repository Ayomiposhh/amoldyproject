from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.


class Contact(models.Model):
  name= models.CharField(max_length= 100,null=True,blank=True)
  email=models.EmailField()
  message=models.TextField()

  def __str__(self): 
    return self.name
  
class Categories(models.Model):
  name= models.CharField(max_length= 100,null=True,blank=True)
  slug = models.SlugField(max_length=300, unique=True)
  
  def __str__(self): 
    return self.name

class ShopManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(Q(is_active=True) | Q(percent=True))


class Shop(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    category = models.ForeignKey(Categories, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    price = models.FloatField(verbose_name='Price')
    market_price = models.FloatField(verbose_name='Market Price')
    author = models.CharField(max_length=300, default='admin')
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    new_product = models.BooleanField(verbose_name='New Product', blank=True, null=True)
    hot_deal = models.BooleanField( verbose_name='Hot Deals of this Week', blank=True, null=True)
    featured = models.BooleanField( verbose_name='Featured', blank=True, null=True)
    best_seller = models.BooleanField(blank=True, null=True, default=False)
    image1 = models.ImageField(upload_to='images/', default='images/default.png')
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    contents = HTMLField('Content')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = models.Manager()
    @property
    def get_price(self):
        format_number = "{:,}".format(self.price)
        if self.percent:
            return format_html(f'<span class="old-price">&#8358;{format_number} </span>')
        else:
            return format_html(f'<span class="price">&#8358;{format_number} </span>')
    
    class Meta:
        verbose_name_plural='Products'
        ordering = ('-created',)

    def show_image1(self):
        if self.image1:
            return self.image1.url
        

    def show_image2(self):
        if self.image2:
            return self.image2.url
        

    def show_image3(self):
        if self.image3:
            return self.image3.url
       
    
    def get_absolute_url(self):
        return reverse('frontend:product_detail', args=[self.slug])

   

    def __str__(self):
        return self.title

  
  