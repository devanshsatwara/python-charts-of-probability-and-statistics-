#LINE GRAPH
# importing the required module 
import matplotlib.pyplot as plt 

# x axis values 
marks = [0,2,4,6,7,8,9,10] 
# y axis value
freq_marks = [7,1,3,7,5,10,17,4] 

# plotting the points  
plt.plot(marks, freq_marks) 

# naming the x axis 
plt.xlabel('Marks') 
# naming the y axis 
plt.ylabel('Freq of Marks') 

# giving a title to my graph 
plt.title('Line Graph') 

# function to show the plot 
plt.show()