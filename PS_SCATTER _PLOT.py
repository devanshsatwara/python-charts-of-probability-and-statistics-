#SCATTER PLOT

import matplotlib.pyplot as plt 
#x axis value  
marks = [0,2,4,6,7,8,9,10] 
# y axis value
freq_marks = [7,1,3,7,5,10,17,4] 
  
# plotting points as a scatter plot 
plt.scatter(marks, freq_marks, label= "Marks", color= "#004099",  marker= ",", s=20) 
  
# x-axis label 
plt.xlabel('Marks') 
# frequency label 
plt.ylabel('Freq.of marks') 
# plot title 
plt.title('07 Scatter plot') 

  
# function to show the plot 
plt.show()