from modules.fileSelect import files, folders
from modules.propCheck import propertyCheck
from modules.intro import userIntro
from modules.docCustomization import userCommand
from modules.dateCalculation import customizeDate
from modules.createDirectory import dirCreation
from modules.fileUpdate import update

FileName, FileNumber, Files, Cash_name, Sched_name, Sales_name, Invoice_name = files()
SourceDir, PrevDir, cwf, DestDir = folders()

PresentName, PresentSize, PresentDate, MissingName = propertyCheck(Files, SourceDir)

##########################################################################################################################
#Code to Exit Program

##########################################################################################################################

userIntro(MissingName, PresentName, Files, DestDir)
      
##########################################################################################################################

Userinput, year, yearpath, sourcepath, Answer, response = userCommand(DestDir, SourceDir)

##########################################################################################################################

countdot, PeriodStart, TotalWeeks = customizeDate(year)

###################################################################################################################################

numbermonths, YearDir = dirCreation(DestDir, year, Files, SourceDir, response)


#####################################################################################################################################


update(numbermonths, FileName, YearDir, countdot, SourceDir, Files, PeriodStart, TotalWeeks)
