#Import modules
import csv
import os
import string
#create path to input file
election_data_file_path =  os.path.join("Resources/" + "election_data.csv")
#create path to output file
election_analysis_file_path =  os.path.join("analysis/" + "election_analysis.txt")
#analyse election
with open(election_data_file_path) as election_data_file:
	#create csv reader
	election_reader = csv.reader(election_data_file)
	#process election entries
	next(election_data_file)
	vote_count = 0
	candidate_list = [] #candidate name, vote count
	for line in election_reader:
		vote_count = vote_count + 1
		if len(candidate_list) == 0:
			#add first candidate
			candidate_list.append([line[2], 1])
		else:
			#update candidate list
			match = 0
			for i in range(len(candidate_list)):
				if candidate_list[i][0] == line[2]:
					candidate_list[i][1] = candidate_list[i][1] + 1
					match = 1
			if match == 0:
				candidate_list.append([line[2], 1])

#load formatted output
output_dict = [{"label": "Total Votes: ", "value": str(vote_count)}]
winner_count = 0
candidate_count = len(candidate_list)
for i in range(candidate_count):
	output_dict.append({"label": candidate_list[i][0], "percent": "{:.3%}".format(candidate_list[i][1]/vote_count), "value": " (" + str(candidate_list[i][1]) + ")"})
	if winner_count < candidate_list[i][1]:
		winner = candidate_list[i][0]
		winner_count = candidate_list[i][1]
output_dict.append({"label": "Winner: ", "value": winner})

#display analysis on terminal
print("Election Results")
print("________________________")
print(output_dict[0]["label"] + (output_dict[0]["value"]))
print("________________________")
for i in range(1, candidate_count + 1):
	print(output_dict[i]["label"] + " " + output_dict[i]["percent"] + (output_dict[i]["value"]))
print("________________________")	
print(output_dict[i + 1]["label"] + (output_dict[i + 1]["value"]))
print("________________________")

#write analysis to text file
with open(election_analysis_file_path, "w") as election_analysis_file:
	election_analysis_file.write("Election Results\n")
	election_analysis_file.write("________________________\n")
	election_analysis_file.write(output_dict[0]["label"] + (output_dict[0]["value"] + "\n"))
	election_analysis_file.write("________________________\n")
	for i in range(1, candidate_count + 1):
		election_analysis_file.write(output_dict[i]["label"] + " " + output_dict[i]["percent"] + (output_dict[i]["value"] + "\n"))
	election_analysis_file.write("________________________\n")	
	election_analysis_file.write(output_dict[i + 1]["label"] + (output_dict[i + 1]["value"]) + "\n")
	election_analysis_file.write("________________________\n")
