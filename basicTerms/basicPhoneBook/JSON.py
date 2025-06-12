# JSON "JavaScript object notation"
import json

# dictonary
person = {"name": "Metin","age": 25,"city": "İstanbul ","hobbies":["kodlama","müzik","spor"]}

with open("fileTest/peoples","w",encoding="utf-8") as f:
    result = json.dump(person,f,ensure_ascii=False,indent=4)
    print(result)


# dosyadan okursan load() olucak
# with open("fileTest/data.json","r",encoding="utf-8") as f:

#     result = json.load(f)
#     print(f"{result["name"]}")
#     print("Hobbies :",end= " ")
#     for item in result["hobbies"]:
#         print(item,end=" ")

# jsonu stringe cevirir

