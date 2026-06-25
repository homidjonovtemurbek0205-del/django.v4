from django.shortcuts import render
from core.models import Mahsulot
# Create your views here.
def hello(request):
    # book = Book.objects.create(title = "Binafsha shulasi", price = 100)
    # book = Book.objects.create(title = "Binafsha shulasi 2", price = 50)
    # book = Book.objects.create(title="Django for Beginners", price=45)
    # book = Book.objects.create(title="Python Pro Tips", price=120)
    # book = Book.objects.create(title="Learning Python", price=25)
    # book = Book.objects.create(title="Advanced Django Pro", price=85)
    # print(book)
    Mahsulot.objects.get_or_create(nomi="iPhone 15", tavsifi="Smartfon", narxi=1200.00, chegirmadagi_narxi=1099.00, ombordagi_soni=15, aktiv_holati=True)
    Mahsulot.objects.get_or_create(nomi="AirPods Pro", tavsifi="Quloqchin", narxi=280.00, chegirmadagi_narxi=249.00, ombordagi_soni=30, aktiv_holati=True)
    Mahsulot.objects.get_or_create(nomi="MX Master 3S", tavsifi="Sichqoncha", narxi=110.00, chegirmadagi_narxi=95.00, ombordagi_soni=20, aktiv_holati=True)
    Mahsulot.objects.get_or_create(nomi="Dell 27\"", tavsifi="Monitor", narxi=550.00, chegirmadagi_narxi=499.00, ombordagi_soni=8, aktiv_holati=True)
    Mahsulot.objects.get_or_create(nomi="Power Bank", tavsifi="20000 mA·soat sig‘imli", narxi=65.00, chegirmadagi_narxi=55.00, ombordagi_soni=50, aktiv_holati=True)
    Mahsulot.objects.get_or_create(nomi="Sony XM5", tavsifi="Naushnik", narxi=399.00, chegirmadagi_narxi=349.00, ombordagi_soni=0, aktiv_holati=False)
    return render(request, 'index.html')