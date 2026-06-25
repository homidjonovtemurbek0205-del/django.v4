# from django.shortcuts import render
# from core.models import Book

# # Create your views here.
# from core.models import Book

# def run():

    # 3. Barcha ma’lumotlarni olib keladigan query
    # books = Book.objects.all()
    # print("3. Barcha kitoblar:", books)
    
    # # 4. Narxi 50 dan katta bo‘lgan barcha booklar
    # books = Book.objects.filter(price__gt=50)
    
    # # 5. Title ichida “django” so‘zi bor barcha booklar (case insensitive)
    # books = Book.objects.filter(title__icontains='django')
    
    # # 6. Narxi 20 va 100 oralig‘ida bo‘lgan booklar
    # books = Book.objects.filter(price__range=(20, 100))
    
    # # 7. ID si 1, 3, 5 bo‘lgan booklar
    # books = Book.objects.filter(id__in=[1, 3, 5])
    
    # # 8. Title “Python” bilan boshlanadigan booklar
    # books = Book.objects.filter(title__istartswith='python')
    
    # # 9. Title “Pro” bilan tugaydigan booklar
    # books = Book.objects.filter(title__iendswith='pro')
    
    # # 10. Narxi 30 dan kichik bo‘lmagan booklar
    # books = Book.objects.filter(price__gte=30)
    
    # # 11. Narxi 40 dan kichik bo‘lgan booklardan tashqari hamma booklarni chiqaring
    # books = Book.objects.exclude(price__lt=40)
    
    # # 12. Barcha booklarni narx bo‘yicha o‘sish tartibida sort qilish
    # books = Book.objects.all().order_by('price')
    
    # # 13. Barcha booklarni narx bo‘yicha kamayish tartibida sort qilish
    # books = Book.objects.all().order_by('-price')
    
    # # 14. Eng arzon bookni topish
    # book = Book.objects.all().order_by('price').first()
    
    # # 15. Eng qimmat bookni topish
    # book = Book.objects.all().order_by('-price').first()
    
    # # 16. Birinchi 3 ta bookni olib kelish
    # books = Book.objects.all()[:3]
    
    # # 17. 4–8 indeks oralig‘idagi booklarni olib keling
    # books = Book.objects.all()[4:8]
    
    # # 18. Booklar sonini hisoblash
    # print("18. Kitoblar soni:", Book.objects.count())
    
    # # 19. Kamida bitta book mavjudligini tekshiring
    # print("19. Kamida bitta bormi?:", Book.objects.exists())
    
    # # 20. Har bir bookdan faqat title va price ni olib kelish
    # books = Book.objects.values('title', 'price')
    
    # # 21. Har bir bookdan faqat title ni list ko‘rinishida olib kelish
    # books = Book.objects.values_list('title', flat=True)
    
    # # 22. Null bo‘lgan booklarni topish
    # books = Book.objects.filter(price__isnull=True)
    
    # # 23. Faqat published bo‘lgan booklarni chiqarish
    # books = Book.objects.filter(status='published')
    
    # # 30. Title ichida “a” harfi bor booklarni filter qilish
    # books = Book.objects.filter(title__icontains='a')
    
    # print( books)




from django.shortcuts import render
from django.db.models import Q 
from core.models import Mahsulot

