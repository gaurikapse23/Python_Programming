import seaborn as sns

sns.scatterplot(data=df, x="StudyHours", y="PreviousScore", hue="FinalResult")
plt.title("StudyHours vs PreviousScore")
plt.show()