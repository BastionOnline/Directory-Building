import os

##########################################################################################################################
#Code to Exit Program

def userCommand(DestDir, SourceDir):
    ClosePhrase = ["stop", "exit", "close", "end"]

    def CloseProgram(Exitcmd):

        for x in ClosePhrase:
        # This loop returns a VALUE not an index, so compare directly
            if Exitcmd.lower() == x:
                # print(x.capitalize() + "ing program")
                ## exit() raise the SystemExit exception so can code this in that block
                exit()
                #sys.exit()
                #Sys.exit, EXITS IMMEDIATELY!
                    #still showed returning to code block, so will just use reg exit
            # else:
                #else statements do NOT need to be present all the time
        return Exitcmd



        # for x in ClosePhrase:

        #     if Exitcmd == ClosePhrase[x]:
        #         print(ClosePhrase[x] + "ing program")
        #         exit()
        #     else:
        #         return Exitcmd


    #     if Exitcmd == "exit":
    #         print("Exiting program")
    #         exit()
    # #        return None
    #     else:
    #         return Exitcmd

        # c = 0
        
        # while c < len(ClosePhrase):
        #     if Exitcmd.lower() == ClosePhrase[c]:
        #         print(ClosePhrase[c] + "ing program.")
        #         return None
        #     elif c == 0:
        #         c +=1
        #     else:
        #         return Exitcmd



    while True:
        try:
            Userinput = input("What year do you want to create? ")

            CloseProgram(Userinput)

            year = int(Userinput)
            yearpath = os.path.join(DestDir,"MTCC " + Userinput)
            sourcepath = os.path.join(SourceDir,"MTCC " + Userinput)
            # print(sourcepath)

            if year < 0:
                print("This is not a valid year")
            elif year < 2000:
                print("Please enter a later year")
            # elif year > 2050:
            #     print("Please enter a earlier year")
            elif os.path.exists(yearpath):
                print("Year already exists")
            else:
                break
        except ValueError:
            print("This is not a year")
        # except SystemExit:
        #     print(Userinput.capitalize() + "ing program")
        # THIS WILL CYCLE BACK LOOP
        # CAN JUST USE SYS.EXIT TO EXIT IMMEDIATELY


    while True:
        Answer = input("\nDo you want the Sales documents dates automatically set?\nThis will take a bit of additional time to complete, about 20 seconds per file, approximately 5 minutes total.\nPlease type either yes or no\n\n")
        response = Answer.lower()

        if response == "no":
            print("Sales documents dates will not be automatically set.\n")
            break
        elif response == "yes":
            print("Sales documents dates will be automatically set.\n")
            break
        else:
            print("\nPlease respond with yes or no.\n")

    # while True:
    #     year = int(input("What year do you want to create? "))
    #     if NameError(year):
    #         year = int(input("Please enter valid year"))
    #     elif ValueError(year):
    #         year = int(input("Please enter a valid year"))
    #     print("Invalid.")

        
    #month = int(input("What month do you want to start from? "))


    return Userinput, year, yearpath, sourcepath, Answer, response