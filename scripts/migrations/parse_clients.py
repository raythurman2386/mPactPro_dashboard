import json
from openpyxl import load_workbook, Workbook
from correct_client import fix_data
import sys
import os

# This is the file that will be corrected
# masterFile = sys.argv[1]
masterFile = "AHFFL.xlsx"

# TODO: Swap out hardcoded filename with masterFile
# This is the file that will be getting corrected
file = load_workbook(filename=masterFile, data_only=True)
client_sheet = file.active

# This will be a new workbook that we save our corrected values to
workbook = Workbook()
sheet = workbook.active

# Create a hashtable to keep track of clients
clients = {}

template_header = ['ClientID', 'ClientCaseStatus', 'ClientProgramEnrollment', 'ActiveStaff', 'ClientFirstName', 'ClientMiddleName',
                     'ClientLastName', 'DateOfBirth', 'Gender', 'Race', 'Ethnicity', 'VeteranStatus', 'ActiveMilitary',
                     'FirstTimeHomebuyer', 'HouseholdSize', 'CountyAmiIncomeLimit', 'HouseholdIncome', 'HouseholdIncomeBand',
                     'IntakeDate', 'StreetNumber', 'StreetName', 'ApartmentNumber', 'ClientCity', 'ClientCounty', 'ClientState',
                     'ClientZip', 'PrivacyOptOut', 'RuralAreaStatus', 'EnglishProficiencyLevel', 'BillToHud', '8a', '8b', '8c', '8d',
                     '8e', '8f', '8g', '8h', '8i', '9a', '9b', '9c', '9d', '9e', '9f', '10a', '10b', '10c', '10d', '10e', '10f',
                     '10g', '10h', '10i', '10j', '10k', '10l', '10m', 'PhoneNumberMobile', 'PhoneNumberWork', 'PhoneNumberHome',
                     'ImmigrationStatus', 'EmailHome', 'EmailWork', 'MaritalStatus', 'Disability', 'HouseholdType', 'Education',
                     'ReferralSource', 'LastContact', 'ActiveReportDateHUD', 'CompletedDate', 'InactiveDate']

# Fill our clients hash table with every client
for row in client_sheet.iter_rows(min_row=2, values_only=True, min_col=2):
  client_id = row[0]
  # TODO: IF THE HEADER COLUMNS ARE IN DIFFERENT LOCATIONS, UPDATE THE VALUES FOR THE CLIENT!!!!!
  client = {
    'ClientCaseStatus': row[1],
    'ClientProgramEnrollment': row[2],
    'ActiveStaff': row[3],
    'ClientFirstName': row[4],
    'ClientMiddleName': row[5],
    'ClientLastName': row[6],
    'DateOfBirth': row[7],
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
    'IntakeDate': row[18],
    'StreetNumber': row[19],
    'StreetName': row[20],
    'ApartmentNumber': row[21],
    'ClientCity': row[22],
    'ClientCounty': row[23],
    'ClientState': row[24],
    'ClientZip': row[25],
    'PrivacyOptOut': row[26],
    'RuralAreaStatus': row[27],
    'EnglishProficiencyLevel': row[28],
    'BillToHud': row[29],
    '8a': row[30],
    '8b': row[31],
    '8c': row[32],
    '8d': row[33],
    '8e': row[34],
    '8f': row[35],
    '8g': row[36],
    '8h': row[37],
    '8i': row[38],
    '9a': row[39],
    '9b': row[40],
    '9c': row[41],
    '9d': row[42],
    '9e': row[43],
    '9f': row[44],
    '10a': row[45],
    '10b': row[46],
    '10c': row[47],
    '10d': row[48],
    '10e': row[49],
    '10f': row[50],
    '10g': row[51],
    '10h': row[52],
    '10i': row[53],
    '10j': row[54],
    '10k': row[55],
    '10l': row[56],
    '10m': row[57],
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
    'LastContact': row[69],
    'ActiveReportDateHUD': row[70],
    'CompletedDate': row[71],
    'InactiveDate': row[72]
  }
  clients[client_id] = client

# Append our proper header to the new worksheet
sheet.append(template_header)
sheet.title = 'Clients'

# Add each client to the new spreadsheet
for client in clients:
  client_id = client
  client_list = [v for k, v in clients[client].items()]
  client_list.insert(0, client_id)

  # TODO: Fix client data to match our requirements
  corrected_client = fix_data(client_list)

  # Add corrected client to the worksheet
  sheet.append(corrected_client)

# Save the worksheet when all is complete
outputFileName = os.path.splitext(masterFile)[0] + "_modified.xlsx"
workbook.save(filename=outputFileName)
