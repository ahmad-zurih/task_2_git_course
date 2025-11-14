import pandas as pd

# Let's suppose we have the following DataFrame
df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [23, 78, 22, 19],
    'Country': ['USA', 'USA', 'Canada', 'Australia']
})

# Print the entire DataFrame
print(df)


# Task 1: Function to calculate and print the average age
def print_average_age(dataframe):
    avg_age = dataframe['Age'].mean()
    print(f"Average age: {avg_age:.2f}")

# Task 2: Function to count and print the number of unique countries
def print_unique_country_count(dataframe):
    unique_count = dataframe['Country'].nunique()
    print(f"Number of unique countries: {unique_count}")

# Run tasks
print_average_age(df)
print_unique_country_count(df)

def calculate_average_age(dataframe):
    average_age = dataframe['Age'].mean()
    print(f"The average age is: {average_age}")

def count_unique_countries(dataframe):
    unique_countries = dataframe['Country'].nunique()
    print(f"The number of unique countries is: {unique_countries}")