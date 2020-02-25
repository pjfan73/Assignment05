#------------------------------------------#
# Title: CDInventory.py
# Desc: Script CDINventory to read, display, delete and store CD Inventory data
# Change Log: (Who, When, What)
# jstevens, 2020-Feb-19, Started Edits on existing File
# jstevens, 2020-Feb-24, Finished edits to File
#------------------------------------------#

# Declare variabls
strChoice = '' # User input
lstTbl = []  # list of dicts to hold CD list
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
dicRowload = {} # Dict that builds each CD for loaded file
dicRowadd = {} #Dict that builds user input into new CD
loadFlag = 0 # flag to check for loading the existing CD File
saveFlag = 0 # flag that checks for unsaved CDs before exiting
# Get user Input
print('The Magic CD Inventory\n')
while True:
    # Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
    if strChoice == 'x':# Exits Script after checking for unsaved added CD's, Gives User choice to exit without saving
        if saveFlag == 1:
            userexit = (input ("You have not saved the list yet,\nto exit without saving type 'exit'\nor press enter to continue "))
            if userexit.lower() == 'exit':
                print('Goodbye!')
                quit()
            else:
                print("Please Save your List!")
                print()
        else:
            print('Goodbye!')
            quit()
    if strChoice == 'l': #Loads existing List of CD from File CDInventory.txt, prevents the same list from being loaded twice.
        if loadFlag == 1:
            print('You already loaded this list!')
            print()
        else:
            objFile = open(strFileName, 'r')
            for row in objFile:
                lstRow = row.strip().split(',')
                dicRowload = {'id': int(lstRow[0]), 'Title': lstRow[1], 'Artist': lstRow[2]}
                lstTbl.append(dicRowload)
            objFile.close()
            loadFlag = 1
            print('The File Named ' + strFileName + ' was loaded.')
            print()
    elif strChoice == 'a':  #Add CD and append to CD list
        strId = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strId)
        dicRowadd = {'id':intID, 'Title':strTitle, 'Artist':strArtist}
        lstTbl.append(dicRowadd)
        saveFlag = 1
        print("You added: ")
        print("{0:<5}{1:<30}{2:30}".format('ID','CD Title', 'Artist'))
        print("{0:<5}{1:<30}{2:30}".format(*dicRowadd.values(), sep = ', '))
        print()
    elif strChoice == 'i':# Show list of CDs that have been loaded and added
        print("{0:<5}{1:<30}{2:30}".format('ID','CD Title', 'Artist'))
        for row in lstTbl:
            print("{0:<5}{1:<30}{2:30}".format(*row.values(), sep = ', '))
        print()
    elif strChoice == 'd': #Allow the deletion of a CD by id
        print("{0:<5}{1:<30}{2:30}".format('ID','CD Title', 'Artist'))
        for row in lstTbl:
            print("{0:<5}{1:<30}{2:30}".format(*row.values(), sep = ', '))
        delId = int(input("Please choose which CD you want to delete, Enter the ID Number:"))
        lstTbl = [cd for cd in lstTbl if not (cd['id'] == delId)]# list comprehension to build lstTbl without the removed CD
        saveFlag = 1
        print ('CD Deleted') 
        print()
    elif strChoice == 's':# Save the List to CDInventory.txt. If list has not been loaded then append the list else overwrite the list
        if loadFlag == 0: 
            objFile = open(strFileName, 'a')
            for row in lstTbl:
                strRow = ''
                for item in row.values():
                    strRow += str(item) + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)
            objFile.close()
            saveFlag = 0
        else: 
            objFile = open(strFileName, 'w')
            for row in lstTbl:
                strRow = ''
                for item in row.values():
                    strRow += str(item) + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)
            objFile.close()
            saveFlag = 0
    else:
        print('Please choose either l, a, i, d, s or x!')

