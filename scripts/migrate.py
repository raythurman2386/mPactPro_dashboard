import csv
import fileinput
import re
import os
import sys


# Helper fn to get length of files
def get_length(i):
    count = 0
    with open(i) as f:
        r = csv.reader(f)

        for row in r:
            count += 1
    
    return count


# Get Files
masterFile = sys.argv[1]
outputFileName = os.path.splitext(masterFile)[0] + "_modified.csv"

# Track the initial length of the master file
initialLength = get_length(masterFile)

# Work with the masterfile
with open(masterFile) as master, open(outputFileName, 'w') as outfile:
    r = csv.reader(master)
    w = csv.writer(outfile)

    # Skip the old header
    r.next()

    # Write new header
    # With header names to match MSSQL Server
    w.writerow(['ClientID', 'ClientCaseStatus', 'ClientProgramEnrollment', 'ActiveStaff', 'ClientFirstName', 'ClientMiddleName', 'ClientLastName', 'DateOfBirth', 'Gender', 'Race', 'Ethnicity', 'VeteranStatus', 'ActiveMilitary', 'FirstTimeHomebuyer', 'HouseholdSize', 'CountyAmiIncomeLimit', 'HouseholdIncome', 'HouseholdIncomeBand', 'IntakeDate', 'StreetNumber', 'StreetName', 'ApartmentNumber', 'ClientCity', 'ClientCounty', 'ClientState', 'ClientZip', 'PrivacyOptOut', 'RuralAreaStatus', 'EnglishProficiencyLevel', 'BillToHud', '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h', '8i', '9a', '9b', '9c', '9d', '9e', '9f', '10a', '10b', '10c', '10d', '10e', '10f', '10g', '10h', '10i', '10j', '10k', '10l', '10m', 'PhoneNumberMobile', 'PhoneNumberWork', 'PhoneNumberHome', 'ImmigrationStatus', 'EmailHome', 'EmailWork', 'MaritalStatus', 'Disability', 'HouseholdType', 'Education', 'ReferalSource', 'LastContact', 'ActiveReportDateHUD', 'CompletedDate', 'InactiveDate'])

    # Writes the remaining rows to the file
    for row in r:
        # Changes to individuals will need done through here
        newRow = []

        for item in row:
            if item == 'American Indian/Alaskan Native':
                newItem = 'a. American Indian/Alaskan Native'
                newRow.append(newItem)
            elif item == 'Asian':
                newItem = 'b. Asian'
                newRow.append(newItem)
            elif item == 'Black/African American' or item == 'Black/African American & White':
                newItem = 'c. Black or African American'
                newRow.append(newItem)
            elif item == 'White':
                newItem = 'e. White'
                newRow.append(newItem)
            elif item == 'Other Multiple Race':
                newItem = 'j. Other Multiple Race'
                newRow.append(newItem)
            elif item == 'Hispanic':
                newItem = 'a. Hispanic'
                newRow.append(newItem)
            elif item == 'Not Hispanic':
                newItem = 'b. Not Hispanic'
                newRow.append(newItem)
            elif item == 'HUD Adj: Extremely Low (0-30%)':
                newItem = '1. Below 30% of AMI'
                newRow.append(newItem)
            elif item == 'HUD Adj: Very Low (31-50%)':
                newItem = '2. 30% - 49% of AMI'
                newRow.append(newItem)
            elif item == 'HUD Adj: Low (51-80%)':
                newItem = '3. 50% - 79% of AMI'
                newRow.append(newItem)
            elif item == 'HUD Adj: (81-100%)':
                newItem = '4. 80% - 100% of AMI'
                newRow.append(newItem)
            elif item == 'HUD Adj: Over (100%)':
                newItem = '5. 101% - 120% of AMI'
                newRow.append(newItem)
            elif item == 'Check required fields--Income level, MSA, Household size.':
                newItem = '6. Chose not to respond'
                newRow.append(newItem)
            elif item == 'Is English proficient':
                newItem = 'b. Household is not Limited English Proficient'
                newRow.append(newItem)
            elif item == 'Is not English proficient':
                newItem = 'a. Household is Limited English Proficient'
                newRow.append(newItem)
            elif item == 'Chose not to respond':
                newItem = 'c. Chose not to respond'
                newRow.append(newItem)
            elif item == 'Household lives in a rural area':
                newItem = 'a. Household lives in a rural area'
                newRow.append(newItem)
            elif item == 'Household does not live in a rural area':
                newItem = 'b. Household does not live in a rural area'
                newRow.append(newItem)
            else:
                newRow.append(item)
            
        # This will be a better way in the future to do all of this
        # Right now this just overwrites race to the proper item
        if newRow[9] == 'c. Chose not to respond':
            newRow[9] = 'k. Chose not to respond'

        w.writerow(newRow)


# Check length of copy
copyCount = get_length(outputFileName)

if initialLength == copyCount:
    print("Successful")
else:
    print("There has been an error")
