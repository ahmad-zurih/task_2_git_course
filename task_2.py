import pandas as pd

# Let's suppose we have the following DataFrame
df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [23, 78, 22, 19],
    'Country': ['USA', 'USA', 'Canada', 'Australia']
})

# Print the entire DataFrame
print(df)

# Task 1: Implement a function to calculate and print the average age of people in the DataFrame.
# Task 2: Implement a function that counts and prints the number of unique countries represented in the DataFrame.

def calculate_average_age(dataframe):
    average_age = dataframe['Age'].mean()
    print(f"The average age is: {average_age}")

def count_unique_countries(dataframe):
    unique_countries = dataframe['Country'].nunique()
    print(f"The number of unique countries is: {unique_countries}")