import pandas as pd
import matplotlib.pyplot as plt

n = int(input("Enter number of students: "))

d = {
    "id": [],
    "sh": [],
    "sl": [],
    "sc": [],
    "ex": [],
    "mk": []
}

for i in range(n):
    print(f"\nStudent {i+1}")
    d["id"].append(int(input("ID: ")))
    d["sh"].append(float(input("Study hours: ")))
    d["sl"].append(float(input("Sleep hours: ")))
    d["sc"].append(float(input("Screen time: ")))
    d["ex"].append(float(input("Exercise hours: ")))
    d["mk"].append(int(input("Marks: ")))

df = pd.DataFrame(d)
df.to_csv("student_habits.csv", index=False)

df = pd.read_csv("student_habits.csv")
print(df)

print(df.mean())
print(df.corr())

plt.bar(df["sh"], df["mk"])
plt.xlabel("Study hours")
plt.ylabel("Marks")
plt.title("Study vs Marks")
plt.show()

plt.plot(df["sl"], df["mk"], marker='o')
plt.xlabel("Sleep hours")
plt.ylabel("Marks")
plt.title("Sleep vs Marks")
plt.show()

act = ["Study", "Sleep", "Screen", "Exercise"]
avg = [df["sh"].mean(), df["sl"].mean(), df["sc"].mean(), df["ex"].mean()]

plt.pie(avg, labels=act, autopct='%1.1f%%')
plt.title("Daily Activity")
plt.show()

h = len(df[df["mk"] >= 85])
m = len(df[(df["mk"] >= 70) & (df["mk"] < 85)])
l = len(df[df["mk"] < 70])

plt.pie([h, m, l], labels=["High", "Medium", "Low"], autopct='%1.1f%%')
plt.title("Marks Distribution")
plt.show()
