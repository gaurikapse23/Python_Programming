import matplotlib.pyplot as plt

plt.hist(df["StudyHours"], bins=10)
plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.show()