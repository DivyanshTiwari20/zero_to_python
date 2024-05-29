import matplotlib.pyplot as plt

#Data 
years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
participants = [10000, 20000, 30000, 40000, 60000, 80000, 100000, 112314, 130000]

# Create the histogram

plt.figure(figsize=(10,6))
plt.bar(years,participants,color="skyblue")
plt.xlabel("Year")
plt.ylabel("Number of participants")
plt.title("Python Adoption in India (2014-2022)")
plt.grid(axis="y",linestyle="--",alpha=0.7)
plt.tight_layout()

plt.show()