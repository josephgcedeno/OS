# -*- coding: utf-8 -*-
"""Activity 5b - FCFS Implementation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F9q2-NynQ0sVbZhwgmf_0zfAtkFnAmYV
"""

import matplotlib.pyplot as plt 
import random

process_queue = []

n = int(input('no of processes: '))
for i in range(n):
    process_queue.append([])
    process_queue[i].append(input('Enter ProcessName: '))
    process_queue[i].append(i)
    process_queue[i].append(int(input('Enter BurstTime: ')))
    

process_queue.sort(key = lambda process_queue:process_queue[1])

print('ProcessName\tArrivalTime\tBurstTime\tCompletionTime\tWaitingTime')
total=0
CT=0
WT=0
CTT=0
WTT=0
for i in range(n):
    
    CT +=process_queue[i][2]
    print(process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2],'\t\t',CT,'\t\t',WT)
    total += process_queue[i][2]
    WTT+=WT
    WT = CT
    CTT+=CT
print('Average Completion time: ',(CTT/n),'ms')
print('Average Waiting time: ',(WTT/n),'ms')


fig, gnt = plt.subplots() 
  
# Setting Y-axis limits 
gnt.set_ylim(0, 3) 
  
# Setting X-axis limits 
gnt.set_xlim(0, (total)) 
gnt.set_yticklabels([])
# Setting labels for x-axis and y-axis 
gnt.set_xlabel('ms') 
gnt.set_ylabel('GANTT CHART') 
  
# Setting ticks on y-axis 


# Labelling tickes of y-axis 

gnt.set_yticks([1])

# Setting graph attribute 
gnt.grid(True) 

numberList = ['tab:red','tab:orange','tab:blue','tab:green','tab:purple']
col = random.sample(numberList,n)
dummy = 0
for i in range(n):
  
  if i > 0:
    gnt.broken_barh([(dummy, (dummy+process_queue[i][2]))], (1, 1), facecolors =(col[i]))
    dummy = dummy+process_queue[i][2]
   
  else:
    gnt.broken_barh([(process_queue[i][1], process_queue[i][2])], (1, 1), facecolors =(col[i]))
    dummy = process_queue[i][2]