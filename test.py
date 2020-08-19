filename = "female_first_names.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
     print(line.split())

with open(filename,"r") as file_object:
    """ Removes numbers and percentage symbol from text file """
    contents = file_object.read()
    print(contents.replace(str(9),"").replace(str(8), "").replace(str(7),"").replace(str(6), "").replace(str(5), "")\
        .replace(str(4), "").replace(str(3), "").replace(str(2), "").replace(str(1), "").replace(str(0), "")\
        .replace("%", "").lstrip("\t").replace("        ", ""))