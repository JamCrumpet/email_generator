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

female_email_address = []
def fe_email():
    for name in range(100):
        rd_full_email = random.choice(column_female_first_name) + "@" + random.choice(column_domains)
        female_email_address.append(rd_full_email + "\n")

print(*female_email_address, sep="")

