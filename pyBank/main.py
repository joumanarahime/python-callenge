import os
import csv

totalMonth=0
totalNet=0
averageChange=0
dataList=[]
maxValue=0
minValue=0
maxValueDate=0
minValueDate=0
counter=1
firstRow=[]
lastRow=[]

csv_path= os.path.join("..","pyBank","pyBankBudgetData.csv")

with open(csv_path,newline='') as dataFile:
    csv_reader=csv.reader(dataFile, delimiter=',')
    csv_header= next(csv_reader)
    
        
    for row in csv_reader:
        totalMonth = totalMonth + 1
        
        totalNet = totalNet + int(row[1])

        if int(row[1])> maxValue:
            maxValue=int(row[1])
            maxValueDate=row[0]
        if int(row[1])< minValue:
            minValue=int(row[1])
            minValueDate = row[0]

        if counter == 1:
            counter=0
            firstRow= row  

        lastRow= row      
        
 
#  print header of table
    print("Financial Analysis")
    print("------------------------------")

#  The total number of months included in the dataset
    print(f"Total Months: {totalMonth}")


# The net total amount of "Profit/Losses" over the entire period
    print(f"Total Net: ${totalNet}")



# # The average of the changes in "Profit/Losses" over the entire period
    averageChange = (float(firstRow[1]) - float(lastRow[1])) / totalMonth

    print(f"Average Change: ${averageChange}")


# # The greatest increase in profits (date and amount) over the entire period
    print(f"Greatest Increase in Profits = {maxValueDate} (${maxValue})")
 
# # The greatest decrease in losses (date and amount) over the entire period
    print(f"Greatest Decrease in Profits = {minValueDate} (${minValue})")
