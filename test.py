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


#class Female_email():
#    """An email address with a female name"""

#    def __init__(self,female_first_name,last_name,domain):
#        self.female_first_name = rd_female_first_name
#        self.last_name = rd_last_name
#       self.domain = rd_domain

        #self.rd1 = female_first_name + last_name + "@" + domain
        #self.rd2 = female_first_name + "." + last_name + "@" + domain

#    def random_femail_email(self):
#        print(random.choice(self.rd1, self.rd2))


#print("Randomly generated email:")
#Female_email.random_femail_email()

#class Male_email():
#    """An email address with a male name"""

#    def __init___(self,male_first_name,last_name,domain):
#        self.male_first_name = male_first_name
#        self.last_name = last_name
#        self.domain = domain

#print(rd_male_first_name + rd_last_name + "@" +rd_domain)


import pandas as pd
import random

# read CSV files and saves as dataframes
df_domains = pd.read_csv("domains.csv")
df_female_first_name = pd.read_csv("female_first_names.csv")
df_last_names = pd.read_csv("last_names.csv")
df_male_first_name = pd.read_csv("male_first_names.csv")

# extract necessary columns
column_domains = df_domains["domain"]
column_female_first_name = df_female_first_name["name"]
column_last_name = df_last_names["lastname"]
column_male_first_name = df_male_first_name["name"]

# pick random values from column
rd_domain = random.choice(column_domains)
rd_female_first_name = random.choice(column_female_first_name)
rd_last_name = random.choice(column_last_name)
rd_male_first_name = random.choice(column_male_first_name)

symbols = ["-", "_", "."]

# Random emails with female first name
rd_fe1 = rd_female_first_name + rd_last_name + "@" + rd_domain
rd_fe2 = rd_female_first_name + str(random.randrange(81,99)) + "@" + rd_domain
rd_fe3 = rd_female_first_name + random.choice(symbols) + rd_last_name + "@" + rd_domain

rd_fe = rd_fe1, rd_fe2, rd_fe3

# Random email with male first name
rd_me1 = rd_male_first_name + rd_last_name + "@" + rd_domain
rd_me2 = rd_male_first_name + str(random.randrange(81,99)) + "@" + rd_domain
rd_me3 = rd_male_first_name + random.choice(symbols) + rd_last_name + "@" + rd_domain

rd_me = rd_me1, rd_me2, rd_me3

def femail_email_genrator():
    for pwd in range(number):
        password = ''
        for c in range(length):
            password += random.choice(chars)
        print(password)