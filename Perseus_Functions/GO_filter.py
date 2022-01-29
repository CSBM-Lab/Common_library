import pandas as pd
from goatools import obo_parser
from io import StringIO

# Read GO term files as csv into df_GO
GO_file = 'df_GOMF.txt'
df_GO = pd.read_csv(GO_file)
df_GO.dropna(inplace=True) # Drop the rows with (NaN)

## Create txt files to check
#df_GO.to_csv('df_GO.txt', index=False)

# Use obo_parser to reorganize GO terms
def GO_obo(GO):
    output = StringIO()  ### print value to variable instead of printing to file or monitor
    term = obo_parser.GODag('go.obo').query_term(GO)
    print(term.parents, file=output)  ### redirect the output to variable
    data = output.getvalue()  ### get the result of "term" to data, it will change the type of object to string that we can access it
    levels = []
    depths = []
    data = data.split("\n")  ### make each line of output to be a elements of a list
    for go in data:
        go = go.strip()  ### remove the space
        if go.startswith(GO):  ### you can replace 'GO:0048528' to the GO term that you get from your input table
            info = go.split("\t")  ### split the parents information to id, level, depth and name
            if len(info) >= 3:  ### filter out the GO term which has no level information (may be root or no child)
                levels.append(int(info[1].replace('level-', "")))
                depths.append(int(info[2].replace('depth-', "")))
    print(levels)
    print(depths)

for i in df_GO['Category value']:
    GO_obo(i)