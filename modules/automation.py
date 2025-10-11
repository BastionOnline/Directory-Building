from modules.dateCalculation import customizeDate
from modules.createDirectory import dirCreation
from modules.scheduleBuilder import excelCreator

# DestDir=api.destinationFolderPath
# SourceDir=api.sourceDir
# FileName=api.nameSolo
# Files=api.nameExcel
# year=api.yearValue
# response=api.customizeDateBool



def automation(DestDir, SourceDir, FileName, Files, year, response, self):
    #Automation
    # Date and ranges created
    countdot, PeriodStart, TotalWeeks = customizeDate(year)

    # Create files and configure them
    numbermonths, YearDir = dirCreation(DestDir, year, Files, SourceDir, response, self)

    # Makes Custom dates on file copies
    excelCreator(numbermonths, FileName, YearDir, countdot, SourceDir, Files, PeriodStart, TotalWeeks)