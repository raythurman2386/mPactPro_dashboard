from openpyxl import load_workbook
from utils import create_workbook

# Load all files here
client_data = load_workbook(filename="access living/client.xlsx", data_only=True)
client_address = load_workbook(filename="access living/client address.xlsx", data_only=True)
client_phone = load_workbook(filename="access living/client phone.xlsx", data_only=True)
person = load_workbook(filename="access living/person.xlsx", data_only=True)
housing_info = load_workbook(filename="access living/housing information.xlsx", data_only=True)
client_notes = load_workbook(filename="access living/client notes.xlsx", data_only=True)

# Dropdown code files
dropdown_codes = load_workbook(filename="access living/dropdown codes.xlsx", data_only=True)
housing_codes = load_workbook(filename="access living/housing dropdown codes.xlsx", data_only=True)

# Create Hash tables for each excel tab
clients = {}
cases = {}
sessions = {}
notes = {}

# *****************************************************************************************
workbook = create_workbook()
template_client_sheet = workbook['Clients']
template_case_sheet = workbook['Case']
template_session_sheet = workbook['Session']
template_note_sheet = workbook['Note']
# *****************************************************************************************

# Start creating initial hash table of clients from the PERSON workbook
for row in person.active.iter_rows(min_row=2, values_only=True, min_col=1):
    client_id = row[0]
    client = {
        'clientId': client_id,
        'ClientCaseStatus': None,
        'ClientProgramEnrollment': None,
        'ActiveStaff': None,
        'ClientFirstName': row[2],
        'ClientMiddleName': row[3],
        'ClientLastName': row[4],
        'DateOfBirth': row[7],
        'Gender': row[6],
        'Race': None,
        'Ethnicity': None,
        'VeteranStatus': None,
        'ActiveMilitary': None,
        'FirstTimeHomebuyer': None,
        'HouseholdSize': None,
        'CountyAmiIncomeLimit': None,
        'HouseholdIncome': None,
        'HouseholdIncomeBand': None,
        'IntakeDate': row[12],
        'StreetNumber': None,
        'StreetName': None,
        'ApartmentNumber': None,
        'ClientCity': None,
        'ClientCounty': None,
        'ClientState': None,
        'ClientZip': None,
        'PrivacyOptOut': None,
        'RuralAreaStatus': None,
        'EnglishProficiencyLevel': None,
        'BillToHud': None,
        '8a': None,
        '8b': None,
        '8c': None,
        '8d': None,
        '8e': None,
        '8f': None,
        '8g': None,
        '8h': None,
        '8i': None,
        '9a': None,
        '9b': None,
        '9c': None,
        '9d': None,
        '9e': None,
        '9f': None,
        '10a': None,
        '10b': None,
        '10c': None,
        '10d': None,
        '10e': None,
        '10f': None,
        '10g': None,
        '10h': None,
        '10i': None,
        '10j': None,
        '10k': None,
        '10l': None,
        '10m': None,
        'PhoneNumberMobile': None,
        'PhoneNumberWork': None,
        'PhoneNumberHome': None,
        'ImmigrationStatus': None,
        'EmailHome': row[9],
        'EmailWork': row[10],
        'MaritalStatus': None,
        'Disability': None,
        'HouseholdType': None,
        'Education': None,
        'ReferralSource': None,
        'LastContact': None,
        'ActiveReportDateHUD': None,
        'CompletedDate': None,
        'InactiveDate': None
    }

    # Save the client by the ID for easy Access
    clients[client_id] = client

# Now that initial clients hashtable is created, go through each open file and fill in client data
for row in client_data.active.iter_rows(min_row=2, min_col=1, values_only=True):
    client_id = row[0]
    try:
        if clients[client_id]:
            clients[client_id]["MaritalStatus"] = row[2]
            clients[client_id]["ReferralSource"] = row[1]
            clients[client_id]["HouseholdSize"] = row[5]
            clients[client_id]["Ethnicity"] = row[6]
            clients[client_id]["Race"] = row[6]
            clients[client_id]["ClientCaseStatus"] = row[19]
    except KeyError:
        pass


for row in client_address.active.iter_rows(min_row=1, min_col=1, values_only=True):
    client_id = row[0]
    try:
        if clients[client_id]:
            clients[client_id]["StreetName"] = row[18]
    except KeyError:
        pass


for row in client_phone.active.iter_rows(min_row=2, min_col=1, values_only=True):
    phone = str(row[3]) + str(row[4])

    client_id = row[0]
    try:
        if clients[client_id]:
            clients[client_id]["PhoneNumberMobile"] = phone
    except KeyError:
        pass


for row in housing_info.active.iter_rows(min_row=2, min_col=1, values_only=True):
    client_id = row[1]
    try:
        if clients[client_id]:
            clients[client_id]["RuralAreaStatus"] = row[30]
            clients[client_id]["EnglishProficiencyLevel"] = row[31]
            clients[client_id]["HouseholdIncomeBand"] = row[49]
    except KeyError:
        pass

# THIS IS DONE LAST FOR THE CLIENT SHEET
# GRAB ALL DATA BEFORE THIS UNLESS TESTING
# Add each client to the new spreadsheet
for client in clients:
    client_list = [v for k, v in clients[client].items()]
    template_client_sheet.append(client_list)

# *****************************************************************************************
# END OF CLIENT TAB DATA

# NOTES TAB
for row in client_notes.active.iter_rows(min_row=2, values_only=True, min_col=1):
    # TODO: IF THE HEADER COLUMNS ARE IN DIFFERENT LOCATIONS, UPDATE THE VALUES FOR THE CLIENT!!!!!
    note_id = row[0]
    client_id = row[1]
    note = {
        'client_id': client_id,
        'first_name': clients[client_id]["ClientFirstName"],
        'last_name': clients[client_id]["ClientLastName"],
        'duration': None,
        'date_start': row[2],
        'counselor_name': None,
        'notes': row[3],
    }
    # Save the client by the ID for easy Access
    notes[note_id] = note


# Add each client to the new spreadsheet
for note in notes:
    note_list = [v for k, v in notes[note].items()]
    # Add corrected client to the worksheet
    template_note_sheet.append(note_list)


# *****************************************************************************************
# Save the worksheet when all is complete
outputFileName = "test_modified.xlsx"
workbook.save(filename=outputFileName)