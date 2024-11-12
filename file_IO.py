"""
Tools for file management.
"""
from pathlib import Path
import pandas as pd
from utilities import create_folder, text_color, read_df


###=== Imput parameters ===###
# (Optional) Project name.
project_name = "006_aging_mice"
# (Required) Path to input file.
file_path = "C:/Repositories/Common_library/data/mmc2.xlsx"
# (Optional) Sheet name for excel files, defaults to None.
sheet_name = "STable1"
# (Optional)(For input file) Character or regex pattern to treat as the delimiter, defaults to '\t'.
delimiter_in = '\t'
# (Optional) Row number(s) containing column labels and marking the start of the data (zero-indexed), defaults to 0.  
header = 0
# (Optional) Column(s) to use as row label(s), denoted either by column labels or column indices, defaults to None.
index_col = None
# (Optional) Subset of columns to select, denoted either by column labels or column indices, defaults to None.
usecols = None
# (Optional) Rows to skip above the table, defaults to None.
skiprows = 1

# (Required) Path to output folder.
out_folder_path = "C:/Repositories/Common_library/data"
# (Required) Output file name.
out_file_name = "proteome_aging_mice.txt"
# (Required)(For output file) Character or regex pattern to treat as the delimiter, defaults to '\t'.
delimiter_out = '\t'


###=== Program execution ===###
# Input file path.
input_file = Path(file_path)
# Output folder path.
out_folder_path = Path(out_folder_path)
output_folder = create_folder(project_name,
                              out_folder_path,
                              verbose=True)

# Read DataFrame from the file.
df = read_df(input_file,
             sheet_name=sheet_name,
             delimiter=delimiter_in,
             header=header,
             index_col=index_col,
             usecols=usecols,
             skiprows=skiprows)
print(df)

print(f"Project name: {text_color(project_name, color='bright_yellow')}")
print(f"The input file: {text_color(input_file, 'bright_yellow')}")
print(f"Output files will be saved in: {text_color(output_folder, 'gray')}")
print(f'The shape of whole matrix: {df.shape}')


# Save to file.
df.to_csv(output_folder / out_file_name,
          index=False,
          sep=delimiter_out)
file_path = text_color(output_folder / out_file_name, color='magenta')
print(f'The output file saved to: {file_path}')