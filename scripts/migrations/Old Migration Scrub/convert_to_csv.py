import pandas as pd
import os
import sys

masterFile = sys.argv[1]

df = pd.read_excel(masterFile, sheet_name=None)

for key in df.keys():
    df[key].to_csv('{}_{}.csv'.format(key.strip(), os.path.splitext(masterFile)[0]))