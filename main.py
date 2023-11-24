#Greeting the user and displaying optionss
def mainPage():
    print("Hello, choose an option:")
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tab")
    print("6. Sort All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")

#Choice 1
def addANewTab():
    Title=input("Please enter the title: ")
    URL=input("Please enter the URL: ")


if __name__ == '__main__':
    while True:
        mainPage()
        choice = int(input("Input your choice: "))
        if choice==1:
            addANewTab()
        # if choice==2:
        # if choice==3:
        # if choice==4:
        # if choice==5:
        # if choice==6:
        # if choice==7:
        # if choice==8:
        # if choice==9:





