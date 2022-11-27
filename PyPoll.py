# The Data we need to retrieve
#1 Total # of Votes Cast
#2 Complete list of Candidates
#3 Total # of votes each Candidate received
#4 % of votes each candidate won
#5 Winner of election on popular vote
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1 Initialize a total vote counter.
total_votes=0

candidates=[]
candidate_votes = {}
#{"name":"","votes":""}

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)

    for row in file_reader:
        #2. Add to the total vote count.
        total_votes +=1
        candidate=row[2]
        #check if in candidate list
        if candidate not in candidates:
            candidates.append(candidate)
        #add to candidate votes
            candidate_votes[candidate]=0

        candidate_votes[candidate] +=1    


#3. Print the total votes.
print(f'Total Votes: {total_votes}')
print(f'We Had {len(candidates)} candidates')
print(candidate_votes)

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

for candidate in candidates:
    votes=candidate_votes[candidate]
    vote_percentage = float(votes)/float(total_votes)*100

    if(votes>winning_count) and (vote_percentage>winning_percentage):
        #if true then set winning_count=votes and winning_percent=vote_percentage

        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate
    print("")
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
