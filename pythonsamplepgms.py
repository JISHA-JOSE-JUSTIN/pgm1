# Import pandas
import pandas as pd
# Create a series of three different colours
Series1=pd.Series(["Black","Red","Blue"])
# View the series of different colours
print(Series1)
0    Black
1      Red
2     Blue
dtype: object

# Create a series of three different car types and view it
Series2=pd.Series(["Sedan","SUV","Supercar"])
print(Series2)

0       Sedan
1         SUV
2    Supercar
dtype: object

# Combine the Series of cars and colours into a DataFrame
dFrame=pd.DataFrame([Series1,Series2])
print(dFrame)

      0    1         2
0  Black  Red      Blue
1  Sedan  SUV  Supercar

# Import "../data/car-sales.csv" and turn it into a DataFrame
car_sale=pd.read_csv("/home/shibuviswam/INTEL Unnati/workshop/Python-Exercise/car-sales.csv")
print(car_sale)
 Make Colour  Odometer (KM)  Doors       Price
0  Toyota  White         150043      4   $4,000.00
1   Honda    Red          87899      4   $5,000.00
2  Toyota   Blue          32549      3   $7,000.00
3     BMW  Black          11179      5  $22,000.00
4  Nissan  White         213095      4   $3,500.00
5  Toyota  Green          99213      4   $4,500.00
6   Honda   Blue          45698      4   $7,500.00
7   Honda   Blue          54738      4   $7,000.00
8  Toyota  White          60000      4   $6,250.00
9  Nissan  White          31600      4   $9,700.00

# Export the DataFrame you created to a .csv file
car_sale.to_csv("/car-sales.csv")
# Find the different datatypes of the car data DataFrame
car_sale.dtypes
Unnamed: 0        int64
Make             object
Colour           object
Odometer (KM)     int64
Doors             int64
Price            object
dtype: object

# Describe your current car sales DataFrame using describe()
car_sale.describe()

Unnamed: 0	Unnamed: 0.1	Odometer (KM)	Doors
count	10.00000	10.00000	10.000000	10.000000
mean	4.50000	4.50000	78601.400000	4.000000
std	3.02765	3.02765	61983.471735	0.471405
min	0.00000	0.00000	11179.000000	3.000000
25%	2.25000	2.25000	35836.250000	4.000000

# Get information about your DataFrame using info()
car_sale.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 8 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0   Unnamed: 0      10 non-null     int64 
 1   Unnamed: 0.1    10 non-null     int64 
 2   Unnamed: 0.1.1  10 non-null     int64 
 3   Make            10 non-null     object
 4   Colour          10 non-null     object
 5   Odometer (KM)   10 non-null     int64 
 6   Doors           10 non-null     int64 
 7   Price           10 non-null     object
dtypes: int64(5), object(3)
memory usage: 768.0+ bytes
50%	4.50000	4.50000	57369.000000	4.000000
75%	6.75000	6.75000	96384.500000	4.000000
max	9.00000	9.00000	213095.000000	5.000000

# Create a Series of different numbers and find the mean of them
series3=pd.Series([1,2,3,4,5,6,7,8,9])
print(series3.mean())
5.0

# Create a Series of different numbers and find the sum of them
series3=pd.Series([1,2,3,4,5,6,7,8,9])
print(series3.sum())
45

# List out all the column names of the car sales DataFrame
car_sale.columns

Index(['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1', 'Unnamed: 0.1.1.1',
       'Unnamed: 0.1.1.1.1', 'Unnamed: 0.1.1.1.1.1', 'Make', 'Colour',
       'Odometer (KM)', 'Doors', 'Price'],
      dtype='object')

# Find the length of the car sales DataFrame
# Show the first 5 rows of the car sales DataFrame
# Show the first 7 rows of the car sales DataFrame
# Show the bottom 5 rows of the car sales DataFrame
# Use .loc to select the row at index 3 of the car sales DataFrame
# Use .iloc to select the row at position 3 of the car sales DataFrame
# Select the "Odometer (KM)" column from the car sales DataFrame
# Find the mean of the "Odometer (KM)" column in the car sales DataFrame
# Select the rows with over 100,000 kilometers on the Odometer
# Create a crosstab of the Make and Doors columns
# Group columns of the car sales DataFrame by the Make column and find the average
# Import Matplotlib and create a plot of the Odometer column
# Don't forget to use %matplotlib inline
# Create a histogram of the Odometer column using hist()
# Try to plot the Price column using plot()


# Remove the punctuation from price column
# Check the changes to the price column
# Remove the two extra zeros at the end of the price column
# Check the changes to the Price column
# Change the datatype of the Price column to integers
# Lower the strings of the Make column
# Make lowering the case of the Make column permanent
# Check the car sales DataFrame
# Import the car sales DataFrame with missing data ("../data/car-sales-missing-data.csv")
# Check out the new DataFrame
# Fill the Odometer column missing values with the mean of the column inplace
# View the car sales missing DataFrame and verify the changes
# Remove the rest of the missing data inplace
# Verify the missing values are removed by viewing the DataFrame
# Create a "Seats" column where every row has a value of 5
# Create a column called "Engine Size" with random values between 1.3 and 4.5
# Remember: If you're doing it from a Python list, the list has to be the same length
# as the DataFrame
# Create a column which represents the price of a car per kilometer
# Then view the DataFrame
# Remove the last column you added using .drop()
# Shuffle the DataFrame using sample() with the frac parameter set to 1
# Save the the shuffled DataFrame to a new variable
# Reset the indexes of the shuffled DataFrame
# Change the Odometer values from kilometers to miles using a Lambda function
# Then view the DataFrame
# Change the title of the Odometer (KM) to represent miles instead of kilometers