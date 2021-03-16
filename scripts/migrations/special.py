from openpyxl import load_workbook, Workbook


# data_only flag will only bring in the data and no excel functions
file = load_workbook(filename='AccessLiving.xlsx', data_only=True)

client_sheet = file.active

# This will be a new workbook that we save our corrected values to
workbook = Workbook()
sheet = workbook.active

# Create a hashtable to keep track of clients
clients = {}

template_header = ['ClientID', 'ClientCaseStatus', 'ClientProgramEnrollment', 'ActiveStaff', 'ClientFirstName',
                   'ClientMiddleName',
                   'ClientLastName', 'DateOfBirth', 'Gender', 'Race', 'Ethnicity', 'VeteranStatus', 'ActiveMilitary',
                   'FirstTimeHomebuyer', 'HouseholdSize', 'CountyAmiIncomeLimit', 'HouseholdIncome',
                   'HouseholdIncomeBand',
                   'IntakeDate', 'StreetNumber', 'StreetName', 'ApartmentNumber', 'ClientCity', 'ClientCounty',
                   'ClientState',
                   'ClientZip', 'PrivacyOptOut', 'RuralAreaStatus', 'EnglishProficiencyLevel', 'BillToHud', '8a', '8b',
                   '8c', '8d',
                   '8e', '8f', '8g', '8h', '8i', '9a', '9b', '9c', '9d', '9e', '9f', '10a', '10b', '10c', '10d', '10e',
                   '10f',
                   '10g', '10h', '10i', '10j', '10k', '10l', '10m', 'PhoneNumberMobile', 'PhoneNumberWork',
                   'PhoneNumberHome',
                   'ImmigrationStatus', 'EmailHome', 'EmailWork', 'MaritalStatus', 'Disability', 'HouseholdType',
                   'Education',
                   'ReferralSource', 'LastContact', 'ActiveReportDateHUD', 'CompletedDate', 'InactiveDate', 'item_ID',
                   'Source']


# Fill our clients hash table with every client
for row in client_sheet.iter_rows(min_row=1, values_only=True, min_col=1):
    client_id = row[0]
    # TODO: IF THE HEADER COLUMNS ARE IN DIFFERENT LOCATIONS, UPDATE THE VALUES FOR THE CLIENT!!!!!
    # This client matches our Template DO NOT CHANGE end up creating multiple
    # clients for each different cms we are importing.
    client = {
      'clientId': client_id,
      'ClientCaseStatus': None,
      'ClientProgramEnrollment': None,
      'ActiveStaff': None,
      'ClientFirstName': None,
      'ClientMiddleName': None,
      'ClientLastName': None,
      'DateOfBirth': None,
      'Gender': None,
      'Race': None,
      'Ethnicity': None,
      'VeteranStatus': None,
      'ActiveMilitary': None,
      'FirstTimeHomebuyer': None,
      'HouseholdSize': None,
      'CountyAmiIncomeLimit': None,
      'HouseholdIncome': None,
      'HouseholdIncomeBand': None,
      'IntakeDate': None,
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
      'EmailHome': None,
      'EmailWork': None,
      'MaritalStatus': None,
      'Disability': None,
      'HouseholdType': None,
      'Education': None,
      'ReferralSource': None,
      'LastContact': None,
      'ActiveReportDateHUD': None,
      'CompletedDate': None,
      'InactiveDate': None,
      'Item_id': None,
      'Source': None
    }
    clients[client_id] = client

# Append our proper header to the new worksheet
sheet.append(template_header)
sheet.title = 'Clients'

# Add each client to the new spreadsheet
for client in clients:
    client_list = [v for k, v in clients[client].items()]

    # Add client to the worksheet
    sheet.append(client_list)

# Save the worksheet when all is complete
outputFileName = "AccessLiving_modified.xlsx"
workbook.save(filename=outputFileName)
