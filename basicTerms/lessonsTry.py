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

#in ile lsitenin içinde aranan kelımenın varlıgı sorgulanır
text="The best lanugage in life are free!"
search="Th"
if search in text:
    print("Yes text have")
else:
    print("No have")