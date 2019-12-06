#--------------------------------------------------------------#
# Title: Assignment 9 
# Description: Working with Modules
# ChangeLog: (Who, When, What)
# RRoot, 1.1.2030,Created started script
# RRoot, 1.1.2030,Added pseudo-code to start assignment 9
# GFlores, 12.2.20190,Modified code to complete the assignment 9
#--------------------------------------------------------------#
# TODO: Import Modules (DONE)

if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
 raise Exception("This file was not created to be imported")

# Main Body of Script-----------------------------------------#
# Data #

strFileName = "EmployeeData.txt"
lstEmployeeTable = []  # A list/table of Employee objects
lstFileData = []  # A list/table of string objects in a list

# TODO: Add Data Code to the Main body (DONE)
#  Load data from file ionto a list of employee objects when sripts starts
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
      lstEmployeeTable.append(Emp(row[0], row[1], row[2].strip()))

# Show user a menu of options
while True:
 Eio.print_menu_items()
 strOption = Eio.input_menu_options() # Get users menu option choice
 if strOption == "1":
# Show user current data in the list of employee objects
     Eio.print_current_list_items(lstEmployeeTable) 
     continue
 elif strOption == "2":
      lstEmployeeTable.append(Eio.input_employee_data()) # Lets user add data to the list of employee objects
      continue
 elif strOption == "3":
      Fp.save_data_to_file("EmployeeData.txt", lstEmployeeTable) #Lets user save current data to file
      continue
 elif strOption == "4": #Exit Program
      break
# Main Body of Script--------------------------------------------------#
