url = 'https://s3.amazonaws.com/ir-data-now/csv/Road_driver_stats.csv'
 
# Fetch the CSV file using requests and load it into a DataFrame
response = requests.get(url)
 
# Write the content to a file
csv_file_path = 'Road_driver_stats.csv'
with open(csv_file_path, 'wb') as f:
    f.write(response.content)
 
# Read the CSV file with pandas
df = pd.read_csv(csv_file_path)
 
# Remove the CSV file
os.remove(csv_file_path)
 
# Filter for specific rows using the isin() method
drivers = ['Chip Witt', 'REDACTED', 'REDACTED', 'REDACTED', 'REDACTED']
df_filtered = df[df['DRIVER'].isin(drivers)]
 
# Extract specific columns using the loc[] method
df_extracted = df_filtered.loc[:, ['DRIVER', 'CLASS', 'IRATING']]
 
# Sort the resulting data using the sort_values() method
df_sorted = df_extracted.sort_values(by='DRIVER')
 
print(df_sorted)