import pandas as pd

# converts txt file to csv
# note: make sure to include header or pd will assume first header value
read_file = pd.read_csv(r'domains.txt') # input (r"filename.txt")
read_file.to_csv(r'domains.csv') # input(r"new_filename.csv")

