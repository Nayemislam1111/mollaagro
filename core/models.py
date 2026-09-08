from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)  # Fish Fry, Poultry, Feed
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # পূর্বের একক image ফিল্ডটি বাদ দেওয়া হয়েছে, এখন ProductImage মডেল ব্যবহার করা হবে
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


# নতুন মডেল: একটি প্রোডাক্টের একাধিক ছবি সংরক্ষণের জন্য
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images'
    )
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return f'Image for {self.product.title}'

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'


# নতুন মডেল: ট্রেড লাইসেন্স, ভোটার আইডি কার্ড বা অন্যান্য বৈধ কাগজপত্র সংরক্ষণের জন্য
class LegalDocument(models.Model):
    title = models.CharField(max_length=255, verbose_name="ডকুমেন্টের নাম (যেমন: ট্রেড লাইসেন্স / ভোটার আইডি)")
    image = models.ImageField(upload_to='legal_docs/', verbose_name="ডকুমেন্টের ছবি")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Legal Document'
        verbose_name_plural = 'Legal Documents'


class Order(models.Model):
    product_title = models.CharField(max_length=255)
    quantity = models.CharField(max_length=50, default='1')  # কত কেজি বা পিস
    customer_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer_name} - {self.product_title} ({self.quantity})'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'