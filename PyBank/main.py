# Analyze the financial record of a company
# Given financial dataset with 2 columns - Date and Profit/Losses

# Following values are calculated
# - The total number of months included in the dataset
# - The net total amount of "Profit/Losses" over the entire period
# - The changes in "Profit/Losses" over the entire period, and then the average of those changes
# - The greatest increase in profits (date and amount) over the entire period
# - The greatest decrease in profits (date and amount) over the entire period

import os
import csv


# Function to read CSV file and analyze the data provided
# parameter: file name of CSV file, defaults to budget_data.csv
# return: analysis results in a list
def analyzeBudgetData(fileName="budget_data.csv"):
    
    filePath = os.path.join(".", "Resources", fileName)
    
    # Open the CSV file
    with open(filePath, "r") as budgetDataFile:
        
        # Read the CSV file
        budgeDataCSVReader = csv.reader(budgetDataFile, delimiter=",")
        
        # Read the header
        budgeDataHeader = next(budgeDataCSVReader)
        
        # Declare variables
        totalNbrOfMonths = 0
        netTotalAmtOfProfitLoss=0
        changeInProfitLoss = []
        averageChangeInProfitLoss = 0.00
        greatestIncreaseInProfitRowIndex = 0
        greatestDecreaseInProfitRowIndex = 0

        previousMonthProfitLoss = 0
      
        # Read all lines in the CSV file to a list  
        rows = list(budgeDataCSVReader)
        
        # Read the rows
        for row in rows:
            
            # Calculate the total number of months included in the dataset 
            totalNbrOfMonths +=1
            
            # Calculate the net total amount of "Profit/Losses" over the entire period
            netTotalAmtOfProfitLoss += int(row[1])
            
            # Store the changes in "Profit/Losses" over the entire period
            if(totalNbrOfMonths != 1):
                changeInProfitLoss.append(int(row[1]) - previousMonthProfitLoss)
            previousMonthProfitLoss = int(row[1])
        
        # Calculate the average of "Profit/Loss" changes over the period
        averageChangeInProfitLoss = sum(changeInProfitLoss) / len(changeInProfitLoss)
        
        # Find the index of the row that holds greatest increase in profits (date and amount) over the entire period
        greatestIncreaseInProfitRowIndex = changeInProfitLoss.index(max(changeInProfitLoss))
        
        # Find the index of the row that holds greatest decrease in profits (date and amount) over the entire period
        greatestDecreaseInProfitRowIndex = changeInProfitLoss.index(min(changeInProfitLoss))
        
        # Create print buffer and store the result lines
        printBuffer = []
        printBuffer.append("Financial Analysis\n")
        printBuffer.append("------------------------------\n")
        
        printBuffer.append(f"Total Months: {totalNbrOfMonths}\n")
        
        printBuffer.append(f"Total: ${netTotalAmtOfProfitLoss}\n")
        
        printBuffer.append("Average Change: $%.2f" %averageChangeInProfitLoss + "\n")
        
        printBuffer.append(f"Greatest Increase in Profits: {rows[greatestIncreaseInProfitRowIndex + 1][0]} (${changeInProfitLoss[greatestIncreaseInProfitRowIndex]})\n")
        
        printBuffer.append(f"Greatest Decrease in Profits: {rows[greatestDecreaseInProfitRowIndex + 1][0]} (${changeInProfitLoss[greatestDecreaseInProfitRowIndex]})\n")
        
        # Print the result lines
        for line in printBuffer:
            print(line)
        return printBuffer

# Function to write analysis to a file
# parameters: results - analysis results in a list, 
#             resultFileName = file to store the analysis results, defaults to FinancialResults.txt
def printResults(results, resultFileName="FinancialResults.txt"):
    
    # Set the file path
    filePath = os.path.join(".", "analysis", resultFileName)

    # Open the file for writing
    with open(filePath, 'w') as resultFile:
        
        #Write the results to file
        resultFile.write('\n'.join(results))
            
# Call functions to analysze budget data and print results
printResults(analyzeBudgetData())
