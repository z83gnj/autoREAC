####################################################################
# Created by: Akos Matiny TDRHS4                                   #
#             akos.matiny@zf.com                                   #
# Desription:                                                      #
#    This script summarizes the rection forces for the evaulating  #
#    of e.g. the bearing forces.                                   #
#    Plese run the script in the dierctory wich contains           #
#    the hwascii files.                                            #
# Required additional module:                                      #
#    xlsxwriter --> for export data to excel                       #
# To install module use:                                           #
#       pip install xlsxwriter                                     #
####################################################################
import os
import xlsxwriter

def CheckExcelFile():
    try:
        with xlsxwriter.Workbook('CTCT_Forces.xlsx') as workbook:
            return True
    except xlsxwriter.exceptions.FileCreateError:
        return False

# Export to excel with xlsxwriter
def WriteToExcel (AllResults, FileNames, nrOfFile):
    with xlsxwriter.Workbook('CTCT_Forces.xlsx') as workbook:
        for i in range(nrOfFile):
            SheetName = FileNames[i][:-5]
            if len(SheetName) > 31:
                tempName = SheetName[:27] + ("_%.3d" % (i+1))
                print(SheetName,' is renamed to ',tempName)
                SheetName = tempName
            worksheet = workbook.add_worksheet(SheetName)
            worksheet.write('A1', 'File name:' )
            #worksheet.merge_range('B1:F1', FileNames[i])
            worksheet.write('A2', FileNames[i] )
            worksheet.write('A3','Time')
            worksheet.write('B3', 'F_x')
            worksheet.write('C3', 'F_y')
            worksheet.write('D3', 'F_z')
            for row_num, data in enumerate(AllResults[i]):
                worksheet.write_row(row_num+3, 0, data)
    print('CTCT_Forces.xlsx',' has been written!')    

def main():
    # Get the current working directory
    cwd = os.getcwd()

# Print the current working directory
    print("Current working directory: {0}".format(cwd))
    
    if not CheckExcelFile():
        print("Unable to open the Damage.xlsx file!!!\nCheck the permmission or the closed state! ")
        input("Press Enter to continue...")
        return -1
    
    # Collecting the hwascii file in the folder
    ListofFiles = []
    
    Results = []

    for x in os.listdir():
        if x.endswith(".post"):
            # Add only the post files to the list
            ListofFiles.append(x)
    # If there are not hwascci files the script end
    if not ListofFiles:
        print("No .post file in directory")
        input("Press Enter to continue...")
        return 0

    
    # Open the files
    #Nrfiles = 0

    for ResFile in ListofFiles:                
        with open(ResFile) as f:
            results =[]
            time, fx, fy, fz = 0, 0, 0, 0
            step = 0
            print(ResFile,'is opened')
            '''
            for i in range(22):
                next(f) # Skip the headers up to $DATA line
            '''
            temp=0
            row=f.readline()
            while (row.split()[0] != "$DATA"):
                #print(temp, " " , row)
                #next(f) # Skip the headers up to $DATA line
                row=f.readline()
                temp +=1
            
            next(f) # skip the $DATA line
            print("Skipped", temp+1, "header row(s)!")
            isREAC=True
            for line in f.readlines():
                # Collect the force in all direction
                 
                if (line[0] != '!' and line[0] != '$'and line[0] != '&') and isREAC:
                    fields = line.split()
                  #  print(line.split()[2])
                    fx += float(fields[1])
                    fy += float(fields[2])
                    fz += float(fields[3])
                    
                elif (len(line.split()) > 1 and line.split()[1] == "TIME"):
                    #print("istime")
                    time = float(line.split()[3])
                elif (line[0] == "$" and line.split()[0] != "$END"):
                    results.append([time, fx, fy, fz])
                    step +=1
                elif (line.split()[0] == "$END"):
                    results.append([time, fx, fy, fz])
                    break
            
            #print(results)
            Results.append(results)

    # Write node - damage to excel file
    WriteToExcel(Results, ListofFiles, len(ListofFiles))
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()

