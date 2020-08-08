#Import modules
import csv
import os
import string
#create path to input file
budget_data_file_path =  os.path.join("Resources/" + "budget_data.csv")
#create path to output file
budget_analysis_file_path =  os.path.join("analysis/" + "budget_analysis.txt")
#analyse budget
with open(budget_data_file_path) as budget_data_file:
	#create csv reader
	budget_reader = csv.reader(budget_data_file)
	#process budget entries
	next(budget_data_file)
	save_PL = 0
	month_count = 0
	tot_PL = 0
	tot_PL_chng = 0
	gtInc = 0
	gtDec = 0
	for line in budget_reader:
		budget_date = line[0]
		PL = int(line[1])
		month_count = month_count + 1
		tot_PL = tot_PL + PL
		if save_PL == 0:
			save_PL = PL
		else:
			#update analysis fields
			PL_chng = PL - save_PL
			tot_PL_chng = tot_PL_chng + PL_chng
			if PL_chng > gtInc:
				gtInc_budget_date = budget_date
				gtInc = PL_chng
			if PL_chng < gtDec:
				gtDec_budget_date = budget_date
				gtDec = PL_chng
			save_PL = PL
	avg_PL_chng = tot_PL_chng / (month_count - 1)

#load formatted output
output_dict = [{"label": "Total Months: ", "date": "", "value": str(month_count)},
				{"label": "Total: ", "date": "", "value": "${:.0f}".format(tot_PL)},
				{"label": "Average Change: ", "date": "", "value": "${:.2f}".format(avg_PL_chng)},
				{"label": "Greatest Increase in Profits: ", "date": gtInc_budget_date, "value": " (" + "${:.0f}".format(gtInc) + ")"},
				{"label": "Greatest Decrease in Profits: ", "date": gtDec_budget_date, "value": " (" + "${:.0f}".format(gtDec) + ")"}]

#display analysis on terminal
print("Financial Analysis")
print("__________________")
for i in range(5):
	print(output_dict[i]["label"] + output_dict[i]["date"] + str(output_dict[i]["value"]))
	
#write analysis to text file
with open(budget_analysis_file_path, "w") as budget_analysis_file:
	budget_analysis_file.write("Financial Analysis\n")
	budget_analysis_file.write("__________________\n")
	for i in range(5):
		budget_analysis_file.write(output_dict[i]["label"] + output_dict[i]["date"] + str(output_dict[i]["value"]) + "\n")
