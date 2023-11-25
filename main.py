import requests
import json
Tabs=[]
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
    while True:
        #check if input is empty
        if i == "":
            Tabs.pop()
            break
        #check if input is valid
        elif 0 <= int(i) <= len(Tabs):
            Tabs.pop(int(i))
            break
        else:
            print("Invalid input.")
            i=input("Input a valid index to close: ")

#choice 3:
def switchTabs(Tabs):
    i = int(input("Input the index of the tab you wish to open: "))
    req=requests.get(Tabs[i]['URL'])
    #checking the success of the request
    if req.status_code==200:
        print(req.text)
    else:
        print("Not available URL")

#choice 4::
def printTitles(Tabs):
    for tab in Tabs:
        print(tab['Title'])
        if len(tab['nestedTabs'])!=0:
            for i in tab['nestedTabs']:
                print("\t"+i['Title'])

#Creating nested tabs
def createNestedTabs(Tabs):
    i=int(input("The index of the parent tab where the nested tab is created: "))
    Tabs[i]['nestedTabs']['Title']=input("Please enter the title of nested tab: ")
    Tabs[i]['nestedTabs']['Content'] = input("Please enter the content of nested tab: ")

#choice 6(sorting tabs according to titles
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

def sortNestedTabs(Tabs):
    for tab in Tabs:
        if len(tab['nestedTabs'])>1:
            sortTabs(tab['nestedTabs'])

#Saving tabs
def saveTabs(Tabs):
    #taking file path from user
    filePath=input("Enter the file path: ")

    #openning file
    file=open(filePath,'w')

    #saving tabs in file
    json.dump(Tabs, file)

def loadTabs():
    loadedTabs=[]
    #taking file path from user
    filePath=input("Enter the file path:")

    #openning file
    file = open(filePath, 'r')

    #loading tabs from file
    loadedTabs=json.load(file)

    printTitles(loadedTabs)

if __name__ == '__main__':
    while True:
        mainPage()
        choice = int(input("Input your choice: "))
        if choice==1:
            addANewTab(Tabs)
        if choice==2:
            closeTab(Tabs)
        if choice==3:
            switchTabs(Tabs)
        if choice==4:
            printTitles(Tabs)
        if choice==5:
            createNestedTabs(Tabs)
        if choice==6:
            sortTabs(Tabs)
            sortNestedTabs(Tabs)
        if choice==7:
            saveTabs(Tabs)
        if choice==8:
            loadTabs()
        if choice==9:
            print("Program closed")
            break
        print(Tabs)




