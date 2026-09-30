import numpy as np

# VEDA Technology - Task 11: NumPy Student Marks
# Name: pranjal jain


marks = np.array([78, 85, 92, 67, 88, 74, 95, 81, 69, 90])

print("Student Marks:", marks)
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Standard Deviation:", np.std(marks))

# Short interpretation
print("\nInterpretation:")
print("The mean represents the average student mark.")
print("The median is the middle value after sorting the marks.")
print("Maximum and minimum show the highest and lowest marks.")
print("Standard deviation shows how much the marks vary around the mean.")
