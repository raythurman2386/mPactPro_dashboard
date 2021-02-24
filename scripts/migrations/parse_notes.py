from openpyxl import load_workbook, Workbook
from correct_client import fix_data
import sys
import os

# This is the file that will be corrected
# masterFile = sys.argv[1]

# This is the file that will be getting corrected
# file = load_workbook(filename=masterFile, data_only=True)

# case_sheet = file.active

# This will be a new workbook that we save our corrected values to
workbook = load_workbook(filename='HOI_modified.xlsx', data_only=True)
sheet = workbook.create_sheet('Note')

# Create a hashtable to keep track of cases
notes = {}

template_header = ['Client ID', 'First Name', 'Last Name', 'Duration', 'Date - start', 'Counselor - name', 'Notes']

# Fill our clients hash table with every client
# for row in case_sheet.iter_rows(min_row=2, values_only=True, min_col=2):
#     client_id = None
#     # TODO: IF THE HEADER COLUMNS ARE IN DIFFERENT LOCATIONS, UPDATE THE VALUES FOR THE CLIENT!!!!!
#     note = {
#         'client_id': client_id,
#         'first_name': None,
#         'last_name': None,
#         'duration': None,
#         'date_start': None,
#         'counselor_name': None,
#         'notes': None,
#     }
#     # Save the client by the ID for easy Access
#     notes[client_id] = note

# Append our proper header to the new worksheet
sheet.append(template_header)
sheet.title = 'Note'

# Add each client to the new spreadsheet
# for note in notes:
# note_list = [v for k, v in notes[client_id].items()]

# TODO: Fix client data to match our requirements
# corrected_note = fix_data(note_list)

# Add corrected client to the worksheet
# sheet.append(corrected_note)

# Save the worksheet when all is complete
workbook.save(filename='HOI_modified_cases.xlsx')
