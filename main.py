import requests
import json

#Greeting the user and displaying options
def mainPage():
    print("Choose an option")
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tab")
    print("6. Sort All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")

#Adding new tab
def addANewTab(Tabs):
    Tab={}
    Tab['Title']=input("Please enter the title: ")
    Tab['URL']= "https://"+input("Please enter the url: ")
    Tab['nestedTabs']=[]
    Tabs.append(Tab)

#Closing tab
def closeTab(Tabs):
    i=input("Input the index of the tab you wish to close: ")
    # check if input is empty
    if i == "":
        Tabs.pop()
        print("Tab closed successfully")

    # check if input is valid
    elif 0 <= int(i) <= len(Tabs):
        Tabs.pop(int(i))
        print("Tab closed successfully")

    else:
        print("Invalid input.")

#Displaying parent tab content
def switchTabs(Tabs):
    i = input("Input the index of the tab you wish to open: ")
    if i=="":
        i=len(Tabs)-1

    elif int(i)<0 or int(i)>=len(Tabs):
        print("Invalid index")

    try:
        req = requests.get(Tabs[int(i)]['URL'])
        # Checking the success of the request
        if req.status_code == 200:
            print(req.text)

        else:
            print("Content can't be loaded")
            return

    except requests.RequestException:
        print("Not available URL")
        return

#Displaying titles of opened tabs
def printTitles(Tabs):
    for tab in Tabs:
        print(tab['Title'])
        if len(tab['nestedTabs'])!=0:
            for i in tab['nestedTabs']:
                print("\t"+i['Title'])

#Creating nested tabs
def createNestedTabs(Tabs):
    tab={}
    i=int(input("The index of the parent tab where the nested tab is created: "))
    #Checking the validity of the index
    if i>=0 or i<len(Tabs):
        tab['Title'] = input("Please enter the title of nested tab: ")
        tab['Content'] = input("Please enter the content of nested tab: ")
        Tabs[i]['nestedTabs'].append(tab)

        print("Nested tab added successfully")

    else:
        print("Invalid index")

#Sorting tabs according to titles
def sortTabs(Tabs):
    if len(Tabs)>1:
        mid=len(Tabs)//2
        left=Tabs[:mid]
        right=Tabs[mid:]

        sortTabs(left)
        sortTabs(right)

        i=j=k=0

        while i<len(left) and j<len(right):
            if left[i]['Title']<right[j]['Title']:
                Tabs[k]=left[i]
                i+=1

            else:
                Tabs[k]=right[j]
                j+=1

            k+=1

        while i<len(left):
            Tabs[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            Tabs[k] = right[j]
            j+=1
            k+=1

    print("Tabs sorted successfully")
    printTitles(Tabs)

#Sorting nested tabs
def sortNestedTabs(Tabs):
    for tab in Tabs:
        if len(tab['nestedTabs'])>1:
            sortTabs(tab['nestedTabs'])

#Saving tabs
def saveTabs(Tabs):
    # Taking file path from user
    filePath = input("Enter the file path: ")

    try:
        #Opening file
        file=open(filePath,'w')

        #Saving tabs in file
        json.dump(Tabs, file)

        print("Files saved successfully")

    except IOError:
        print("Error saving tabs")

#Loading tabs from file
def loadTabs(Tabs):
    loadedTabs=[]
    #Taking file path from user
    filePath=input("Enter the file path:")

    try:
        #Openning file
        file=open(filePath, 'r')

        #Loading tabs from file and adding them to Tabs list
        loadedTabs=json.load(file)
        Tabs.extend(loadedTabs)

        #Adding loaded tabs to Tabs list
        print("Tabs loaded successfully")

    except IOError:
        print("Error loading tabs")

if __name__ == '__main__':
    # Declaring list of opened tabs
    Tabs = []
    #Greeting the user
    print("Hello, welcome to my program!")
    while True:
        mainPage()

        choice = input("Input your choice(1---9): ")

        if choice=='1':
            addANewTab(Tabs)

        elif choice=='2':
            closeTab(Tabs)

        elif choice=='3':
            switchTabs(Tabs)

        elif choice=='4':
            printTitles(Tabs)

        elif choice=='5':
            createNestedTabs(Tabs)

        elif choice=='6':
            sortTabs(Tabs)
            sortNestedTabs(Tabs)

        elif choice=='7':
            saveTabs(Tabs)

        elif choice=='8':
            loadTabs(Tabs)

        elif choice=='9':
            print("Program closed")
            break

        # Check validity of choice
        else:
            print("Input is invalid.")
            continue