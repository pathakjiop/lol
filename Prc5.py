from matplotlib import pyplot as plt
from matplotlib import style

# 1. Line Graph
x = [1,2,3]
y = [10,11,12]
plt.plot(x,y)
plt.title("Line graph")
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

# 2. Styled Line Graph
style.use('ggplot')
x = [10, 12, 13]
y = [8, 16, 6]
x2 = [8, 15, 11]
y2 = [6, 15, 7]
plt.plot(x, y, 'b', label='line one', linewidth=5)
plt.plot(x2, y2, 'r', label='line two', linewidth=5)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

# 3. Bar Graph
Names = ['Arun','James','Ricky','Patrick']
Marks = [51,87,45,67]
plt.bar(Names,Marks,color = 'blue')
plt.title('Result')
plt.xlabel('Names')
plt.ylabel('Marks')
plt.show()

# 4. Pie Chart
Aus_Players = 'Smith', 'Finch', 'Warner', 'Lumberchane'
Runs = [42, 32, 18, 24]
explode = (0.1, 0, 0, 0)
plt.pie(Runs, explode=explode, labels=Aus_Players, autopct='%1.1f%%',
    shadow=True, startangle=90)
plt.title('Pie Chart')
plt.show()

# 5. Histogram
percentage = [97,54,45,10,20,10,30,97,50,71,40,49,40,74,95,80,65,82,70,65,55,70,75,60,52,44,43,42,45]
number_of_student = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(percentage, number_of_student, histtype='bar', rwidth=0.8)
plt.xlabel('percentage')
plt.ylabel('Number of people')
plt.title('Histogram')
plt.show()

# 6. Scatter Plot
x = [4,8,12]
y = [19,11,7]
x2 = [7,10,12]
y2 = [8,18,24]
plt.scatter(x, y)
plt.scatter(x2, y2, color='g')
plt.title('Scatter Plot')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()