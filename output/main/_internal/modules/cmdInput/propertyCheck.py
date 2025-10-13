import os

##########################################################################################################################
# THIS CHECKS FILE PROPERTIES

def propertyCheck(Files, SourceDir):
    # FSizes = []
    PresentName = []
    PresentSize = []
    PresentDate = []
    MissingName = []

    def Attributes():
        
        f = 0

        for f in range(len(Files)):

            filecheck = os.path.exists(SourceDir + Files[f])

            if filecheck == False:
                MissingName.append(Files[f])
                # print(Files[f] + " was not found")
                f +=1

            else:
                # print(Files[f] + " located")
                PresentName.append(Files[f])
                PresentSize.append(os.path.getsize(Files[f]))
                PresentDate.append(os.path.getctime(Files[f]))
                # FSizes.append(SourceDir + Files[f])
                f +=1

        # print(len(PresentName))

    Attributes()

    return PresentName, PresentSize, PresentDate, MissingName