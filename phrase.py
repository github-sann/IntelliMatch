import pandas as pd
import jellyfish
import pickle

# Define a function to calculate Jaro-Winkler Distance between two strings
def calculate_jaro_winkler_distance(string1, string2):
    return jellyfish.jaro_winkler_similarity(string1, string2)

# Load CSV data into a DataFrame
csv_file_path = 'data.csv'  # Update with your CSV file path
df = pd.read_csv(csv_file_path)

# Get user input for a string to compare
user_input = input("Enter a string to compare with User-Generated Text: ")

# Calculate Jaro-Winkler Distance between the user input and each entry in 'User-Generated Text' column
df['jaro_winkler_distance'] = df['User-Generated Text'].apply(lambda x: calculate_jaro_winkler_distance(user_input, x))

# Save the DataFrame using pickle
pickle_file_path = 'results.pkl'
with open(pickle_file_path, 'wb') as f:
    pickle.dump(df, f)

print("Results saved successfully.")

# Later, to load the DataFrame:
# with open(pickle_file_path, 'rb') as f:
#     loaded_df = pickle.load(f)
# print("Results loaded successfully:")
# print(loaded_df[['User-Generated Text', 'jaro_winkler_distance']])
