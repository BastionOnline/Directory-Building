from modules.customizeDate import customizeDate
from modules.dirCreation import dirCreation
from modules.excelCreator import excelCreator

def automation(DestDir, SourceDir, FileName, Files, year, response, self):
    #Automation
    # Date and ranges created
    countdot, PeriodStart, TotalWeeks = customizeDate(year)

    # Create files and configure them
    numbermonths, YearDir = dirCreation(DestDir, year, Files, SourceDir, response, self)

    # Makes Custom dates on file copies
    excelCreator(numbermonths, FileName, YearDir, countdot, SourceDir, Files, PeriodStart, TotalWeeks, self)