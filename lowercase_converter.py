filename = "male_first_names.txt"

with open(filename,"r") as file_object:
    """Converts all letters to lowercase"""
    for line in file_object: # loops through each line
        line = line.lower().rstrip() # converts each line to lowercase + strips trailing characters
        print(line)