def run():
    Mahsulot.objects.get_or_create(nomi="iPhone 15", tavsifi="Smartfon", narxi=1200.00, chegirmadagi_narxi=1099.00, ombordagi_soni=15, aktiv_holati=True)
    Mahsulot.objects.get_or_create(nomi="AirPods Pro", tavsifi="Quloqchin", narxi=280.00, chegirmadagi_narxi=249.00, ombordagi_soni=30, aktiv_holati=True)
    Mahsulot.objects.get_or_create(nomi="MX Master 3S", tavsifi="Sichqoncha", narxi=110.00, chegirmadagi_narxi=95.00, ombordagi_soni=20, aktiv_holati=True)
    Mahsulot.objects.get_or_create(nomi="Dell 27\"", tavsifi="Monitor", narxi=550.00, chegirmadagi_narxi=499.00, ombordagi_soni=8, aktiv_holati=True)
    Mahsulot.objects.get_or_create(nomi="Power Bank", tavsifi="20000 mA·soat sig‘imli", narxi=65.00, chegirmadagi_narxi=55.00, ombordagi_soni=50, aktiv_holati=True)
    Mahsulot.objects.get_or_create(nomi="Sony XM5", tavsifi="Naushnik", narxi=399.00, chegirmadagi_narxi=349.00, ombordagi_soni=0, aktiv_holati=False)

    # 1. Aktiv holati yoqilgan bo‘lgan barcha mahsulotlar
    mahsulotlar = Mahsulot.objects.filter(aktiv_holati=True)
    print(mahsulotlar)

    # 2. Narxi 100 dan katta bo‘lgan mahsulotlar
    mahsulotlar = Mahsulot.objects.filter(narxi__gt=100)
    print(mahsulotlar)

    # 3. Chegirmadagi narxi kiritilmagan mahsulotlar
    mahsulotlar = Mahsulot.objects.filter(chegirmadagi_narxi__isnull=True)
    print(mahsulotlar)

    # 4. Ombordagi soni 0 dan katta bo‘lgan mahsulotlar
    mahsulotlar = Mahsulot.objects.filter(ombordagi_soni__gt=0)
    print(mahsulotlar)

    # 5. Ombordagi soni 0 ga teng bo‘lgan mahsulotlar
    mahsulotlar = Mahsulot.objects.filter(ombordagi_soni=0)
    print(mahsulotlar)

    # 6. Narxi 50 dan 200 gacha bo‘lgan mahsulotlar
    mahsulotlar = Mahsulot.objects.filter(narxi__range=(50, 200))
    print(mahsulotlar)

    # 7. Nomi ichida "pro" so‘zi bor mahsulotlar (case insensitive)
    mahsulotlar = Mahsulot.objects.filter(nomi__icontains="pro")
    print(mahsulotlar)

    # 8. Nomi "A" harfi bilan boshlanadigan mahsulotlar
    mahsulotlar = Mahsulot.objects.filter(nomi__istartswith="A")
    print(mahsulotlar)

    # 9. Tavsifi ichida "gaming" so‘zi bor mahsulotlar
    mahsulotlar = Mahsulot.objects.filter(tavsifi__icontains="gaming")
    print(mahsulotlar)

    # 10. Identifikator raqami 2, 4, 6 va 8 bo‘lgan mahsulotlar
    mahsulotlar = Mahsulot.objects.filter(id__in=[2, 4, 6, 8])
    print(mahsulotlar)

    # 11. Mahsulotlarni narxi bo‘yicha o‘sish tartibida saralash
    mahsulotlar = Mahsulot.objects.all().order_by('narxi')
    print(mahsulotlar)

    # 12. Mahsulotlarni narxi bo‘yicha kamayish tartibida saralash
    mahsulotlar = Mahsulot.objects.all().order_by('-narxi')
    print(mahsulotlar)

    # 13. Birinchi 5 ta mahsulotni olib kelish
    mahsulotlar = Mahsulot.objects.all()[:5]
    print(mahsulotlar)

    # 14. 10-dan 20-gacha bo‘lgan o‘rindagi mahsulotlar
    mahsulotlar = Mahsulot.objects.all()[10:20]
    print(mahsulotlar)

    # 15. Barcha mahsulotlar sonini hisoblash
    print(Mahsulot.objects.count())

    # 16. Kamida bitta aktiv mahsulot mavjudligini tekshiring
    print(Mahsulot.objects.filter(aktiv_holati=True).exists())

    # 17. Chegirmadagi narxi mavjud bo‘lgan mahsulotlar
    mahsulotlar = Mahsulot.objects.filter(chegirmadagi_narxi__isnull=False)
    print(mahsulotlar)

    # 18. Chegirmadagi narxi kiritilmagan mahsulotlarni chiqarib tashlash
    mahsulotlar = Mahsulot.objects.exclude(chegirmadagi_narxi__isnull=True)
    print(mahsulotlar)

    # 19. Ombordagi soni 10 tadan kam bo‘lgan mahsulotlar
    mahsulotlar = Mahsulot.objects.filter(ombordagi_soni__lt=10)
    print(mahsulotlar)

    # 20. Ombordagi soni 10 ta yoki undan ko‘p bo‘lgan mahsulotlar
    mahsulotlar = Mahsulot.objects.filter(ombordagi_soni__gte=10)
    print(mahsulotlar)

    # 21. Narxi 100 dan katta bo‘lgan mahsulotlardan boshqa barcha mahsulotlar
    mahsulotlar = Mahsulot.objects.exclude(narxi__gt=100)
    print(mahsulotlar)

    # 22. Nomi ichida "pro" mavjud YOKI narxi 50 dan kichik bo‘lgan mahsulotlar (Mustaqil topshiriq yechimi)
    mahsulotlar = Mahsulot.objects.filter(Q(nomi__icontains="pro") | Q(narxi__lt=50))
    print(mahsulotlar)

    print(mahsulotlar)