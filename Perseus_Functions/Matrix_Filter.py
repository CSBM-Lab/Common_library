'''Based on Perseus v1.6.15.0
Using enrichment analysis Matrix to filter out a more specific list
'''
import pandas as pd
import numpy as np
from goatools import obo_parser

'''Transform DataFrame x='column name' from string into float, excluding first row'''
def Tf_float(x):
    x = pd.to_numeric(df[x][1:], downcast='float')
    return x

'''Reduce DataFrame based on 'Category column' with value x'''
def DF_Reduce(x):
    df_filtered = df.loc[df['Category column'] == x]
    return df_filtered

# Read Matrix text file into pandas DataFrame
M_file = 'Matrix_GO_404.txt'
MA_file = 'Matrix_All.txt'
df = pd.read_csv(M_file, sep='\t')
df_all = pd.read_csv(MA_file, sep='\t')

# Reduce DataFrame based on 'Category column' with Cat_input
Cat_input = 'KEGG' ### Decide which Category to use
df = DF_Reduce(Cat_input)

# Add a 'Gene Ratio'(Intersection size / Category size) column. !!!First row will be empty (NaN)!!!
df['Intersection size'] = Tf_float('Intersection size')
df['Category size'] = Tf_float('Category size')
df['Gene ratio'] = df['Intersection size'][1:] / df['Category size'][1:]
'''This df is ready for plot drawing'''

'''Let's compare 'Category value' names back to the original data,
to filter out more specific targets.'''
# Reduce df_all to only one column with name Cat_input, excluding first row
df_all_reduced = df_all[Cat_input][1:]
df_all_reduced.dropna(inplace=True) # Drop the rows with (NaN)

## Create 2 txt files to compare
df.to_csv('df_KEGG.txt', index=False, sep='\t')
#df_all_reduced.to_csv('df_all_GOMF.txt', index=False, sep='\t')

'''Read through each row, and compare the last 3 items
create a list of matched numbers of rows
'''
#Match = [] # Create a list of matched row numbers (first row is 0)
#def Comp_df_full():
#    global Match
#    for i in df_all_reduced: 
#        Temp = [] # Create a list and put each row of selected 'Cat_input' in
#        Temp = i.split(';')
#        for i, v in enumerate(df['Category value']): # i=index, v=value in this for loop, for each row of v, compare it to the list 'Temp'
#            if len(Temp) >= 3: # if the list 'Temp' has at least 3 items, compare v to the last 3
#                if v.casefold() == Temp[-1] or v.casefold() == Temp[-2] or v.casefold() == Temp[-3]:
#                    Match.append(i)
#                else:
#                    continue
#            elif len(Temp) >= 2:# if the list 'Temp' has at least 2 items, compare v to the last 2
#                if v.casefold() == Temp[-1] or v.casefold() == Temp[-2]:
#                    Match.append(i)
#                else:
#                    continue
#            elif len(Temp) >= 1:# if the list 'Temp' has at least 1 items, compare v to the last 1
#                if v.casefold() == Temp[-1]:
#                    Match.append(i)
#                else:
#                    continue
#            else:
#                continue
#    Match = sorted(set(Match))
#
#Comp_df_full()
#print(Match)
#'''This is the Matched DataFrame for plot drawing'''
#df = df.iloc[Match]