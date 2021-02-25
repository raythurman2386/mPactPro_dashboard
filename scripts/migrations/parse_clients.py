from openpyxl import load_workbook, Workbook
from tkinter import *
from tkinter import ttk
from correct_client import fix_data
import sys
import os

# This is the file that will be corrected
masterFile = sys.argv[1]

# This is the file that will be getting corrected
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


# **********************************************************************
# Playing around with Tkinter to build a ui for this tool.
# This may or may not need moved from this file.
# Experimenting
# root = Tk()
# root.title('Agency Data Migration Assistant')
#
# mainframe = ttk.Frame(root, padding='3 3 12 12')
# mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)


# **********************************************************************

# Fill our clients hash table with every client
for row in client_sheet.iter_rows(min_row=2, values_only=True, min_col=2):
    client_id = row[60]
    # TODO: IF THE HEADER COLUMNS ARE IN DIFFERENT LOCATIONS, UPDATE THE VALUES FOR THE CLIENT!!!!!
    client = {
      'clientId': client_id,
      'ClientCaseStatus': None,
      'ClientProgramEnrollment': row[2],
      'ActiveStaff': None,
      'ClientFirstName': row[5],
      'ClientMiddleName': None,
      'ClientLastName': row[6],
      'DateOfBirth': row[36],
      'Gender': row[84],
      'Race': row[108],
      'Ethnicity': row[88],
      'VeteranStatus': row[97],
      'ActiveMilitary': None,
      'FirstTimeHomebuyer': row[115],
      'HouseholdSize': None,
      'CountyAmiIncomeLimit': None,
      'HouseholdIncome': row[116],
      'HouseholdIncomeBand': None,
      'IntakeDate': None,
      'StreetNumber': None,
      'StreetName': row[16],
      'ApartmentNumber': None,
      'ClientCity': row[17],
      'ClientCounty': None,
      'ClientState': row[18],
      'ClientZip': row[19],
      'PrivacyOptOut': None,
      'RuralAreaStatus': row[109],
      'EnglishProficiencyLevel': row[75],
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
      'PhoneNumberHome': row[27],
      'ImmigrationStatus': row[59],
      'EmailHome': row[31],
      'EmailWork': None,
      'MaritalStatus': row[92],
      'Disability': row[71],
      'HouseholdType': row[85],
      'Education': row[74],
      'ReferralSource': row[61],
      'LastContact': None,
      'ActiveReportDateHUD': None,
      'CompletedDate': None,
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
    corrected_client = fix_data(client_list)

    # Add corrected client to the worksheet
    sheet.append(corrected_client)

# Save the worksheet when all is complete
outputFileName = os.path.splitext(masterFile)[0] + "_modified.xlsx"
workbook.save(filename=outputFileName)
