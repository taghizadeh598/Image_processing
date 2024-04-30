import numpy as np
#Creating a simple NumPy array
arr=np.array([1, 2, 3, 4])
#Sum of elements
total = arr.sum()
# Mean of elements
mean_value = arr.mean()
#Standard deviation
std_dev = arr.std()
#Multidimensional array
multi_arr = np.array([[1, 2, 3], [4, 5, 6]])
#Correlation coefficient
corr = np.corrcoef(multi_arr)
print(total,mean_value,std_dev,corr)
identity_matrix=np.array([[1,0,0],[0,1,0],[0,0,1]])
#Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(identity_matrix)
import pandas as pd
df = pd.read_csv('data.csv')
print(df)
print(df.head(10))
#Print the first 5 rows of the DataFrame:
print(df.head())
#There is also a tail() method for viewing the last rows of the DatFrame.
#Print the last 5 rows of the DataFrame:
print(df.tail())
#The DataFrames object has a method called info(), that gives you more information about the data set.
print(df.info())
print(df.corr())
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
df.plot()
plt.show()

#scatter data
df = pd.read_csv('data.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()

