#BAR GRAPH
# importing the required module 
import matplotlib.pyplot as plt 
  
# x axis values 
marks = [25, 6, 185, 13, 17.5, 94, 8, 22, 160, 63, 93, 55, 1.2, 94, 63, 25, 18, 3, 11.4, 165, 0.6, 19, 70, 60, 20, 33, 19, 11, 1.1, 3.18, 12.5, 3.3, 11.49, 40, 90, 35, 103, 20, 6, 21.15, 45, 102, 5, 3.7, 19, 5, 0.8, 0.95, 1.5, 1.5, 4, 55, 3.4, 9.3, 90, 356, 321, 175, 100, 250, 7.3, 1.6, 180, 2, 3, 9, 22.23, 30, 18, 19, 31.5, 11, 1.8, 3, 0.93, 1, 1.75, 2, 3.8, 70, 20, 4.5, 15, 10, 30, 72, 1.2, 18.5, 18, 32.5, 19.79, 12, 2.47, 2.54, 0.83, 0.25, 5.5, 2.2, 0.04, 15] 
 
  
# plotting a bar chart 
plt.bar(marks) 
  
# naming the x-axis 
plt.xlabel('Marks') 


# plot title 
plt.title('Bar Graph') 
  
# function to show the plot 
plt.show() 