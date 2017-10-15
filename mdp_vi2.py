import os
import re
import pandas
import csv
draft1 = pandas.read_csv('C:\Users\Ajesh\Desktop\UNH\Courses\CS980\smallsize_test_nr.csv')
try:
    for i in range(0,len(draft1)):
        draft1.to_csv('C:\Users\Ajesh\Desktop\UNH\Courses\CS980\smallsize_test_nr_output.csv')
finally:
    draft1.close()