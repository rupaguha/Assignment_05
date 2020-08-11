#------------------------------------------#
# Title: CDInventory.py
# Desc: CDInventory - Creating, Appending, Reading to and Writing from Dictionaries
# Change Log: (Who, When, What)
# Srirupa Guha, 2020-Aug-09, Created File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('Write or Read file data.')
while True:
    print('\n[a] add data to list\n[w] to write data to file\n[r] to read data from file')
    print('[d] display data\n[exit] to quit')
    strChoice = input('a, w, r, d, or exit: ').lower()  # convert choice to lower case at time of input
    print('\n\n')

    if strChoice == 'exit':
        break
    if strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        
        # Add data to list in memory
        
        print("Adding to the Inventory Table")
        cd_Title = input("Enter Title:  ")
        cd_Artist = input("Enter Artist: ")
        
        dicRow = {"ID":(len(lstTbl)+1),"Title":cd_Title,"Artist":cd_Artist}
        lstTbl.append(dicRow)

        #pass
    elif strChoice == 'w':
        
        # List to File
        
        new_line = ""
        objFile = None

        for row in lstTbl:
            for item in row.values():
                new_line = new_line + str(item) + ","
            new_line = new_line[:-1] + "\n"
            
        objFile = open(strFileName, "w")    
        objFile.write(new_line)    
        objFile.close()
        print("Data saved!")
        
        #pass
    elif strChoice == 'r':
        
        # File to print
        
        lstRow = []
        dicRow = {}
        objFile = None
        
        objFile = open(strFileName, "r")
        try:
            for row in objFile:
                lstRow = row.strip().split(",")
                dicRow = {"ID":lstRow[0],"Title":lstRow[1],"Artist":lstRow[2]}
                print(dicRow)
        except:
            print("Something went wrong - maybe there is nothing to read.")
            
        objFile.close()
        
        pass
    elif strChoice == 'd':
        
        # Display data
        
        print("Displaying the Current Inventory Data\n")
        
        print("ID"+" | "+"CD Title"+" | "+"Artist")
    
        for row in lstTbl:
            print("\n")
            for item in row.values():
                print(item,end=" | ")        
        print("\n=======================================")

        #pass
    else:
        print('Please choose either a, w, r or exit!')

