# Automate the vote-counting process
# Given voting data file contains "Voter ID", "County" and "Candidate"

# Following values to be calcuated
# - The total number of votes cast
# - A complete list of candidates who received votes
# - The percentage of votes each candidate won
# - The total number of votes each candidate won
# - The winner of the election based on popular vote

import os
import csv

# Function to read voting data and analyze the data provided
# parameter: votingFileName, defaults to election_data.csv
# return: voting results in a list 
def analyzeVotingData(votingFileName="election_data.csv"):
    
    # Initialize the file path 
    votingFilePath = os.path.join(".", "Resources", votingFileName)
    
    # Open the CSV file
    with open(votingFilePath, 'r') as votingFile:
        
        # Read the CSV file
        votingFileReader = csv.reader(votingFile)
        
        # Read the header
        votingFileHeader = next(votingFileReader)
        
        # Declare variables
        totalVotes = 0
        listOfCandidates = {} # Dictonary: Key - Candidate Name, value = vote counted
        
        # Loop thru the CSV file
        for row in votingFileReader:
            
            # Count total votes casted
            totalVotes += 1
            
            # Record vote receved for the candidate to the dictionary
            if ( row[2] in listOfCandidates):
                listOfCandidates[row[2]] += 1
            else:
                listOfCandidates[row[2]] = 1
        
        # Find the votes received for the winner
        winnerVotes = max(listOfCandidates.values())
        
        # Find the winner name
        winner = [key for key, value in listOfCandidates.items() if value == winnerVotes] [0]
        
        
        # Store results to a list
        printBuffer = []
        
        # Add the header
        printBuffer.append("Election Results\n")
        printBuffer.append("---------------------------\n")
        
        # Add line that displays total votes
        printBuffer.append(f"Total Votes: {totalVotes}\n")
        printBuffer.append("---------------------------\n")
        
        # Add lines to print percetage vote and total votes casted for each candidate
        for candidate, votes in listOfCandidates.items():
            printBuffer.append(f"{candidate}: {(votes * 100) /totalVotes:.3f}% ({votes})\n")
        
        printBuffer.append("---------------------------\n")
            
        printBuffer.append(f"Winner: {winner}\n")
        
        printBuffer.append("---------------------------\n")
        
        for line in printBuffer:
            print(line)
        return printBuffer

# Function to write analysis to a file
# parameters: results - analysis results in a list, 
#             resultFileName = file to store the analysis results, defaults to FinancialResults.txt
def printResults(results, resultFileName="VotingResults.txt"):
    
    # Set the file path
    filePath = os.path.join(".", "analysis", resultFileName)

    # Open the file for writing
    with open(filePath, 'w') as resultFile:
        
        #Write the results to file
        resultFile.write('\n'.join(results))


# Call functions to analysze voting data and print results
printResults(analyzeVotingData())   
        
        
        