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

# psw = 12345
# myPsw = int(input("enter psw :"))
# if psw == myPsw:
#     print("succesful")
# else:
#     print("wrong")
# list=> sıralı,degişebilir.yilenelebilir
# tuple => sıralı,degişmez, yinelenebılır
# set=> sıralı degıl, degiştirilmez, yinlenemez
# dictanıtory=> sıralanabılır, degişebilir, yenılenemez
# append=> lsitenın sonuna item ekler
# car = ["bmw","merc"]
# car.append("volvo")
# print(car)
# insert=> belirli yere ekler
# car.insert(1,"skoda")
# print(car)
# extend=> başka bir listeyi ekler, tupple dict set de eklenir
# copy=>list=> ile abagımsız ve aynı liste oluşturur
# remove=>pop=>(geriye dondurur sonra atar) listeden veriyi kadlırır ()=> itemin adını yaz ilkini sıler aynı varsa
# del list[index] listeden oge siler
# clear=> lissteyi boşaltır
# index()=> itemin indexini dondurur
# sort=>(key=str.lower=> b.k duyarlılı kalkar) afabetik ve b.kücüge sıralar
# sort(reverse=true)=> b.kcuge zdena ya sıralar
# sort(key=mysort(abs(x-20)))=> 20 ye yakınlık derecesıne gore sıralar
# enumrate()=> key value gibi listeler

# myNumbers = []
# i=0
# while(i<8):
#     number = int(input("Enter a integer"))
#     myNumbers.append(number)
#     i+=1
# print(myNumbers)

# randomNum = random.randint(1,100)
# i=0
# print("--- Number Guessing Game ---")
# while (i<10):
#     userNumber = int(input("The number you guessed ="))
#     if randomNum < userNumber:
#         print("Guess the smaller number")
#     elif randomNum > userNumber:
#         print("Guess the larger number")
#     else:
#         print("Conguralations u got it right")
#     i+=1
# print(randomNum)

# finding prime number

# inputNumber = int(input("Enter a number"))
# flag = True
# if(inputNumber<0):
#     print("pls enter a positive number")
# for i in range(2,int(inputNumber**0.5)+1):
#     if(inputNumber %i ==0):
#         flag=False
#         break
# if(flag):
#     print("number a prime")
# else:
#     print("number a not prime")

# inputNumber = int(input("Enter a number"))
# primeNumbers = []
# primeNumbers.append(2)
# flag = True
# if(inputNumber<0):
#     print("pls enter a positive number")
# for i in range(3,inputNumber+1,2):
#     for j in range(3,int(i**0.5)+1):
#         if(i %j ==0):
#             break
#     else:
#             primeNumbers.append(i)
# print(primeNumbers)
# OBEB OKEK
# list comprehension()=>
# fruits = ["orange","strawberry","watermelon","cheery","grape"]
# [print(item) for item in fruits]
# newList= [item.upper() for item in fruits if("g" in item)]
# print(newList)

# def myName(**kwargs):
#     print("his last name is "+kwargs["lastname"])
# myName(firstname="mehmet",lastname="delibas")

# default içerdeli parameterın degerını atar
# def myLastName(lastname="Delibas"):
#     print("My Last Name :"+lastname)
# myLastName()

# def numbersWord(number):
#     ones = ["","bir","iki","üc","dort","bes","alti","yedi","sekiz","dokuz"]
#     tens = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
#     if not 1000<=number <= 9999:
#         return "please enter a 4-digit number"
    
#     oneDigit = number %10
#     tenDigit = (number // 10) %10
#     hunderedDigit = (number//100) %10
#     thousandDigit = number // 1000
#     resultt = ""

#     if thousandDigit>0:
#         if thousandDigit>1:
#             resultt+=f"{ones[thousandDigit]} bin "
#         else:
#             resultt+= "bin "
#     if hunderedDigit>0:
#         if hunderedDigit>1:
#             resultt+=f"{ones[hunderedDigit]} yüz "
#         else:
#             resultt+= "yüz "
#     if tenDigit>0:
#         resultt+= f"{tens[tenDigit]}"+" "
#     if oneDigit>0:
#         resultt+= f"{ones[oneDigit]}"
    
#     return resultt.strip()

# number = int(input("Enter a 4-digit number"))
# print(numbersWord(number))

