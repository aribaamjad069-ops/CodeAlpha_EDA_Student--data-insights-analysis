import pandas as pd
import matplotlib.pyplot as plt

# Sample Dataset
data = {
    "Student": ["Ali", "Ahmed", "Sara", "Ayesha", "Usman"],
    "Marks": [85, 78, 92, 74, 88],
    "Study_Hours": [5, 4, 6, 3, 5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Dataset
print("Dataset:")
print(df)

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Statistical Summary
print("\nStatistics:")
print(df.describe())

# Average Marks
average_marks = df["Marks"].mean()
print("\nAverage Marks:", average_marks)

# Create Visualization
plt.figure(figsize=(6,4))
plt.bar(df["Student"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")

# Save Chart
plt.savefig("marks_analysis.png")

print("\nEDA Completed Successfully!")
