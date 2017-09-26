import pandas
import matplotlib.pyplot as plt
import seaborn as sns

# Convert Letter Grades to GPA

def convert_grades(df):
    numeric_val = []
    for row in df['MEDIAN']:
        if row == "A":
            numeric_val.append(4)
        elif row == "A/A-":
            numeric_val.append(3.8)
        elif row == "A-":
            numeric_val.append(3.7)
        elif row == "A-/B+":
            numeric_val.append(3.3)
        elif row == "B+":
            numeric_val.append(3.3)
        elif row == "B":
            numeric_val.append(3)
        elif row == "B-":
            numeric_val.append(2.7)
        elif row == "C+":
            numeric_val.append(2.3)
        elif row == "C":
            numeric_val.append(2)
        elif row == "C-":
            numeric_val.append(1.7)
        elif row == "D":
            numeric_val.append(1)
        elif row == "E":
            numeric_val.append(0)
        else:
            numeric_val.append(-1)

    df['NUMERIC'] = numeric_val

# Create Department
def add_depts(df):
    dep = []
    for row in df['COURSE']:
        dep.append(row[:4])
    df['DEPT'] = dep

def describe(df):
    print(df.describe())

def make_plot(df, name, term):
# Group by Department for Analysis
    by_dept = df.groupby('DEPT').mean().round(3).reset_index()
    sorted_vals = by_dept.sort_values('NUMERIC', ascending=False)

    # Save DF to .csv
    # by_dept.to_csv("aggregated.csv", sep=',')

    # Create figure
    f, ax = plt.subplots(figsize=(8, 15))
    sns.set_style("whitegrid")
    ax = sns.barplot(x="NUMERIC", y="DEPT", data=sorted_vals, palette="Blues_d")
    ax.set(xlabel='Average Grade', ylabel='Department', title=name)
    ax.figure.savefig("plots/" + term + "_plot.png")
