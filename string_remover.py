filename = "domains.txt"

# Text file last_names.txt able with a large quantity of numbers and excess characters after each name
# Using current knowledge I created a code to remove all numbers and excess characters

with open(filename,"r") as file_object:
    """ Removes numbers and percentage symbol from text file """
    contents = file_object.read()
    print(contents.replace(str(9),"").replace(str(8), "").replace(str(7),"").replace(str(6), "").replace(str(5), "")\
        .replace(str(4), "").replace(str(3), "").replace(str(2), "").replace(str(1), "").replace(str(0), "")\
        .replace("%", "").lstrip("\t").replace("        ", ""))
