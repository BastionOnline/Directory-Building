import os

def userIntro(MissingName, PresentName, Files, DestDir):
    print("\nThis is a directory building program.")
    print("If you want to stop this program, type stop or exit, or press 'CTRL' + 'C' at any time\n")

    if len(MissingName) == 0:
        
        for Templates in Files:
            print(Templates + " is ready to copy.")
        
        print("\nAll files needed to build this directory are present.\n")

    else:
        
        if len(PresentName) == 0:
            print("\n*** NO FILES ARE IN " + os.getcwd() + " ***\n")
        else:
            print("The following are present:")
            for Templates in PresentName:
                print(Templates)

        print("\nThe following are NOT present in this folder and WILL NOT be created in the directory:")

        for Missing in MissingName:
            print(Missing)

        print("\nPlease place these missing files in " + os.getcwd())

    # print("The current directory is:\n" + os.getcwd() + "\n")
    print("\nThe Destination Directory is:\n" + DestDir + "\n\n")
    # print("Please make sure the following files are in this folder:")

    # f = 0
    # while f <= 3:
    #     print(Files[f] + "\n")
    #     f +=1
        
