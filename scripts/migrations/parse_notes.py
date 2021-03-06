from openpyxl import load_workbook
from utils import correct_date

# This is the file that will be corrected
# masterFile = sys.argv[1]

# This is the file that will be getting corrected
# file = load_workbook(filename=masterFile, data_only=True)

# case_sheet = file.active

# This will be a new workbook that we save our corrected values to
workbook = load_workbook(filename='access living/client notes.xlsx', data_only=True)
new_wb = load_workbook(filename='test_modified.xlsx')
sheet = workbook.active
new_sheet = new_wb.create_sheet('Note')
client_sheet = new_wb['Clients']

# Create a hashtable to keep track of cases
notes = {}

template_header = ['ClientID', 'ClientFirstName', 'ClientLastName', 'Duration', 'NoteDate', 'Counselor', 'NoteText']


# Grab the names of the clients from the main sheet in the template
clients = {}
for row in client_sheet.iter_rows(min_row=1, min_col=1, values_only=True):
    client_id = row[0]
    client = {
        'client_id': client_id,
        'first': row[4],
        'last': row[6]
    }
    clients[client_id] = client

# Fill our clients hash table with every client
for row in sheet.iter_rows(min_row=2, values_only=True, min_col=1):
    # TODO: IF THE HEADER COLUMNS ARE IN DIFFERENT LOCATIONS, UPDATE THE VALUES FOR THE CLIENT!!!!!
    note_id = row[0]
    client_id = row[1]
    note = {
        'client_id': client_id,
        'first_name': clients[client_id]["first"],
        'last_name': clients[client_id]["last"],
        'duration': None,
        'date_start': row[2],
        'counselor_name': None,
        'notes': row[3],
    }
    # Save the client by the ID for easy Access
    notes[note_id] = note

# Append our proper header to the new worksheet
new_sheet.append(template_header)
new_sheet.title = 'Note'

# Add each client to the new spreadsheet
for note in notes:
    note_list = [v for k, v in notes[note].items()]

    # Add corrected client to the worksheet
    new_sheet.append(note_list)

# Save the worksheet when all is complete
new_wb.save(filename='test_modified-notes.xlsx')
