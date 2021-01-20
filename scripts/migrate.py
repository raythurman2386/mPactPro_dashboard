import csv
import fileinput
import re
import os
import sys


def get_length(i):
    count = 0
    with open(i) as f:
        r = csv.reader(f)

        for row in r:
            count += 1
    
    return count


masterFile = sys.argv[1]
outputFileName = "hfhm_modified.csv"
initialLength = get_length(masterFile)

with open(masterFile) as master, open(outputFileName, 'w') as outfile:
    r = csv.reader(master)
    w = csv.writer(outfile)

    # Grab the old header
    r.next()

    # Write new header
    # With header names to match MSSQL Server
    w.writerow(['client_id', 'client_case_status', 'client_program_enrollment', 'ActiveStaff', 'ClientFirstName', 'ClientMiddleName', 'ClientLastName', 'DateOfBirth', 'Gender', 'Race', 'Ethnicity', 'VeteranStatus', 'ActiveMilitary', 'FirstTimeHomebuyer', 'HouseholdSize', 'CountyAmiIncomeLimit', 'HouseholdIncome', 'HouseholdIncomeBand', 'IntakeDate', 'StreetNumber', 'StreetName', 'ApartmentNumber', 'ClientCity', 'ClientCounty', 'ClientState', 'ClientZip', 'PrivacyOptOut', 'RuralAreaStatus', 'EnglishProficiencyLevel', 'BillToHud', '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h', '8i', '9a', '9b', '9c', '9d', '9e', '9f', '10a', '10b', '10c', '10d', '10e', '10f', '10g', '10h', '10i', '10j', '10k', '10l', '10m', 'PhoneNumberMobile', 'PhoneNumberWork', 'PhoneNumberHome', 'ImmigrationStatus', 'EmailHome', 'EmailWork', 'MaritalStatus', 'Disability', 'HouseholdType', 'Education', 'ReferalSource', 'LastContact', 'ActiveReportDateHUD', 'CompletedDate', 'InactiveDate'])

    for row in r:
        w.writerow(row)


# Check length of both
with open("hfhmmigrate.csv") as master, open("hfhm_modified.csv") as outfile:
    r = csv.reader(master)
    w = csv.reader(outfile)

    count = get_length("hfhmmigrate.csv")
    copyCount = get_length("hfhm_modified.csv")

    if initialLength == copyCount:
        print("Successful")
    else:
        print("There has been an error")
