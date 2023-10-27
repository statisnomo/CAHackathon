import time as t
import pandas as pd
import numpy as np

serno = list(range(1, 51))
state = ['Agra', 'Ahmedabad', 'Allahabad(Prayagraj)', 'Amritsar', 'Asansol Durgapur', 'Aurangabad', 'Bengaluru',
         'Bhopal', 'Chandigarh', 'Coimbatore', 'Chennai', 'Delhi', 'Dhanbad', 'Faridabad', 'Ghaziabad', 'Gwalior',
         'Hyderabad',
         'Indore', 'Jabalpur', 'Jaipur', 'Jamshedpur', 'Jodhpur', 'Kannur', 'Kanpur', 'Khozikode', 'Kochi',
         'Kolkata', 'Kollam',
         'Kota', 'Lucknow', 'Ludhiana', 'Madurai', 'Mallapuram', 'Meerut', 'Mumbai', 'Nagpur', 'Nashik', 'Patna',
         'Pune',
         'Raipur', 'Rajkot', 'Srinagar', 'Surat', 'Thiruvanthapuram', 'Thrissur', 'Tiruchirapalli',
         'Vadodra', 'Varanasi', 'Vijaywada city', 'Vizaq']
stagJ = [31, 82, 123, 0, 4, 0, 347, 0, 72, 139, 367, 497, 9, 6, 27, 0, 227, 16, 0, 179,
         20, 2, 0, 57, 184, 278, 39, 0, 0, 60, 12, 0, 0, 0, 28, 16, 0, 0, 27, 44, 0, 0, 28,
         99, 228, 229, 7, 44, 77, 98]
roabJ = [23, 12, 53, 0, 3, 0, 33, 0, 31, 35, 45, 105, 2, 2, 11, 0, 27, 0, 32, 32, 9, 1, 0, 13, 13, 12, 9, 0, 0, 7,
         25, 0, 0, 0, 33, 9, 0, 0, 3, 21, 0, 0, 23, 78, 58, 78, 0, 0, 198, 13]
oth = [17, 41, 21, 0, 2, 0, 232, 0, 4, 97, 255, 12, 23, 1, 10, 0, 43, 0, 61, 13, 23, 7, 0, 21, 134, 129, 32, 0, 0,
       4, 13, 0, 0, 0, 66, 28, 0, 0, 8, 53, 119, 4, 60, 41, 119, 0, 87, 67, 23, 34]
tna = [30, 78, 1, 7, 3, 694, 0, 96, 146, 464, 440, 55, 14, 59, 5, 746, 9, 87, 90, 1, 1, 1, 17, 299, 204, 127, 0, 0,
       307, 105, 9, 0, 0, 107, 100, 0, 0, 16, 201, 812, 37, 440, 45, 76, 237, 276, 464, 68, 299, 127]
perinj = [3, 16, 66, 0, 1, 3, 398, 0, 20, 14, 709, 111, 55, 6, 23, 3, 52, 16, 5, 93, 5, 1, 13, 84, 255, 23, 5, 0, 6,
          6,
          0, 6, 3, 13, 3, 4, 0, 0, 55, 5, 1, 13, 24, 44, 56, 78, 86, 45, 67, 19]
SIGNAL = {'Serial No': serno, 'States/UTs': state, 'Staggered Junction': stagJ,
          'Round about Junction': roabJ, 'Others': oth, 'Total number of Accidents': tna, 'Persons Injured': perinj}
SUG = pd.DataFrame(SIGNAL)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data = {'S.No': serno, 'States/UTs': state,
        'Traffic Light Signal': [31, 82, 123, 0, 4, 0, 347, 0, 72, 139, 367, 497, 9, 6, 27, 0, 227, 16, 0, 179, 20, 2,
                                 0, 57, 184, 278, 39,
                                 60, 12, 0, 0, 0, 28, 16, 0, 0, 27, 44, 0, 0, 28, 99, 228, 229, 7, 109, 44, 77, 98,
                                 189],
        'Police Controlled': [3, 12, 53, 0, 3, 0, 33, 0, 31, 35, 45, 105, 2, 2, 11, 0, 27, 0, 32, 32, 9, 1, 0, 13, 13,
                              12, 9, 0, 0, 7,
                              25, 0, 0, 0, 33, 9, 0, 0, 3, 21, 0, 0, 23, 78, 58, 78, 0, 0, 198, 13],
        'Stop Sign': [7, 41, 21, 30, 71, 29, 12, 7, 13, 20, 21, 5, 13, 3, 16, 0, 7, 0, 7, 0, 7, 24, 31, 27, 10, 5, 15,
                      3, 0, 7,
                      0, 7, 31, 23, 17, 7, 24, 31, 27, 10, 5, 15, 3, 0, 7, 0, 7, 8, 20, 0],
        'Persons Injured': [24, 29, 20, 3, 71, 29, 12, 7, 13, 20, 21, 5, 13, 3, 16, 0, 7, 0, 7, 0, 7, 24, 31, 27, 10, 5,
                            15, 3, 0, 7,
                            0, 7, 24, 31, 27, 10, 5, 15, 3, 0, 7, 0, 7, 24, 31, 27, 10, 5, 8, 27]}
df = pd.DataFrame(data)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)



print('Hello user, welcome to our program')
print('This program primarily aims on eliminating the increased wait times at junctions and allow the easy flow of traffic')
print('You will now be asked to view statistics in order to get a grasp.')
print('1 View the Accidents Classified according to Type of Junction \n'
      '2 View the Accidents Classified according to the type of control')
AC = int(input('Enter the option number: '))
if AC == 1:
    print(SUG)
    print('The graphs will now be shown')
elif AC == 2:
    print(df)

