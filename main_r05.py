import pandas as pd

# specify the path to the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"

# load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# extract the year range
year_range = (df['date'].dt.year.min(), df['date'].dt.year.max())

# print the results
print("The shape of the file is:", df.shape)
print("The column names are:", df.columns.tolist())
print("The year range in the file based on the 'date' column is:", year_range)
