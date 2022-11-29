import sys

names = ["Zoran", "Moeko", "Ljubisa", "Jovana", "Pavle"]


def getName():
    try:
        inputName = input("Enter search name:  ")
        if len(inputName) > 0:
            return inputName

        else:
            print("Check your input name.")
    except Exception:
        print(f"Check your input:{Exception} ")


def checkList(nameToCheck):
    if nameToCheck in names:
        print(
            f"{nameToCheck} name is found in the list at index: {names.index(nameToCheck)}")
    else:
        print(
            f"{nameToCheck} has not been found in the list.")


def getAndCheckName():
    nameInput = getName()
    checkList(nameInput)


getAndCheckName()
