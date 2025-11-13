import os
import openpyxl

#This formats excel sales
def xlSales(inputdir, file, MY, FirstDay):

    print(f"starting ${file} config\n\n")
    print(f"inputdirectory:\n ${inputdir}")

    inputfile = os.path.join(inputdir, file)
    outputfile = os.path.join(inputdir, file)

    print("\nUpdating excel Sales file to " + MY + "...")

    workbook = openpyxl.load_workbook(inputfile)

    sheet = workbook['Yearly Calendar']
    cell = sheet['B2']
    cell.value = FirstDay

    workbook.save(outputfile)
    print("Sales file updated to " + MY + " and saved to\n" + outputfile)


