import csv


people = {
    "Zoran": "41242144512",
    "Moeko": "2145454314",
    "Pavle": "98798731023"
}


'''
def searchPhoneBook():
    personName = input("Enter name: ")

    if personName in people:
        personIndex = people[personName]
        print(f"{personName} number is: {personIndex}")
    else:
        print(f"{personName} has not been found")

searchPhoneBook()
'''

# open a file
#file = open("phonebook.csv", "a")

# write a row to the csv file and close it automaticaly becouse we use it the "with"
with open("phonebook.csv", "w") as file:
    name = input("Your name: ")
    number = input("Number: ")

   # writer = csv.writer(file)
    # we can use the DictWriter(file,fieldname=["name","number"])
    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": number})
