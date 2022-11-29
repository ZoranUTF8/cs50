def printHashes():
    while True:
        try:
            n = int(input("How many hashes do you want to print: "))
            for i in range(n):
                print("#")

            break
        except Exception:
            print("Only integers are allowed")


# printHashes()

#! We can add the end to the prin
for i in range(3):
    for j in range(3):
        print("#", end="")
    print("")

'''
###
###
###
'''
