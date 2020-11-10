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

group = []
for name in range(3):
    rd_full_email = random.choice(df_female_first_name) + "@" + random.choice(df_domains)
    group.append(rd_full_email)

print(group)