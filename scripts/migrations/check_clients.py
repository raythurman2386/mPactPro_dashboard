import csv
import re
from utils import get_length, options, validate_dates

def check_clients(masterFile, outputFileName, length):
    # Work with the masterfile
    with open(masterFile) as master, open(outputFileName, 'w') as outfile:
        r = csv.reader(master)
        w = csv.writer(outfile)

        # Skip the old header
        # r.next()

        # Write new header
        # With header names to match MSSQL Server
        # w.writerow(['ClientID', 'ClientCaseStatus', 'ClientProgramEnrollment', 'ActiveStaff', 'ClientFirstName', 'ClientMiddleName', 'ClientLastName', 'DateOfBirth', 'Gender', 'Race', 'Ethnicity', 'VeteranStatus', 'ActiveMilitary', 'FirstTimeHomebuyer', 'HouseholdSize', 'CountyAmiIncomeLimit', 'HouseholdIncome', 'HouseholdIncomeBand', 'IntakeDate', 'StreetNumber', 'StreetName', 'ApartmentNumber', 'ClientCity', 'ClientCounty', 'ClientState', 'ClientZip', 'PrivacyOptOut', 'RuralAreaStatus', 'EnglishProficiencyLevel', 'BillToHud', '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h', '8i', '9a', '9b', '9c', '9d', '9e', '9f', '10a', '10b', '10c', '10d', '10e', '10f', '10g', '10h', '10i', '10j', '10k', '10l', '10m', 'PhoneNumberMobile', 'PhoneNumberWork', 'PhoneNumberHome', 'ImmigrationStatus', 'EmailHome', 'EmailWork', 'MaritalStatus', 'Disability', 'HouseholdType', 'Education', 'ReferalSource', 'LastContact', 'ActiveReportDateHUD', 'CompletedDate', 'InactiveDate'])

        # Writes the remaining rows to the file
        for row in r:
            # Changes to individuals will need done through here
            newRow = []
            # print(type(row[7]))
            # TODO: Look into why dates are acting wonky in Excel
            # Work to find a date work around.

            for item in row:
                # Race items
                if item == 'American Indian/Alaskan Native' or item == 'Native American/American Indian':
                    newItem = options['race']['a']
                    newRow.append(newItem)
                elif item == 'Asian' or item == 'Asian Pacific Islander':
                    newItem = options['race']['b']
                    newRow.append(newItem)
                elif item == 'Black/African American' or item == 'Black/African American & White':
                    newItem = options['race']['c']
                    newRow.append(newItem)
                elif item == 'Black/African American & White':
                    newItem = options['race']['h']
                    newRow.append(newItem)
                elif item == 'White' or item == 'White/Caucasian':
                    newItem = options['race']['e']
                    newRow.append(newItem)
                elif item == 'Other Multiple Race' or item == 'Other' or item == 'Multi-Race':
                    newItem = options['race']['j']
                    newRow.append(newItem)
                elif item == 'Not Reported':
                    newItem = options['race']['k']
                    newRow.append(newItem)

                # Ethnicity Items
                elif item == 'Hispanic' or item == 'Hispanic or Latino' or item == 'Hispanic/Latino':
                    newItem = options['ethnicity']['a']
                    newRow.append(newItem)
                elif item == 'Not Hispanic' or item == 'Not Hispanic or Latino':
                    newItem = options['ethnicity']['b']
                    newRow.append(newItem)
                elif item == 'Prefer Not to Answer':
                    newItem = options['ethnicity']['c']

                # Income Band Items
                elif item == 'HUD Adj: Extremely Low (0-30%)' or item == '<30%':
                    newItem = options['incomeBand']['a']
                    newRow.append(newItem)
                elif item == 'HUD Adj: Very Low (31-50%)' or item == '30-49%':
                    newItem = options['incomeBand']['b']
                    newRow.append(newItem)
                elif item == 'HUD Adj: Low (51-80%)' or item == '50-79%':
                    newItem = options['incomeBand']['c']
                    newRow.append(newItem)
                elif item == 'HUD Adj: (81-100%)' or item == '80-100%':
                    newItem = options['incomeBand']['d']
                    newRow.append(newItem)
                elif item == 'HUD Adj: Over (100%)' or item == '>120%' or item == '100%-120%':
                    newItem = options['incomeBand']['e']
                    newRow.append(newItem)
                elif item == 'Check required fields--Income level, MSA, Household size.':
                    newItem = options['incomeBand']['f']
                    newRow.append(newItem)

                # Eng Proficiency
                elif item == 'Is English proficient' or item == 'English':
                    newItem = options['englishProficiency'][1]
                    newRow.append(newItem)
                elif item == 'Is not English proficient':
                    newItem = options['englishProficiency'][0]
                    newRow.append(newItem)
                elif item == 'Chose not to respond':
                    newItem = options['englishProficiency'][2]
                    newRow.append(newItem)

                # Rural Status
                elif item == 'Household lives in a rural area' or item == 'Household Lives in a Rural Area':
                    newItem = options['ruralStatus'][0]
                    newRow.append(newItem)
                elif item == 'Household does not live in a rural area' or item == 'Household Does Not Live in a Rural Area':
                    newItem = options['ruralStatus'][1]
                    newRow.append(newItem)

                # Client Case Status
                elif item == 'In-Process':
                    newItem = options['status'][1]
                    newRow.append(newItem)
                elif item == 'Suspended':
                    newItem = options['status'][4]
                    newRow.append(newItem)
                elif item == 'Fulfilled':
                    newItem = options['status'][2]
                    newRow.append(newItem)

                # Client Program Enrollment
                elif item == 'Education':
                    newItem = options['programEnrollment'][5]
                    newRow.append(newItem)
                elif item == 'Mortgage Default/Early Delinquency':
                    newItem = options['programEnrollment'][1]
                    newRow.append(newItem)
                elif item == 'Financial Capability Counseling':
                    newItem = options['programEnrollment'][5]
                    newRow.append(newItem)

                # check for dates
                elif re.search(r'\d{1,2}(?P<delim>[.\-/])\d{1,2}(?P=delim)\d{1,4}', item):
                    newItem = validate_dates(item)
                    newRow.append(newItem)
                else:
                    newRow.append(item)
                
            # This will be a better way in the future to do all of this
            # Right now this just overwrites race to the proper item
            if newRow[9] == 'c. Chose not to respond':
                newRow[9] = options['race']['k']

            w.writerow(newRow)


    # Check length of copy
    copyCount = get_length(outputFileName)

    if length == copyCount:
        return "Successful"
    else:
        return "There has been an error"