# Table of Contents
1. [Strategy and Assumptions](README.md#strategy-and-assumptions)
1. [Method and Functions](README.md#method-and-functions)
1. [Possible Improvements](README.md#possible-improvements)

# Strategy and Assumptions

In this program I have assumed that the declaration of the data used is made on the very first line. For example the first line states that the order of data is of the form $drug_name, prescriber_last_name, prescriber_first_name, drug_cost, or at least contains these identifiers.
After reading in the data line by line, I construct a library, in order to categorize the data.
I then use a customized ``mergesort" function in order to read through the dictionary and sort the data efficiently, with the given requirement.
The input file is looked through, sorted, and as a result a sorted output file is created.

## Input file
The input file must be uploaded into the input folder. In order for the Run.sh script to automatically run the code, the input text file should be the only text file in the folder.

# Method and Functions
The functions used are: #\n
1- Sort: This takes in the required variable lists (cost list and drug names list), and outputs a permutation index list, in order to map the unsorted list to a sorted one. #\n
2- Merger: This function is used implicitly in the Sort function, and is a part of the mergesort algorithm, for efficient sorting. 
3- Word_detector: This function takes in a line of string and outputs words that were separated by a comma or a space. This function is utilized to read every line of the input file and output the desired data.

# Possible Improvements
Improvements can be made in the code in order to detect broken data. For example the code could produce a list with all the data that were recorded in the input file correctly, and another that contains the data with missing name or cost input. 

