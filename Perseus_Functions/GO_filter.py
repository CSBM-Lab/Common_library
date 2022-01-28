import pandas as pd
from goatools import obo_parser

# Read GO term files as csv into df_GO
GO_file = 'df_all_GOMF.txt'
df_GO = pd.read_csv(GO_file)
df_GO.dropna(inplace=True) # Drop the rows with (NaN)

## Create txt files to check
#df_GO.to_csv('df_GO.txt', index=False)

# Use obo_parser to reorganize GO terms
for i in df_GO['GOMF'][0:5]:
    Temp = [] # Create a list and put each row of GO ID in
    Temp = i.split(';')
    levels = {}
    for go in Temp:
        term = obo_parser.GODag('go.obo').query_term(go)
        levels[go] = term.level
    print(levels)
