#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import scipy as sp
import scipy.stats
import matplotlib.pyplot as plt

text_file = open("/Users/rishika/Desktop/anomaly_detection.txt", "r+")
lines = text_file.readlines()
new_file=[]
text_file.close()
for item in lines:
    new_file.append(item.strip())
    
string_array= np.array(new_file)

float_array= string_array.astype(np.float)

def mean_cal(array):
    mean= np.mean(array)
    return mean

def standard_deviation_cal(array):
    
    standard_deviation= np.std(array) 
    return standard_deviation


    

def anomaly_detection(array):
    index=0
    array.sort() 
    while index < len(array):
        item= array[index]
        array1=np.delete(array,index,0)
        
        if  ((array[index]) < (mean_cal(array1)-(3* standard_deviation_cal(array1)))) or (array[index]) > ((3* standard_deviation_cal(array1))+ mean_cal(array1)):
            cal_times=abs( ((array[index] - mean_cal(array1))/standard_deviation_cal(array1)))
                       
            print("Remove " + str(array[index]) +" from the list because it's "+ str(cal_times)+" times the standard deviation of the list without it " )
            print(str(array[index])+" is removed from the list")
            
            
            array=np.delete(array,index,0)
            index=0
            
        else:
            
            index+=1
           
    print("No more anomaly detected!")            
#     x=array
#     v=sp.stats.norm.pdf(array,mean_cal(array),standard_deviation_cal(array))
#     return plt.plot(x,v) 
       
         
             
        
print(anomaly_detection(float_array))

