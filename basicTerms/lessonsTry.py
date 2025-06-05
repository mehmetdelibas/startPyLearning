#lessons
import random


# #radnom
# print(random.randrange(1,11,3))
# #artış miktarli random
# print(random.randrange(1,11,3))

# #randrangeden rakı iki tarafta dahil
# print(random.randint(1,4))

# #listede random bir öğe dödürür
# myList = ["apple","banana","watermelon","orange"]
# print(random.choice(myList))

# #liste halinde getirir, weights=hangisine agırlık versin k=adet seayisi
# print(random.choices(myList,weights=[5,2,2,2],k=20))

# #shuffle seriyi random sıralarla döndürür
# myList2=["red","blue","dark","white"]
# random.shuffle(myList2)
# print(myList2)

# #verdigin listeden random veri getriri ama bozmaz listeyi k=adet sayisi
# myList3=["red","blue","dark","white"]
# print(random.sample(myList3,3))

# #iki parametre arası ondalıklı random sayı dondurur
# print(random.uniform(2,6))

# #random sayı uretırken agırlıklı olarak hangı sayısa yakın olacagını ayarlamak için kullanılır
# print(random.triangular(20,70,69))

# #dongu kullanımı
# cars=["bmw","auidi","merc","volvo"]
# for x in cars:
#     print(x)

# #lste uzunlugu bulma boşlukta sayılır
# text="python is weird"
# print(len(text))

# #in ile lsitenin içinde aranan kelımenın varlıgı sorgulanır
# text="The best lanugage in life are free!"
# search="Th"
# if search in text:
#     print("Yes text have")
# else:
#     print("No have")

#modify string

# text = "Python is doing well"
# print(text.upper())
# print(text.lower())

# #bas ve sondakı bosluklari kaldırmak için gerkelı olan fonk
# print(text.strip()) 
# print(text.replace("P","A"))
# #ayırmak için
# print(text.split(" "))

# age=23
# name = "metin"
# # text = "Name = {0}, Age = {1}".format(name,age)
# # print(text)
# text = f"Name = {name}, Age = {age}"
# print(text)

# vize = float(input("vize notu giriniz :"))
# final = float(input("final notu giriniz :"))
# sonuc = (vize*0.4+final*0.6)
# if sonuc > 35:
#     print("geçti")
# else:
#     print("kaldi")
# print(sonuc)
# upper=> hepsi buyuk lowe => hepsi kucuk captitalize=>ilk harfi büyük
# casefold=> lowerden daha cok harfı donusturur lowerden daha yavas calısır
# title=> her kelimenin ilk harfi buyuk olur numarlardan sonra da buyuk başlar
# swapcase=> buykluklerı degistiri
# islowe=>isupper=> hepsi buyuk veya kucukse true olur
# center()=> stringi ortalar 
# text = "Welcome to my world"
# resılt = text.center(30,"-")
# print(resılt)

# count=> arnan şeyin strtinge kaç adet oldugunu gosterıor
# enswith startswith başlangıcta verdiign degerle baslıyorsa veya bitiyorsa true
# expandtabs=> \₺ boşluklarını defult8 alır ve () içine rakam yazarak ayarlarsım
# find=> yazılan harf veya kelımenın indexini dödürür
# isalnum stringedkiler harf sayi veya harf+sayisya tru doner
# isalpha=> tum liste harfse tru doner
# isascii=> tum liste asciyse true doner
# isdecimal=> isdigit=> sadece rakamsa true doner

# text = "m\t\te\t\ti\tn"
# result=text.expandtabs(2)
# print(result)
# a,b=5,1
# if a<b:
#     print("a small b")
# elif a==b:
#     print("a equals b")
# else:
#     print("a big b")
# leftshift
# x=16
# x <<=2
# print(x)
# x=7
# x |= 3
# print(x)
# walrus atama
# x=7
# print(x:=19)

psw = 12345
myPsw = int(input("enter psw :"))
if psw == myPsw:
    print("succesful")
else:
    print("wrong")
