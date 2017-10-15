#from __future__ import division

#import numpy as np
#import matplotlib.pyplot as pl

#import discrete
#import dp
#import rl
import os
import re
import pandas as pd
import csv
#File1 = open("C:\Users\Ajesh\Desktop\UNH\Courses\CS980\smallsize_test_nr.csv", 'r')
#File1 = csv.reader(open('C:\Users\Ajesh\Desktop\UNH\Courses\CS980\smallsize_test_nr.csv')

draft1 = pd.read_csv('C:\Users\Ajesh\Desktop\UNH\Courses\CS980\smallsize_test_nr.csv')
for i in range(0,len(draft1)):
    #print draft1['probability'][i]
    #draft1.to_csv('C:\Users\Ajesh\Desktop\UNH\Courses\CS980\smallsize_test_nr_output.csv')
	for j in range(0,4):
	    print (draft1[list(draft1)[j]][i], end=" ")
#print len(draft1)
#print draft1[list(draft1)[3]][0]
#print list(draft1)[1]
#idstate,idaction
#0,1
#1,2
#2,0

# def csv_reader(file_obj):
    # """
    # Read a csv file
    # """
    # reader = csv.reader(file_obj)
    # for row in reader:
        # print(" ".join(row))

# if __name__ == "__main__":
    # csv_path = "C:\Users\Ajesh\Desktop\UNH\Courses\CS980\smallsize_test_nr.csv"
    # with open(csv_path, "rb") as f_obj:
        # csv_reader(f_obj)
		
#try:
#for line in File1:
#    print(', '.join(line))
    # for line in File1:
        # fields = line.strip().split()
        # print fields[0][2]
		#, fields[1], fields[2], fields[3], fields[4], fields[5]
		# #for i in range(0,7):
		# #j=0
        # #Var[i] = fields[j].strip().split()
		# #j++
        # #print fields[0]
        # Var0 = fields[0].strip()
        # #print Var0
        # Var1 = fields[1].strip()
        # Var2 = fields[2].strip()
        # Var3 = fields[3].strip()
        # Var4 = fields[4].strip()
        # Var5 = fields[5].strip()
        # Var6 = fields[6].strip()
        # Var7 = fields[7].strip()
   
    # result = ''.join([i for i in Var4 if i.isdigit()])
    # print result
    
	# p = re.compile(r'\d+\.\d+')  # Compile a pattern to capture float values
    # floats = [float(i) for i in p.findall(Var6)]  # Convert strings to float
    # print floats[0]
	
#finally:
#File1.close()


# def value_iteration(m=5, n=6, goal=8, gamma=0.7):
    # # define the model.
    # P = discrete.create_gridworld(m,n)
    # R = np.zeros(m*n)
    # R[goal] = 1

    # V = np.zeros(m*n)
    # pl.clf()

    # for i in xrange(100):
        # pl.pcolor(V.reshape(n,m))
        # pl.draw()
        # raw_input()

        # Q = dp.action_values(R, gamma, P, V)
        # pi = np.argmax(Q, axis=1)
        # Ppi = dp.matrix_from_policy(P, pi)
        # V = R + gamma * Ppi.dot(V)