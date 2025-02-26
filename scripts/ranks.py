import matplotlib.pyplot as plt

students = ['Alice', 'Bob', 'Charlie', 'David']
marks = [85, 90, 78, 88]
ranks = [2, 1, 4, 3]

fig, ax = plt.subplots()
bars = ax.barh(students, marks, color='skyblue')

# Adding text labels
for bar, mark, rank in zip(bars, marks, ranks):
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, f'Marks: {mark}, Rank: {rank}', ha='center', va='bottom')

ax.set_xlabel('Marks')
ax.set_ylabel('Students')
ax.set_title('Student Marks and Ranks')
plt.show()
