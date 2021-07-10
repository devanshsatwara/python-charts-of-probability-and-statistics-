# import matplotlib.pyplot library 
import matplotlib.pyplot as plt 

data = [7,0,1,0,3,0,7,5,10,17,4] 

# separating the stem parts 
stems = [0,1,2,3,4,5,6,7,8,9,10] 

plt.ylabel('Data') # for label at y-axis 

plt.xlabel('stems') # for label at x-axis 

plt.xlim(0, 10) # limit of the values at x axis 

plt.stem(stems, data) # required plot 