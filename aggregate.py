# import packages
import pandas as pd
import os
cwd = os.path.abspath('') 
files = os.listdir(cwd) 

# read an excel file and convert 
# into a dataframe object
df = pd.DataFrame(pd.read_excel("class_enrollment_summary_fall_2013.xlsx"))


  
# show the dataframe

df