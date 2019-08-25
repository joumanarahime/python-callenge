import os
import csv
import operator

voteCount=0
candidates=[]
counter=0
appendedCandidate=""


csv_path= os.path.join("..", "pyPoll","pyPollData.csv")

with open(csv_path,newline="") as dataFile:
    csv_reader=csv.reader(dataFile,delimiter=",")
    csv_header=next(csv_reader)
    sorted_list= sorted(csv_reader, key=operator.itemgetter(2))
  
    

    for votes in sorted_list:
        voteCount= voteCount + 1
        

        if len(candidates)==0:
            candidates.append(votes[2])
            appendedCandidate = votes[2]
            # print(appendedCandidate)

        if appendedCandidate != votes[2]:
            #print(f"{appendedCandidate} === {votes[2]}")
            candidates.append(votes[2])
            appendedCandidate = votes[2]


    print(candidates)  

# The total number of votes cast
print(f"Total Votes:: {voteCount}")
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.