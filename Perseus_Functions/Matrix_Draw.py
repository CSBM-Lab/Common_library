'''Based on Perseus v1.6.15.0
Draw a dot plot with enrichment analysis Matrix
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''Transform DataFrame x='column name' from string into float, excluding first row'''
def Tf_float(x):
    x = pd.to_numeric(df[x][1:], downcast='float')
    return x

'''Put DataFrame column 'x' into a list, excluding first row'''
def DF_list(x):
    x = df[x][1:].to_list()
    return x

'''Reduce DataFrame based on 'Category column' with value x'''
def DF_Reduce(x):
    df_filtered = df.loc[df['Category column'] == x]
    return df_filtered

# Read Matrix text file into pandas DataFrame
M_name = 'Matrix_162.txt'
MA_name = 'Matrix_All.txt'
df = pd.read_csv(M_name, sep='\t')
df_all = pd.read_csv(MA_name, sep='\t')

# Reduce DataFrame based on 'Category column' with Cat_input
Cat_input = 'GOBP' ### Decide which Category to use
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

## Create 2 txt files to compare
#df['Category value'].to_csv('df_GOBP.txt', index=False, sep='\t')
#df_all_reduced.to_csv('df_all_GOBP.txt', index=False, sep='\t')

'''Read through each row, and compare the last 3 items
create a list of matched numbers of rows
'''
Match = [] # Create a list of matched row numbers (first row is 0)
def Comp_df_full():
    global Match
    for i in df_all_reduced:
        if type(i) == str: # Only work on rows with strings
            Temp = [] # Create a list and put each row of selected 'Cat_input' in
            Temp = i.split(';')
            for i, v in enumerate(df['Category value']): # i=index, v=value in this for loop, for each row of v, compare it to the list 'Temp'
                if len(Temp) >= 3: # if the list 'Temp' has at least 3 items, compare v to the last 3
                    if v.casefold() == Temp[-1] or v.casefold() == Temp[-2] or v.casefold() == Temp[-3]:
                        Match.append(i)
                    else:
                        continue
                elif len(Temp) >= 2:# if the list 'Temp' has at least 2 items, compare v to the last 2
                    if v.casefold() == Temp[-1] or v.casefold() == Temp[-2]:
                        Match.append(i)
                    else:
                        continue
                elif len(Temp) >= 1:# if the list 'Temp' has at least 1 items, compare v to the last 1
                    if v.casefold() == Temp[-1]:
                        Match.append(i)
                    else:
                        continue
                else:
                    continue
        else:
            continue
    Match = sorted(set(Match))

#Comp_df_full()

'''This is the Matched DataFrame for plot drawing'''
#df = df.iloc[Match]

'''Let's begin to draw the plot'''
# Plot parameters from user
x_input = 'Enrichment factor'
y_input = 'Category value'
c_input = 'Benj. Hoch. FDR'
s_input = 'Intersection size' ### 'Gene ratio' or 'Intersection size'(gene counts) remember to change 'M_size'
Title = ''
x_label = 'Enrichment factor'
y_label = 'Function'

# Transform string into float and modify marker size
M_size = 1 ### 500 for 'Gene ratio', 1 for 'Intersection size'
df[c_input] = Tf_float(c_input)
df[s_input] = M_size * Tf_float(s_input)

# Make data into a list (not necessary for x and y)
x = DF_list(x_input)
y = DF_list(y_input)
c = DF_list(c_input)
s = DF_list(s_input)

# Draw the scatter plot
fig, ax = plt.subplots(figsize=(4, 4)) ### Decide plot size
sc = ax.scatter(x, y, s, c, cmap='coolwarm')
ax.invert_xaxis()

# Set plot margins, Title and labels
ax.margins(0.05, 0.05) ### Decide plot margins
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.set_title(Title)
ax.set_xticks([0, 1, 2, 3])

# To specify the number of ticks on X axis
ax.xaxis.set_major_locator(plt.MaxNLocator(5))

# Add a colorbar
cbar = fig.colorbar(sc, anchor=(0, 0), shrink=0.4)
cbar.ax.set_title('FDR', fontdict = {'size':8})

''' Set legend_values from the list 's', 
 divide the list into 5 groups, 
 and grab the last 5 groups' first item '''
legend_values = np.sort(s)[::len(s)//5][-5:]
#print(legend_values)

# Get the bounds of colorbar axis
xmin, ymin, dx, dy = cbar.ax.get_position().bounds

# Setup new axis for the size chart
xmin -= 0.025
ymin = 0.5
dx -= 0.05
dy = dy
sax = fig.add_axes([xmin, ymin, dx, dy], frame_on=False, ymargin=0.15)

# Plot legend size entries onto this axis
x = [0]*len(legend_values)
y = range(len(legend_values))
sizes = legend_values
sax.scatter(x, y, s = sizes, c = 'black', edgecolors = 'none', marker = 'o')

# Decide size chart title
if s_input == 'Intersection size':
    sc_title = 'Gene counts'
elif s_input == 'Gene ratio':
    sc_title = 'Gene ratio'

# Add y axis labels and remove x ticks
sax.yaxis.set_label_position("right")
sax.yaxis.tick_right()
sax.set_yticks(y)
sax.set_yticklabels(np.round_(legend_values / M_size, decimals=2), fontdict = {'size':8})
sax.set_title(sc_title, loc='left', fontdict = {'size':8})
sax.set_xticks([]) # Set xticks to empty
sax.tick_params(axis='both', which='both', length=0) # Set ticks length to 0 in order to not show

# remove spines
for pos in ['right', 'top', 'bottom', 'left']:
    sax.spines[pos].set_visible(False)


# plt.tight_layout()
plt.savefig('DotPlot_GO.png',bbox_inches='tight')
#plt.show()

### Output filtered data
#df.at[0, 'Gene ratio'] = 'N' # Give Gene ratio Numeric type
