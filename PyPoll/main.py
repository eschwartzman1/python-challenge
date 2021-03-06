# Dependencies
# --------------------------------------
import csv

# Files to Load / Output
# --------------------------------------
file_to_load = "election_data_2.csv"
file_to_output = "election_analysis_2.txt"

# Variables to Track
# --------------------------------------
# [{"Khan": 5}, {"Li": 2}, {"Correy": 70}]
candidate_options = []
candidate_votes = {}
voting_percent = []
loop_count = 0

winning_candidate = ""
winning_count = 0

total_votes = 0

greatest_vote_candidate = ""
greatest_vote_percentage = 0

# Main Process 
# --------------------------------------
# Reading the file
with open(file_to_load) as election_data:
  reader = csv.DictReader(election_data)

  # For Each row...
  for row in reader:

    # Total Votes
    total_votes = total_votes + 1

    # Build our Array of Unique Candidates 
    if row["Candidate"] not in candidate_options:

      # Add the candidate as an option
      candidate_options.append(row["Candidate"])

      # Set that candidate's initial vote count to 0
      candidate_votes[row["Candidate"]] = 0

    # If the candidate is NOT unique
    candidate_votes[row["Candidate"]] =  candidate_votes[row["Candidate"]] + 1

  print("----------------------")
  print("Election Results")
  print("----------------------")

  
  for key, value in candidate_votes.items():

    print(key)
    print(str(value) + " votes")
    print(str(int(value) * 100 / total_votes) + "%")
    print("----------------------")

    
    voting_percent.append(int(value) * 100 / total_votes)


  # # Iterate through the candidate_votes
  for candidate in candidate_votes:

    votes = candidate_votes[candidate]
    vote_percentage = (votes / total_votes)  * 100
  #   print(votes)
  #   print(total_votes)
  #   print("-----------------")
  #   print(vote_percentage)
  #   print("-----------------")

    if(vote_percentage > greatest_vote_percentage):

      greatest_vote_candidate = candidate
      greatest_vote_percentage = vote_percentage

  # # Printing Election Results/The Winner
  # print("Election results ")
  # print("----------------------")
  # print("Total votes: " + str(total_votes))
  # print("----------------------")
  # print("Khan: ")
  # print("Li: ")
  # print("Correy: ")
  # print("O'Tooley: ")

  # print(str(vote_percentage) + " %")
  print("----------------------")
  print("The winning candidate is " + greatest_vote_candidate)
  print("The greatest vote percentage is: " + str(greatest_vote_percentage) + "%")
  print("----------------------")
  

# Write Output
  with open(file_to_output, "w") as txt_file:
      
      txt_file.write("Election results" + "\n")
      txt_file.write("--------------------" + "\n")
      txt_file.write("Total votes: " + str(total_votes) + "\n") 
      
      
      
      for key, value in candidate_votes.items():
       
       
       
       txt_file.write("--------------------" + "\n")       
       txt_file.write(key + "\n")
       txt_file.write(str(value) + " votes" + "\n")
       txt_file.write(str(voting_percent[loop_count]) + "%" + "\n")
       loop_count = loop_count+1
      txt_file.write("--------------------" + "\n")       
      txt_file.write("The winning candidate is " + greatest_vote_candidate + "\n")
      txt_file.write("The greatest vote percentage is: " + str(greatest_vote_percentage) + "%" + "\n")