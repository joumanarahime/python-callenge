import os
import csv
import operator

voteCount=0
candidates={}
counter=0
appendedCandidate=""
higherVotes=0
winner=""


csv_path= os.path.join("..", "pyPoll","pyPollData.csv")

with open(csv_path,newline="") as dataFile:
    csv_reader=csv.reader(dataFile,delimiter=",")
    csv_header=next(csv_reader)
    sorted_list= sorted(csv_reader, key=operator.itemgetter(2))

    for votes in sorted_list:
        voteCount= voteCount + 1
        

        if len(candidates)== 0:
            candidates= {votes[2]:1}
            appendedCandidate = votes[2]
           # print(appendedCandidate)
        elif appendedCandidate == votes[2]:
            counter = counter + 1
            candidates.update({votes[2]:counter}) 
        elif appendedCandidate != votes[2]:
            #print(f"{appendedCandidate} === {votes[2]}")
            counter= 1
            candidates.update({votes[2]:counter})
            appendedCandidate = votes[2]
            


   # print(candidates)  

# The total number of votes cast
print("--------------------------------")
print(f"Total Votes:: {voteCount}")
print("--------------------------------")

for keys, val in candidates.items():
    print(f"{keys} :  {round((val/voteCount)*100)}.000%  ({val})")
   
    if  val > higherVotes:
        higherVotes= val 
        winner = keys
      
print("--------------------------------")
print(f"Winner of the election is {winner}.")
print("--------------------------------")

