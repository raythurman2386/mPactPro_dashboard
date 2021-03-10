from openpyxl import load_workbook, Workbook
from correct_client import fix_client_data
from utils import correct_date
import sys
import os

# This is the file that will be corrected
masterFile = sys.argv[1]

# This is the file that will be getting corrected
# data_only flag will only bring in the data and no excel functions
file = load_workbook(filename=masterFile, data_only=True)

# File to act as simple dp to keep track of count var
# count var will be used for the itemID col
try:
    count_file = open("count.txt", "r")
    count = int(count_file.readlines()[-1])
    count_file.close()
except ValueError:
    count = 1
except IndexError:
    count = 1


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
                   'ReferralSource', 'LastContact', 'ActiveReportDateHUD', 'CompletedDate', 'InactiveDate', 'ItemID',
                   'Source']


# Fill our clients hash table with every client
for row in client_sheet.iter_rows(min_row=2, values_only=True, min_col=1):
    client_id = row[0]
    # Uncomment if the name needs split to first and last
    # if row[3] is not None:
    #     split_name = row[3].split(' ')
    # TODO: IF THE HEADER COLUMNS ARE IN DIFFERENT LOCATIONS, UPDATE THE VALUES FOR THE CLIENT!!!!!
    # This client matches our Template DO NOT CHANGE end up creating multiple
    # clients for each different cms we are importing.
    client = {
      'clientId': client_id,
      'ClientCaseStatus': row[1],
      'ClientProgramEnrollment': row[2],
      'ActiveStaff': row[3],
      'ClientFirstName': row[4],
      'ClientMiddleName': row[5],
      'ClientLastName': row[6],
      'DateOfBirth': correct_date(row[7]),
      'Gender': row[8],
      'Race': row[9],
      'Ethnicity': row[10],
      'VeteranStatus': row[11],
      'ActiveMilitary': row[12],
      'FirstTimeHomebuyer': row[13],
      'HouseholdSize': row[14],
      'CountyAmiIncomeLimit': row[15],
      'HouseholdIncome': row[16],
      'HouseholdIncomeBand': row[17],
      'IntakeDate': correct_date(row[18]),
      'StreetNumber': row[19],
      'StreetName': row[20],
      'ApartmentNumber': row[21],
      'ClientCity': row[22],
      'ClientCounty': None,
      'ClientState': row[24],
      'ClientZip': row[25],
      'PrivacyOptOut': row[26],
      'RuralAreaStatus': row[27],
      'EnglishProficiencyLevel': row[28],
      'BillToHud': row[29],
      '8a': correct_date(row[30]),
      '8b': correct_date(row[31]),
      '8c': correct_date(row[32]),
      '8d': correct_date(row[33]),
      '8e': correct_date(row[34]),
      '8f': correct_date(row[35]),
      '8g': correct_date(row[36]),
      '8h': correct_date(row[37]),
      '8i': correct_date(row[38]),
      '9a': correct_date(row[39]),
      '9b': correct_date(row[40]),
      '9c': correct_date(row[41]),
      '9d': correct_date(row[42]),
      '9e': correct_date(row[43]),
      '9f': correct_date(row[44]),
      '10a': correct_date(row[45]),
      '10b': correct_date(row[46]),
      '10c': correct_date(row[47]),
      '10d': correct_date(row[48]),
      '10e': correct_date(row[49]),
      '10f': correct_date(row[50]),
      '10g': correct_date(row[51]),
      '10h': correct_date(row[52]),
      '10i': correct_date(row[53]),
      '10j': correct_date(row[54]),
      '10k': correct_date(row[55]),
      '10l': correct_date(row[56]),
      '10m': correct_date(row[57]),
      'PhoneNumberMobile': row[58],
      'PhoneNumberWork': row[59],
      'PhoneNumberHome': row[60],
      'ImmigrationStatus': row[61],
      'EmailHome': row[62],
      'EmailWork': row[63],
      'MaritalStatus': row[64],
      'Disability': row[65],
      'HouseholdType': row[66],
      'Education': row[67],
      'ReferralSource': row[68],
      'LastContact': correct_date(row[69]),
      'ActiveReportDateHUD': correct_date(row[70]),
      'CompletedDate': correct_date(row[71]),
      'InactiveDate': row[72],
      'Item_id': count,
      'Source': os.path.splitext(masterFile)[0]
    }
    # Save the client by the ID for easy Access
    clients[client_id] = client
    count += 1

# Append our proper header to the new worksheet
sheet.append(template_header)
sheet.title = 'Clients'

# Add each client to the new spreadsheet
for client in clients:
    client_list = [v for k, v in clients[client].items()]

    # TODO: Fix client data to match our requirements
    # If the address needs split, pass True along with the client list
    # If correcting address use this variable instead
    # corrected_client = fix_client_data(client_list, True)
    # If the address does not need split this is the one to use
    corrected_client = fix_client_data(client_list)

    # Add corrected client to the worksheet
    sheet.append(corrected_client)

# Save the worksheet when all is complete
outputFileName = os.path.splitext(masterFile)[0] + "_modified.xlsx"
workbook.save(filename=outputFileName)

# Save the count var for the next agency
count_file = open('count.txt', 'w')
count_file.write(str(count))
count_file.close()
