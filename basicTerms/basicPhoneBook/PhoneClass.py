import os

class PhoneBook:
    FILE_NAME= "fileTest/phonebook.txt"
    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w", encoding="utf-8") as f:
                pass
    
    def addContact(self,fname,lname,pnumber):
        with open(self.FILE_NAME,"a",encoding="utf-8") as f:
            f.write(f"{fname},{lname},{pnumber}\n")
        print(f"{fname} {lname} has been added to the phone book")

    def listContacts(self):
        with open(self.FILE_NAME,"r",encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            print("The phone books is empty")
        else:
            print("\nPhone Book\n")
            for line in lines:
                fname,lname,pnumber=line.strip().split(",")
                print(f"{fname} {lname} - {pnumber}\n")

    def deleteContact(self,name):
        with open(self.FILE_NAME,"r",encoding="utf-8") as f:
            lines = f.readlines()
        contactFound = False
        with open(self.FILE_NAME,"w",encoding="utf-8") as f:
            for line in lines:
                fname,lname,pnumber=line.strip().split(",")
                if fname != name:
                    f.write(line)
                else:
                    contactFound = True
        if contactFound:
            print(f"Contact named {name} has been deleted from the phone book")
        else:
            print(f"No contact named {name} was found")




