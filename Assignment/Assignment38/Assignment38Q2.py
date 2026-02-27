print("Total Students:", len(df))

print("Passed Students:", len(df[df["FinalResult"] == 1]))

print("Failed Students:", len(df[df["FinalResult"] == 0]))