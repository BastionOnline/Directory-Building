import os
import shutil

def initTemplate(self, templateFolderDir):
    fileGrouping = []
    # check if templates exist in current directory, if not, make one

    # check if files exist via json
    
    # make templates folder and copy files there
    fileGrouping.append([["Balance"], ["Balance.xlsx"], ["1. Balance.xlsx"], [self.balanceFilePath]])
    fileGrouping.append([["Schedules"], ["Schedules.xlsx"], ["2. Schedules.xlsx"], [self.scheduleFilePath]])
    fileGrouping.append([["Sales"], ["Sales.xlsx"], ["3. Sales.xlsx"], [self.salesFilePath]])
    fileGrouping.append([["Invoices"], ["Invoices.xlsx"], ["4. Invoices.xlsx"], [self.invoiceFilePath]])
    fileGrouping.append([["Hotel - Schedule"], ["Hotel - Schedule.xlsx"], ["5. Hotel - Schedule.xlsx"], [self.hotelFilePath]])


    # do file check against dirs

    for file in fileGrouping:
        print(file[2][0])

        templateFilePath = os.path.join(templateFolderDir, file[2][0])
        print(templateFilePath)
        if os.path.exists(templateFilePath) == True:
            # move to draft folder and date it
            print(f"{file[2][0]} exists")
        else:
            print(f"copy {file[2][0]}")
            shutil.copyfile(file[3][0], templateFilePath)
    
    print("finished")

    nameNumberedExcel = []
    nameExcel = []
    nameSolo = []

    for file in fileGrouping:
        print(file[1][0])
        nameExcel.append(file[1][0])
        nameSolo.append(file[0][0])
        nameNumberedExcel.append(file[2][0])

    print(nameSolo)

    return templateFolderDir, fileGrouping, nameExcel, nameSolo, nameNumberedExcel