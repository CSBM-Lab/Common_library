"""
Tools for file management.
"""
import sys
import csv
from pathlib import Path
import pandas as pd
from utilities import create_folder, text_color, read_df


###=== Imput parameters ===###
# (Required) Project name.
project_name = "002_vcf" # "001_aging_mice"
# (Required) Function of this program, "dataframe" or "readlines"
# "dataframe" mode can ignore the first n rows with "skiprows".
# "readlines" mode can skip the information rows with specific markers at the start, then add those lines back before saving to file.
mode = "readlines" # "dataframe"  # "readlines"

### Settings for both modes.
# (Required) Path to input file.
file_path = "D:/Repositories/Common_library/data/test_output_grch38.txt"
# (Optional)(For input file) Character or regex pattern to treat as the delimiter, defaults to '\t'.
delimiter_in = '\t'
# (Required) Path to output folder.
out_folder_path = "D:/Repositories/Common_library/analysis"
# (Required) Output file name.
out_file_name = "test_output_grch38.txt"
# (Required)(For output file) Character or regex pattern to treat as the delimiter, defaults to '\t'.
delimiter_out = '\t'

### Settings for "dataframe" mode.
# (Optional) Sheet name for excel files, defaults to None.
sheet_name = "STable1"
# (Optional) Row number(s) containing column labels and marking the start of the data (zero-indexed), defaults to 0.  
header = 0
# (Optional) Column(s) to use as row label(s), denoted either by column labels or column indices, defaults to None.
index_col = None
# (Optional) Subset of columns to select, denoted either by column labels or column indices, defaults to None.
usecols = None
# (Optional) Rows to skip above the table, defaults to None.
skiprows = 1

### Settings for "readlines" mode.
# (Required) Markers for information rows.
marker_info = "##"
# {Optional} Markers for table header row(s), defaults to None.
# If set to None, the next row after information rows will be considered header.
marker_header = "#"  # None
# (Optional) Reinsert the information rows or not, defaults to False.
reinsert = False




###=== Program execution ===###
# Input file path.
input_file = Path(file_path)
# Output folder path.
out_folder_path = Path(out_folder_path)
output_folder = create_folder(project_name,
                              out_folder_path,
                              verbose=True)

### DataFrame mode.
if mode == 'dataframe':
    print(f"Program mode is: {text_color(mode, color='bright_magenta')}")
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

elif mode == "readlines":
    print(f"Program mode is: {text_color(mode, color='bright_magenta')}")
    with open(input_file, 'r') as file:
        line = csv.reader(file, delimiter=delimiter_in)
        count = 0
        # Save info_rows for later reinsert.
        if reinsert:
            info_rows = []
        for row in line:
            ## Rows with informations with markers.
            if row[0].startswith(marker_info):
                if reinsert:
                    info_rows += row
                count += 1
            ## Header Row with markers.
            elif marker_header:
                if row[0].startswith(marker_header):
                    header = row
            # The table content.
            else:    
                print(row)

        print(f"Information rows count: {count}")
        print(header)

        # For later write to output file.
        if reinsert:
            print(info_rows)
else:
    message = "Wrong mode."
    check_highlight = "mode setting"
    input_para = "Input parameters section."
    print(f"{text_color('Error', color='bright_red')}: "
              f"{message} Please check "
              f"{text_color(check_highlight, color='bright_blue')} "
              f"of the {text_color(input_para, color='bright_green')}.")
    if exit:
        sys.exit()