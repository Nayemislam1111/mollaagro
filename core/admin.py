from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Category, Product, ProductImage, Order, LegalDocument


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_per_page = 20
    prepopulated_fields = {'slug': ('name',)}


# প্রোডাক্টের ভেতরে একাধিক ছবি আপলোড করার জন্য ইনলাইন ক্লাস
class ProductImageInline(TabularInline):
    model = ProductImage
    extra = 3  # একসাথে কয়টি ছবি আপলোডের ফিল্ড দেখাবে


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('title', 'category', 'price', 'is_available', 'created_at')
    list_filter = ('category', 'is_available', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('price', 'is_available')  # লিস্ট পেজ থেকেই সরাসরি দাম বা অ্যাভেইলঅ্যাবিলিটি বদলানো যাবে
    list_per_page = 20
    inlines = [ProductImageInline]  # এখানে ইনলাইন যুক্ত করা হলো যাতে প্রোডাক্ট পেজ থেকেই ছবি আপলোড করা যায়


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ('customer_name', 'product_title', 'quantity', 'phone', 'address', 'created_at')
    list_filter = ('created_at', 'product_title')
    search_fields = ('customer_name', 'phone', 'product_title', 'address')
    date_hierarchy = 'created_at'  # তারিখ অনুযায়ী ড্রিল-ডাউন করার জন্য প্রিমিয়াম বার
    list_per_page = 20
    readonly_fields = ('created_at',)  # তৈরির সময় ও তারিখ পরিবর্তন করা যাবে না (সিকিউরিটির জন্য)


# নতুন মডেল: ট্রেড লাইসেন্স ও অন্যান্য ডকুমেন্টের জন্য
@admin.register(LegalDocument)
class LegalDocumentAdmin(ModelAdmin):
    list_display = ('title', 'uploaded_at')  # লিস্টে ডকুমেন্টের নাম ও আপলোডের সময় দেখাবে
    search_fields = ('title',)
    list_filter = ('uploaded_at',)
    list_per_page = 20
    readonly_fields = ('uploaded_at',)