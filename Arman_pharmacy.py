# " Author: 			Arman Babakhani "
# " Date Written:		February 16, 2019 "

# "" This file reads in a random text file of drugs and outputs an ordered list of drugs with their prices"" 
import os
import sys

# =================================== [1] Utilized Functions ================================= #
def Sort(unsorted_cost_list, unsorted_name_list):
	# " This function provides the sorted permutation indices "
	Que_list = []
	for i in range(len(unsorted_cost_list)):
		drug_cost = unsorted_cost_list[i]; drug_name = unsorted_name_list[i]
		Que_list.append([[drug_cost,drug_name,i]])
	while len(Que_list) > 1:
		Que_list.append(Merger(Que_list.pop(0), Que_list.pop(0)))
	Que_list = Que_list[0]
	permutation = []
	for i in range(len(Que_list)):
		permutation.append(Que_list[i][2])		# Permutation list
	return permutation

def Merger(list1, list2):
	if len(list1) == 0:
		return list2
	if len(list2) == 0:
		return list1
	# Sorting conditions:
	if list1[0][0] < list2[0][0]:	# .................. Condition1 : Total Cost
		merged_list = Merger(list1[1::], list2)
		merged_list.insert(0, list1[0])
	elif list1[0][0] == list2[0][0]: # ................. Condition2 : Name in case of tie on Condition1
		if list1[0][1] >= list2[0][1]:	
			merged_list = Merger(list1[1::], list2)
			merged_list.insert(0, list1[0])
		else:
			merged_list = Merger(list1, list2[1::])
			merged_list.insert(0, list2[0])
	else:
		merged_list = Merger(list1, list2[1::])
		merged_list.insert(0, list2[0])
	return merged_list

def Word_detector(l_text):
	words = []
	commas_index = 0
	for i in range(len(l_text)):
		if l_text[i] == ',' or i == len(l_text)-1:
			if i - commas_index > 1:
				word = l_text[commas_index:i].strip()
				words.append(word)
				commas_index = i+1
	return words 		# ..........This function must be fed a line of text at a time

# ================================ [2] Reading in the input file ============================= #
input_file = sys.argv[1]

with open(input_file, 'r') as inp_f:
	lines = inp_f.readlines()
# ================================= [3] Detecting input indices ============================== #
words = Word_detector(lines[0])
for i in range(len(words)):
	if words[i].endswith('last_name'):
		l_name_index = i
	elif words[i].endswith('first_name'):
		f_name_index = i
	elif words[i].endswith('drug_name'):
		d_name_index = i
	elif words[i].endswith('drug_cost'):
		d_cost_index = i

# ================================== [4] Collecting the Data =================================== #
drug_dict = {}
for i in range(len(lines))[1::]:	# .....................................Skipping the first line
	good_cost = True
	words = Word_detector(lines[i])
	d_name = words[d_name_index].upper(); d_lname = words[l_name_index].upper(); d_fname = words[f_name_index].upper()
	d_cost = words[d_cost_index]
	# ----------------------- 4.1 Detecting mistyped costs (entered non-digits) ------------------
	try:
		d_cost = float(d_cost)
	except:
		try: 
			d_cost = float(d_cost.strip('$'))
		except:
			good_cost = False
			print('Data Type Warning: The cost of data in line ', i, ' contains non-digits! The data on this line was ignored.')

	if good_cost:
		if d_name not in drug_dict:
			total_cost = d_cost
			drug_dict[d_name] = [d_lname], [d_fname], [d_cost]
		else:
			if d_lname not in drug_dict[d_name][0] or d_fname not in drug_dict[d_name][1]: # Detecting repetitions
				drug_dict[d_name][0].append(d_lname); drug_dict[d_name][1].append(d_fname); drug_dict[d_name][2].append(d_cost)
			if d_cost not in drug_dict[d_name][2]:
				# Detecting price contradiction for identical prescribers:
				print('There are possible contradictory cost information for the drug: ', d_name)

# ============================ [5] Inputting data in list and sorting =========================== #
drug_names = []
drug_costs = []
drug_unique_pres = []
for d_names in drug_dict:
	drug_names.append(d_names)
	drug_costs.append(sum(drug_dict[d_names][2]))
	drug_unique_pres.append(len(drug_dict[d_names][1]))

perms = Sort(drug_costs, drug_names)[::-1]			# Reversing the permutation from Ascending to Descending
drug_names = [drug_names[i] for i in perms]
drug_costs = [drug_costs[i] for i in perms]
drug_unique_pres = [drug_unique_pres[i] for i in perms]

# ============================ [6] Create output file and save =================================== #
with open('top_cost_drug.txt', 'w') as output_file:
	output_file.write('drug_name, num_prescriber, total_cost')
	for i in range(len(drug_names)):
		output_file.write(str(drug_names[i]) + ','+ str(drug_unique_pres[i]) + ',' + str(drug_costs[i]) + '\n')