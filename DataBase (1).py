#my imports of the os and mmap
import os
import mmap
import decimal

#Makin a class !
class UserDataBase:

    #Dis is my constructor!! there are many like it but this one is mine!!
    #My constructor is my best friend it is my life. I must master it as I must
    #master my life. With out me my constructor is usless with out my constructor
    #I am useless. I must program my constructor true I must program it better
    #than i have ever before or bugs will kill it. I must fix the bug before it kills me
    #I will before god i sware this creed my constructor and myself are the savors of this program
    #we are the masters of it. we are the fixers of them all. so be it untill theres no bugs
    #but working program! (Full metal jacket spin off ohhhh yaaaaaa)
    def __init__(self):
        self.userNames = [] #Holds names of users
        self.userPasswords = [] #Holds Passwords of users
        self.filesAdded = 0 #Holds the value of files added from all people
        self.userAddedFiles = [] #Holds users that added the files number
        self.nameOfFiles = [] #Holds the names of the files that the users have added

        decimal.getcontext().prec = 28

        print("          == say HelpDesk() for help on how to use ==")
        print("== Dont actually say it....this isn't magic type it in ya nitwit ==")
        return

##################################################################################
    #To show the user how to use the software
    def HelpDesk(self):
        print("MakeAccount('name', 'password'): it's in the name but if you have to know it makes an account")
        print("RemoveAccount('name'): again in the name but it removes the account")
        print("LogInAccount('password'): well ding ding ding you got it logs you in!")
        print("The more you know!")


##################################################################################

    #For making accounts to add Users also checks if the names are already taken
    #to prevent mess up's from going into other people's accounts becuase
    #that would be awkward if that happend
    def MakeAccount(self, name, password):
        #Checks the length of the variable userNames and sees if it's greater than
        #'0'
        if len(self.userNames) > 0:
            for x in range(0, len(self.userNames)):
                #Making sure nothing is taken by the other users...so if it is just
                #put 'x' in front of it or a number at the end
                if name != self.userNames[x] and password != self.userPasswords[x]:
                    self.userNames.append(name)
                    self.userPasswords.append(password)
                    self.userAddedFiles.append(0)
                    print(name + " added to the data base of fun")
                else:
                    print(name + " or " + password + " taken")
        else:
            self.userNames.append(name)
            self.userPasswords.append(password)
            self.userAddedFiles.append(0)
            print(name + " added to the data base of fun")
        return

##################################################################################

    #Removing users on the dataBase becuase you don't want them there !
    def RemoveAccount(self, name):
        #Scans the list of usersNames
        for x in range(0, len(self.userNames)):
            #Checks to see if the name you put down maches anything in the
            #database
            if name == self.userNames[x]:
                self.userNames.pop(x)
                self.userPasswords.pop(x)
                print(name + " Has been removed BYE BYE!!!")
            else:
                print("No one by " + name + " is on here")
        return

