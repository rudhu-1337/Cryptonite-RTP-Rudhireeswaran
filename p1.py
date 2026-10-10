import pandas as pd

# 1. Create a DataFrame from a Python dictionary
data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["HR", "IT", "IT", "Sales", "HR"],
    "Salary": [60000, 85000, None, 95000, 62000], 
    "Experience_Years": [2, 5, 1, 7, 4]  # Fixed: Added the missing list of years
}

df = pd.DataFrame(data)
print("--- Original DataFrame ---")
print(df)
# 2. Clean Data: Fill missing values (NaN) with the average salary
average_salary = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(average_salary)
print("\n--- After Cleaning Missing Salary ---")
print(df)

# 3. Filter Data: Select employees with more than 3 years of experience
experienced_staff = df[df["Experience_Years"] > 3]
print("\n--- Experienced Staff (> 3 years) ---")
print(experienced_staff)

# 4. Aggregate Data: Find the average salary per department
dept_summary = df.groupby("Department")["Salary"].mean()
print("\n--- Average Salary by Department ---")
print(dept_summary)

import numpy as np

# Creating 5x4 array
array = np.arange(20).reshape(5, 4)
print(array)
print()

# If no axis mentioned, then it works on the entire array
print(np.argmax(array))

# If axis=1, then it works on each row
print(np.argmax(array, axis=1))

# If axis=0, then it works on each column
print(np.argmax(array, axis=0))

import numpy as np

list = [
    np.array([3, 2, 8, 9]),
    np.array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])
]

result = []
for i in range(len(list)):
    result.append(float(np.mean(list[i])))
print(result)