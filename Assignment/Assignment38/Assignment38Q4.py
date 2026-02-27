counts = df["FinalResult"].value_counts()
print(counts)

percentage = df["FinalResult"].value_counts(normalize=True) * 100
print("\nPercentage:")
print(percentage)