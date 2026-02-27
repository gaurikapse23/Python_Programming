print(df.groupby("FinalResult")["StudyHours"].mean())
print(df.groupby("FinalResult")["Attendance"].mean())