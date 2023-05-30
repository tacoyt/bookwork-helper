#defining the things
bookworkcodelist = []

answerlist = []

codefetch = 0

tempinputstore = ""

def start():
    print("Welcome to the Sparx Bookwork Code helper")
    print("its a disgrace to society but we have to do it. So here we are.")
    print("----------------\n")
    
    getanswers()

def getanswers():
    tempinputstore = input('Enter the bookwork code. Capitalise the Letter. ')
    bookworkcodelist.append(tempinputstore)

    tempinputstore = input('Enter the answer for the bookwork code. ')
    answerlist.append(tempinputstore)

    answersmenu()

def answersmenu():
    tempinputstore = input('Enter "1" to continue adding answers or "2" to fetch a bookwork code. ')
    if tempinputstore == '1':
        getanswers()
    elif tempinputstore == '2':
        fetchcodes()
    else:
        print('Not a valid input. Try again.')

    answersmenu()

def fetchcodes():
    tempinputstore = input('Enter the bookwork code you want to fetch. ')
    if tempinputstore in bookworkcodelist:
        codefetch = bookworkcodelist.index(tempinputstore)
        print("\n" + answerlist[codefetch], "is your answer")

        fetchcodesmenu()
        
    elif tempinputstore not in bookworkcodelist:
        print('Entered code in not in database. Check capitalisation or check entered bookwork code. ')
        fetchcodes()

def fetchcodesmenu():
    tempinputstore = input('Enter "1" to return to entering answers or "2" to exit program. ')
    if tempinputstore == '1':
        getanswers()
    elif tempinputstore == '2':
        exit()
    else:
        print('Pay attention.', tempinputstore, 'was not in the options. Wakey wakey! ')
        fetchcodesmenu()

start()