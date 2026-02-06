#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#folder walk

import os, shutil

from pathlib import Path

p = Path.home()
print(p)

for folderName, subfolders, filenames in os.walk(p/'Downloads/com'):
    print(f'the current folder is {folderName}')
    
    for subfolder in subfolders:
        print('SUBFOLDER OF' + folderName + ': ' + subfolder)
        
    for filename in filenames:
        print('FILE INSIDE' + folderName + ': ' + filename)
        
    print('')


# In[39]:


#selective copy

import os, shutil
from pathlib import Path

p = Path.home()
print(p)

#walk through folder tree and search for file with certain ext.

for folderName, subfolders, filenames in os.walk(p/'Downloads/com'):
    print(f'the current folder is {folderName}')
    
  
    #copy these files from wherever they are into a new folder      

    for filename in filenames:
        
        if filename.endswith('.txt'):
            print('FILE INSIDE' + folderName + ': ' + filename)
            shutil.copy(folderName + '/' + filename, '/home/nick/Downloads/extraspam')
            






# In[28]:


#deleting unneeded files

#walk through a folder tree and find files > 100mb

import os, shutil

from pathlib import Path

p = Path.home()
print(p)

for folderName, subfolders, filenames in os.walk(p/'Downloads'):
    #print(f'the current folder is {folderName}')
    
    #for subfolder in subfolders:
    #    print('SUBFOLDER OF' + folderName + ': ' + subfolder)
        
    for filename in filenames:
        #filesize = os.path.getsize(filename)
        location = os.path.join(folderName,filename)
        filesize = os.path.getsize(location)
        if filesize > 1000000:
            print('Filename:' + filename + ' Location:' + location + ' Size:' + str(filesize))
       
    print('')

    #print these files with their abspath to the screen


# In[73]:


#filling in the gaps

#find all files with a given prefix in a single folder e.g. spam

import os, shutil

os.getcwd()
files = os.listdir('/home/nick/Downloads/extraspam')
print(files)
files.sort()
print(files)

#locate gap in numbering and renumber all subsequent files

for i, file in enumerate(files):
    filenum = int(file[-1])
    #print(i,filenum)
    if i != 0: 
        prevfile = files[i - 1]
        #print(prevfile)
        prevnum = int(prevfile[-1])
        #print(prevnum)
        if filenum != prevnum + 1:
            #print('error')
            print(files[i][-1]) # = str(prevnum + 1)
            files[i] = f'spam00{str(prevnum + 1)}'
            shutil.move(f'/home/nick/Downloads/extraspam/{file}' , f'/home/nick/Downloads/extraspam/{files[i]}')
           


# In[ ]:


#create files
count = 0
for i in range(6):
    count += 1
    shutil.copy(f'/home/nick/Downloads/extraspam/spam.txt' , f'/home/nick/Downloads/extraspam/spam00{count}')