# def repeatFunc(string,num):
#     for item in range(num):
#         print(f"sunu yolladın {string}")

# repeatFunc("Mehmet",6)

# def areaAndRnvironment(leng,weight):
#     print("area :",leng*weight)
#     print("enviorement :", 2*(leng+weight))

# areaAndRnvironment(5,3)

# oran = random.randrange(0,2)
# print(oran)
# for item in 

# open("log.txt","")
# OOP()=> object oriatned programing

# class Person:
#     def __init__(self,n,a):
#         self.name = n
#         self.age = a
#     def myInfo(self):
#         print(f"my name {self.name}, my age : {self.age}")

# class IdariPersonel(Person):
#     pass
# class AkademikPersonel(Person):
#     pass
# class Student(Person):
#     def __init__(self, n, a,year):
#         super().__init__(n, a)
#         self.graudetinory = year
#     def welcome(self):
#         print("Welcomeee")


# p1 = Student("Mehmet",23,2027)
# p1.myInfo()
# print(p1.graudetinory)
# print(p1.name)
# p1.welcome()
# METHOD overriding

# class Animal:
#     def speak(self):
#         return "Sound"
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
# class Dog(Animal):
#     def speak(self):
#         return "Hav Hav"
    
# dog=Dog()
# cat=Cat()
# print(dog.speak())
# print(cat.speak())
# print(isinstance(dog,Animal))

# class BankACcount:
#     def __init__(self,number,balance):
#         self.accountNumber=number
#         self.__balance=balance

#     def deposit(self,amount):
#         if(amount>0):
#             self.__balance+=amount
#             return f"Deposited : {amount} New balance : {self.__balance}"
#         return "Invalid deposit"
#     def __display_balance(self):
#         return f"Balance :{self.__balance}"
#     def get_balance(self):
#         return self.__display_balance()
    
# account = BankACcount("321321",200)
# print(account.get_balance())
# Abstract class

# from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimetre(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
    
#     def area(self):
#         return self.width*self.height
#     def perimetre(self):
#         return 2*(self.width+self.height)
    
# rect =Rectangle(4,7)
# print(rect.area())
# print(rect.perimetre())

# class Vehicle:
#     def move(self):
#         return "This vehicle moves"
# class Car(Vehicle):
#     def move(self):
#         return "The car drives on the road"
# class Boat(Vehicle):
#     def move(self):
#         return "The boat sails on water"
# class Airplane(Vehicle):
#     def move(self):
#         return "The airplane fliees in the sky"
# class Bcylyce(Vehicle):
#     pass

# vehicles = [Car(),Bcylyce(),Airplane(),Boat()]
# for item in vehicles:
#     print(item.move())

# class Employes:
#     def __init__(self,name,emp_id):
#         self.name=name
#         self.emp_id=emp_id
# class Department:
#     def __init__(self,name_dp):
#         self.name_dp=name_dp
#         self.employees=[]

#     def add_employee(self,employe):
#         self.employees.append(employe)

#     def show_department(self):
#         print(f"Department : {self.name_dp}")
#         for item in self.employees:
#             print(f"Employees : {item.name}, ID:{item.emp_id}")

# e1=Employes("mehmet metin",23)
# e2=Employes("eren türkoglu",21)

# dept=Department("software development")

# dept.add_employee(e1)
# dept.add_employee(e2)
# dept.show_department()

# class Student:
#     def __init__(self, name):
#         self.name = name
# class School:
#     def __init__(self, name):
#         self.name = name
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)
# s1 = Student("Ahmet")
# s2 = Student("Ayşe")

# my_school = School("Anadolu Lisesi")
# my_school.add_student(s1)
# my_school.add_student(s2)

# for item in range(0,2):
#     print(my_school.students[item].name)

# # File Handling

# with open("fileTest/demo.txt","r",encoding="utf-8") as f:
#     print(f.read())
# print(f.closed)
# f.close()
# import os

# os.mkdir("C:\\Users\\Mertcan\Masaüstü\\PythonLearn\\basicTerms\\newFolders")
# os.rmdir("newFolders")
# print(os.listdir())
# fruits=["grape\n","strawberry\n","banana\n"]
# with open("fileTest/newFile.txt","a+",encoding="utf-8") as f:
#     f.writelines(fruits)
#     f.flush()
