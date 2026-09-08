from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
import requests
from .models import Category, LegalDocument, Order, Product


# হোমপেজ ভিউ (ট্রেড লাইসেন্স ও লিগ্যাল ডকুমেন্ট সহ)
def home_view(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)
    legal_documents = (
        LegalDocument.objects.all()
    )  # ট্রেড লাইসেন্স বা ভোটার আইডি ডাটা কুয়েরি করা হলো

    context = {
        'categories': categories,
        'products': products,
        'legal_documents': legal_documents,  # কনটেক্সটে পাস করা হলো
    }
    return render(request, 'core/index.html', context)


# ইউজার সাইন-আপ (Registration) ভিউ
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # রেজিস্টার করার পর অটো লগইন হয়ে যাবে
            messages.success(request, 'আপনার অ্যাকাউন্ট সফলভাবে তৈরি হয়েছে!')
            return redirect('home')
        else:
            messages.error(request, 'দয়া করে সঠিক তথ্য দিয়ে ফর্মটি পূরণ করুন।')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})


# ইউজার লগইন ভিউ
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'স্বাগতম, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'ভুল ইউজারনেম বা পাসওয়ার্ড!')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


# ইউজার লগআউট ভিউ
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'সফলভাবে লগআউট করা হয়েছে।')
        return redirect('home')
    return redirect('home')


# টেলিগ্রাম নোটিফিকেশন পাঠানোর ফাংশন
def send_telegram_notification(order):
    TOKEN = '8853594328:AAEbCyyTpjAeucGIZeDxhub3yqHtw44kjB8'
    CHAT_ID = '6113658597'

    message = (
        f'🚨 **নতুন অর্ডার এসেছে!** 🚨\n\n'
        f'📦 **প্রোডাক্ট:** {order.product_title}\n'
        f'⚖️ **পরিমাণ:** {order.quantity}\n'
        f'👤 **নাম:** {order.customer_name}\n'
        f'📞 **ফোন:** {order.phone}\n'
        f'📍 **ঠিকানা:** {order.address}\n'
        f"🕒 **সময়:** {order.created_at.strftime('%d-%m-%Y %I:%M %p')}"
    )

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown',
    }

    try:
        requests.post(url, data=payload)
    except Exception as e:
        print('Telegram Error:', e)


# প্রোডাক্ট অর্ডার সাবমিট ভিউ (কোয়ান্টিটি ও টেলিগ্রাম নোটিফিকেশন সহ)
def submit_order(request):
    if request.method == 'POST':
        product_title = request.POST.get('product_title')
        quantity = request.POST.get('quantity')
        customer_name = request.POST.get('customer_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # ডাটাবেজে পরিমাণসহ অর্ডার সেভ করা হচ্ছে
        order = Order.objects.create(
            product_title=product_title,
            quantity=quantity,
            customer_name=customer_name,
            phone=phone,
            address=address,
        )

        # অর্ডার সফল হওয়ার পর টেলিগ্রামে নোটিফিকেশন পাঠানো হচ্ছে
        send_telegram_notification(order)

        messages.success(
            request,
            'আপনার অর্ডারটি সফলভাবে গ্রহণ করা হয়েছে! খুব শীঘ্রই আমরা আপনার সাথে যোগাযোগ করব।',
        )
        return redirect('home')

    return redirect('home')