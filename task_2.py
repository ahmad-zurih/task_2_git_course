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
    pass
    average_age = dataframe['Age'].mean()
    print(f"Average Age: {average_age}")

# Task 2: Function to count and print the number of unique countries
def print_unique_country_count(dataframe):
    pass

# Run tasks
print_average_age(df)
#print_unique_country_count(df)

