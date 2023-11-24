import requests
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

#Choice 1
def addANewTab(Tabs):
    Tab={}
    Title=input("Please enter the title: ")
    URL=input("Please enter the URL: ")
    content=''
    nested_tabs=[]
    Tab['Title']=Title
    Tab['URL']=URL
    Tab['Content']=content
    Tab['nested_tabs']=nested_tabs
    Tabs.append(Tab)

#choice 2
def closeTab(Tabs):
    i=int(input("Input the index of the tab you wish to close:"))
    if i<0 or i>len(Tabs):
        Tabs.pop()
    else:
        Tabs.pop(i)

#choice 3:
def switchTabs(Tabs):

if __name__ == '__main__':
    while True:
        mainPage()
        choice = int(input("Input your choice: "))
        if choice==1:
            addANewTab(Tabs)
        if choice==2:
            closeTab(Tabs)
        print(Tabs)

        # if choice==3:
        # if choice==4:
        # if choice==5:
        # if choice==6:
        # if choice==7:
        # if choice==8:
        # if choice==9:





