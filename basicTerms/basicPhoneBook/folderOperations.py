import os
import json

FILE_NAME = "fileTest/peoples.json"
 
class Person:
    def __init__(self):
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME,"w",encoding="utf-8") as f:
                json.dump([],f,ensure_ascii=False,indent=4)

    def readPeople(self):
        with open(FILE_NAME,"r",encoding="utf-8") as f:
            return json.load(f)


    def savePeople(self,people):
        with open(FILE_NAME,"w",encoding="utf-8") as f:
            json.dump(people,f,ensure_ascii=False,indent=4)

    def addedPerson(self):
        name = input("Name : ")
        age = int(input("Age : ")) 
        city = input("City : ")

        newPerson = {"Name":name,"Age":age,"City":city}
        people=self.readPeople()
        people.append(newPerson)
        self.savePeople(people)
        
        print(f"{name} has been added!")

    def deletePerson(self):
        name = input("Enter the name of the person to delete : ")
        people=self.readPeople()
        updatePeople = [item for item in people if item["Name"]!= name]

        if len(people)==len(updatePeople):
            print(f"{name} not found")
        else:
            self.savePeople(updatePeople)
            print(f"{name} has been deleted!")

    def showPeople(self):
        people = self.readPeople()

        if not people:
            print("No people found")
        else:
            for item in people:
                print(f"Name:{item["Name"]},Age:{item["Age"]},City:{item["City"]} ")

class App:
    def __init__(self):
        self.manager=Person()
        
    def run(self):
        while True:
            print("\n1 - Added Person")
            print("\n2 - Delete Person")
            print("\n3 - Show All Person")
            print("\n4 - Exit")
            choice = int(input("Choose an option"))

            if choice == 1 : self.manager.addedPerson()
            elif choice == 2 : self.manager.deletePerson()
            elif choice == 3 : self.manager.showPeople()
            elif choice == 4 :
                print("Exiting...")
                break
            else:
                print("Invalid optional Please try again!")

if __name__=="__main__":
    app=App()
    app.run()