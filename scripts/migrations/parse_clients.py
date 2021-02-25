from openpyxl import load_workbook, Workbook
from correct_client import fix_client_data
import sys
import os

# This is the file that will be corrected
masterFile = sys.argv[1]

# This is the file that will be getting corrected
# data_only flag will only bring in the data and no excel functions
file = load_workbook(filename=masterFile, data_only=True)

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
                   'ReferralSource', 'LastContact', 'ActiveReportDateHUD', 'CompletedDate', 'InactiveDate']


# Fill our clients hash table with every client
for row in client_sheet.iter_rows(min_row=23, values_only=True, min_col=2):
    client_id = row[0]
    # Uncomment if the name needs split to first and last
    # if row[3] is not None:
    #     split_name = row[3].split(' ')
    # TODO: IF THE HEADER COLUMNS ARE IN DIFFERENT LOCATIONS, UPDATE THE VALUES FOR THE CLIENT!!!!!
    client = {
      'clientId': client_id,
      'ClientCaseStatus': row[1],
      'ClientProgramEnrollment': row[2],
      'ActiveStaff': None,
      'ClientFirstName': split_name[0],
      'ClientMiddleName': None,
      'ClientLastName': split_name[1],
      'DateOfBirth': None,
      'Gender': row[4],
      'Race': row[5],
      'Ethnicity': row[6],
      'VeteranStatus': row[7],
      'ActiveMilitary': None,
      'FirstTimeHomebuyer': row[8],
      'HouseholdSize': row[9],
      'CountyAmiIncomeLimit': row[10],
      'HouseholdIncome': row[11],
      'HouseholdIncomeBand': row[12],
      'IntakeDate': row[13],
      'StreetNumber': None,
      'StreetName': row[14],
      'ApartmentNumber': None,
      'ClientCity': row[15],
      'ClientCounty': row[16],
      'ClientState': row[17],
      'ClientZip': row[18],
      'PrivacyOptOut': None,
      'RuralAreaStatus': row[19],
      'EnglishProficiencyLevel': row[20],
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
      'MaritalStatus': row[21],
      'Disability': row[22],
      'HouseholdType': row[23],
      'Education': row[24],
      'ReferralSource': row[25],
      'LastContact': row[26],
      'ActiveReportDateHUD': None,
      'CompletedDate': row[27],
      'InactiveDate': None
    }
    # Save the client by the ID for easy Access
    clients[client_id] = client

# Append our proper header to the new worksheet
sheet.append(template_header)
sheet.title = 'Clients'

# Add each client to the new spreadsheet
for client in clients:
    client_list = [v for k, v in clients[client].items()]

    # TODO: Fix client data to match our requirements
    # If the address needs split, pass True along with the client list
    # If correcting address use this variable instead
    corrected_client = fix_client_data(client_list, True)
    # If the address does not need split this is the one to use
    # corrected_client = fix_client_data(client_list)

    # Add corrected client to the worksheet
    sheet.append(corrected_client)

# Save the worksheet when all is complete
outputFileName = os.path.splitext(masterFile)[0] + "_modified.xlsx"
workbook.save(filename=outputFileName)
