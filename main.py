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
        if len(tab['nested_tabs'])!=0:
            for i in tab['nested_tabs']:
                print("\t"+i['Title'])

def createNestedLoops(Tabs):
    i=int(input("The index of the parent tab where the nested tab is created: "))
    addANewTab(Tabs[i]['nested_tabs'])

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
            createNestedLoops(Tabs)
        if choice==6:
            sortTabs(Tabs)
        # if choice==7:
        # if choice==8:
        # if choice==9:
        print(Tabs)