##################################################################################

    #Logging into the account
    def LogInAccount(self, password):
        logIn = False
        count = 0
        for x in range(0, len(self.userPasswords)):
            if password == self.userPasswords[x]:
                count = x
                logIn = True

        if logIn == True:
            while logIn == True:
                #Display of a interactive user interface by using the
                #number system or you can write it out this will also
                #display your name at the top becuase that's cool
                print(" == Welcome " + self.userNames[count] + " ==")
                print("1) Add File")
                if self.filesAdded > 0:
                    print("2) Remove File")
                else:
                    print("2) Remove File can't be done becuase no files added")
                print("3) Open File (" + str(self.filesAdded) + ")")
                print("4) Users On Data Base")
                print("5) Log Out")
                choice = input("> ")

                #Logging out of the system becuase you gave me an A+ and you are
                #amazed
                if choice == str(5):
                    logIn = False

                #Addig a file to the system and you can write to the file if you want
                elif choice == str(1) or choice == "Add File":
                    nameOfFile = input("File Name: ")

                    #Adds the name of the file to the records
                    self.nameOfFiles.append(nameOfFile)

                    #Checking to see if there is a '.txt' in the name of the
                    #file to prevent mess ups and error and it's just bad....like really bad
                    #1/10 would not recommend
                    if ".txt" in nameOfFile:
                        file = open(nameOfFile, "w")
                    else:
                        file = open(nameOfFile + ".txt", "w")

                    #Adding to the text file what ever you want just nothing weird
                    text = input("Enter Text here >")
                    file.write(text)
                    file.close()

                    #incrementing files that have been added and the files that have
                    #been personally added
                    self.filesAdded = self.filesAdded + 1
                    self.userAddedFiles[count] = self.userAddedFiles[count] + 1

                #Removing the file from the system becuase you don't want it there

                if choice == str(2) or choice == "Remove File":
                    if self.filesAdded > 0:
                        #Display list of files that have been added by users
                        if len(self.nameOfFiles) > 0:
                            for y in range(0, len(self.nameOfFiles)):
                                print(str(y + 1) + ") " + self.nameOfFiles[y])

                            nameOfFile = input("File Name: ")

                            #Checks to see if its a digit or not if not then make sure that
                            #there is a '.txt' then remove it from the list
                            if nameOfFile.isdigit():
                                os.remove(self.nameOfFiles[y - 1] + ".txt")
                                self.nameOfFiles.pop(y - 1)
                            else:
                                if ".txt" in nameOfFile:
                                    os.remove(nameOfFile)
                                else:
                                    os.remove(nameOfFile + ".txt")
                                    self.nameOfFiles.pop(y - 1)



                            #Subtract from the files that have been added and subtract the files
                            #that the user personally added
                            self.filesAdded = self.filesAdded - 1
                            self.userAddedFiles[x] = self.userAddedFiles[x] - 1
                        else:
                            print(" == No files Added == (nice try ;))")

                #Open a file from the system and prints it out on the screen and
                #waits for an exit key also finds words that are in the File
                #and prints the ammount of them on the screen
                elif choice == str(3) or choice == "Open File":
                    if self.filesAdded > 0:
                        stillInFile = False

                        #Displays the files
                        if len(self.nameOfFiles) > 0:
                            for z in range(0, len(self.nameOfFiles)):
                                print(str(z + 1) + ") " + self.nameOfFiles[z])

                        nameOfFile = input("File: ")

                        #Check to see if the user input a number or a text if and check to see
                        # if '.txt' is at the end of the file name so
                        #it can open it becuase that's the main thing....come on
                        try:
                            nameOfFile = int(nameOfFile) - 1
                            file = open(self.nameOfFiles[nameOfFile] + ".txt", 'r')
                        except ValueError:
                            if ".txt" in nameOfFile:
                                file = open(nameOfFile, "r")
                            else:
                                file = open(nameOfFile + ".txt", "r")

                        contents = file.read()  #Store the contents of text in 'contents'
                        print(contents) #Print it to the screen
                        comeOut = False #Set the loop

                        #This is a loop to say in the file viewer to either find a words
                        #or to read it whatever you prefer
                        while comeOut == False:
                            print("(1) Exit  (2) Find Word (3) Compaire")
                            exitTime = input("> ")

                            #Will exit out of the loop and will go back to the mane
                            #interface
                            if exitTime == str(1) or exitTime == "Exit":
                                file.close()
                                comeOut = True

                            #Will find the word you inputted and count how many Times
                            #it appers in the text file
                            elif exitTime == str(2) or exitTime == "Find Word":
                                wordRepeted = 0 #Stores repeated words
                                word = input("Word: ")
                                for w in contents.split():
                                    if word == w:
                                        wordRepeted = wordRepeted + 1
                                print(word + " " + str(wordRepeted) + " Times")

                            #This would comapre another document and see the similaritys
                            elif exitTime == str(3) or exitTime == "Compaire":
                                if self.filesAdded > 1:
                                    similarity = 0.0 #percent of similairty
                                    repition = 0 #Count similar words

                                    for t in range(0, len(self.nameOfFiles)):
                                        print(str(t + 1) + " " + self.nameOfFiles[t])

                                    secondFileChooser = input("Second File: ")

                                    #This will try to make the input a integer if it doesn't
                                    #succeed then it will go to the string value then check to
                                    #see if there is a '.txt' then open the file as a readOnly
                                    try:
                                        secondFileChooser = int(secondFileChooser) - 1
                                        secondFile = open(self.nameOfFiles[secondFileChooser] + ".txt", "r")
                                    except ValueError:
                                        if ".txt" in secondFileChooser:
                                            secondFile = open(secondFileChooser + ".txt", "r")
                                        else:
                                            secondFile = open(secondFileChooser, "r")


                                    secondFileContents = secondFile.read()
                                    secondFileContents = secondFileContents.split()
                                    contents = contents.split()

                                    for v in range(0, min(len(contents), len(secondFileContents))):
                                        if contents[v] == secondFileContents[v]:
                                            repition += 1

                                    if repition > 0:
                                        similarity = (float(repition)/float(max(len(contents), \
                                            len(secondFileContents)))) * 100.0
                                        print(str(similarity) + "% similar")
                                    else:
                                        print("Nope")


                            else:
                                print("What?")


                #Displays the users on the dataBase to see who's in on the fun!
                #Also displays how much to the file fun they contributed
                elif choice == str(4) or choice == "DataFun":
                    if len(self.userNames) > 0:
                        for number in range(0, len(self.userNames)):
                            print(str(number+1) + ") " + self.userNames[number] +
                                " Files Contributed: " + str(self.userAddedFiles[number]))
                    else:
                        print(str(x+1) + ") " + self.userNames[number] +
                            " Files Contributed: " + str(self.userAddedFiles[number]))
        else:
            print(" == Unknown User ==")
        return
