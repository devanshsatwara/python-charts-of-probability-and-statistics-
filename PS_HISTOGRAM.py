import matplotlib.pyplot as plt 
  
# frequencies 
marks = [0,0,0,0,0,0,0,2,4,4,4,6,6,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10,10,10,10] 
  
# setting the ranges and no. of intervals 
range = (0, 11) 
bins = 15  
  
# plotting a histogram 
plt.hist(marks, bins, range, color = '#61a0ff',edgecolor='#004099', 
        histtype = 'bar', rwidth = 1) 
  
# x-axis label 
plt.xlabel('Markk') 
# frequency label 
plt.ylabel('Freq. of Marks') 
# plot title 
plt.title('07_Histogram') 
  
# function to show the plot 
plt.show() 