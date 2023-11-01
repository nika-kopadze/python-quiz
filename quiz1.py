import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('data.csv')

# Extract rows 1 to 3 and columns 'Name' and 'Age'
desired_data = data.loc[1:3, ['Name', 'Age']]
print(desired_data)


# Assign 'Name' column as the index
data.set_index('Name', inplace=True)
print(data)


# Create a filter for age > 30 and salary > 60000
filter_condition = (data['Age'] > 30) & (data['Salary'] > 60000)
filtered_data = data[filter_condition]
print(filtered_data)


# Sort the data by 'Age' in descending order and then by 'Salary' in ascending order
sorted_data = data.sort_values(by=['Age', 'Salary'], ascending=[False, True])
print(sorted_data)



# Calculate mean, standard deviation, median, min, and max of 'Age' and 'Salary'
mean_age = data['Age'].mean()
std_age = data['Age'].std()
median_age = data['Age'].median()
min_age = data['Age'].min()
max_age = data['Age'].max()

mean_salary = data['Salary'].mean()
std_salary = data['Salary'].std()
median_salary = data['Salary'].median()
min_salary = data['Salary'].min()
max_salary = data['Salary'].max()

print(f"Age Statistics: Mean={mean_age}, Std={std_age}, Median={median_age}, Min={min_age}, Max={max_age}")
print(f"Salary Statistics: Mean={mean_salary}, Std={std_salary}, Median={median_salary}, Min={min_salary}, Max={max_salary}")


# Bar chart for 'Age'
plt.figure(figsize=(8, 5))
plt.bar(data.index, data['Age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age Distribution')
plt.xticks(rotation=45)
plt.show()

# Line chart for 'Salary'
plt.figure(figsize=(8, 5))
plt.plot(data.index, data['Salary'], marker='o', linestyle='-')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Salary Trends')
plt.xticks(rotation=45)
plt.show()
