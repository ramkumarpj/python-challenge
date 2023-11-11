# Python Challenge

Python challenge tackles 2 real-world situations - PyBank and PyPoll

## PyBank
Analyze the financial records of a company
Given financial CSV data file contains "Date" and "Profit/Losses"

Following values are calculated
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The changes in "Profit/Losses" over the entire period, and then the average of those changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in profits (date and amount) over the entire period

## Files
* Source code:
    PyBank/main.py
  
* Data:
    PyBank/Resources/budget_data.csv
  
* Results:
    PyBank/analysis/FinancialResults.txt

## Run Instructions

* Open a terminal and confirm python version
  python --version

* Change directory
  cd PyBank

* Run PyBank script
  python main.py

* Results are printed on the console and also saved to analysis/FinancialResults.txt
  
## PyPoll
Automate the vote-counting process
Given election data CSV file contains "Voter ID", "County" and "Candidate"

Following values to be calcuated
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote

## Files
* Source code:
    PyPoll/main.py
  
* Data:
    PyPoll/Resources/election_date.csv
  
* Results:
    PyPoll/analysis/VotingResults.txt

## Run Instructions

* Open a terminal and confirm python version
  python --version

* Change directory
  cd PyPoll

* Run PyPoll script
  python main.py

* Results are printed on the console and also saved to analysis/VotingResults.txt
  
    
