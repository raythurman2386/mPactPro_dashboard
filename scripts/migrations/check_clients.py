import csv
import re
from utils import get_length, options, validate_dates

def check_clients(masterFile, outputFileName, length):
    # Work with the masterfile
    with open(masterFile) as master, open(outputFileName, 'w') as outfile:
        r = csv.reader(master)
        w = csv.writer(outfile)

        # Skip the old header
        # next(r)

        # WRITE A NEW HEADER IF NEEDED TO MATCH WHAT IS NEEDED
        # With header names to match MSSQL Server
        # w.writerow(['ClientID', 'ClientCaseStatus', 'ClientProgramEnrollment', 'ActiveStaff', 'ClientFirstName', 'ClientMiddleName', 'ClientLastName', 'DateOfBirth', 'Gender', 'Race', 'Ethnicity', 'VeteranStatus', 'ActiveMilitary', 'FirstTimeHomebuyer', 'HouseholdSize', 'CountyAmiIncomeLimit', 'HouseholdIncome', 'HouseholdIncomeBand', 'IntakeDate', 'StreetNumber', 'StreetName', 'ApartmentNumber', 'ClientCity', 'ClientCounty', 'ClientState', 'ClientZip', 'PrivacyOptOut', 'RuralAreaStatus', 'EnglishProficiencyLevel', 'BillToHud', '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h', '8i', '9a', '9b', '9c', '9d', '9e', '9f', '10a', '10b', '10c', '10d', '10e', '10f', '10g', '10h', '10i', '10j', '10k', '10l', '10m', 'PhoneNumberMobile', 'PhoneNumberWork', 'PhoneNumberHome', 'ImmigrationStatus', 'EmailHome', 'EmailWork', 'MaritalStatus', 'Disability', 'HouseholdType', 'Education', 'ReferalSource', 'LastContact', 'ActiveReportDateHUD', 'CompletedDate', 'InactiveDate'])

        # Writes the remaining rows to the file
        for row in r:
            # Changes to individuals will need done through here
            newRow = []
            # NEED TO FIND BETTER OPTIONS THAN A GIANT FOR LOOP
            # WILL WORK FOR NOW, BUT MAY NEED TO UPDATE FIELDS AS NEW ONES ARISE  
            # THAT THIS ONE DOESN'T CATCH
            for item in row:
                # Race items
                if item == 'American Indian/Alaskan Native' or item == 'Native American/American Indian' or item == 'American Indian or Alaska Native':
                    newItem = options['race']['a']
                    newRow.append(newItem)
                elif item == 'Asian' or item == 'Asian Pacific Islander':
                    newItem = options['race']['b']
                    newRow.append(newItem)
                elif item == 'Black/African American' or item == 'Black or African American':
                    newItem = options['race']['c']
                    newRow.append(newItem)
                elif item == 'Black/African American & White' or item == 'Black or African American AND White':
                    newItem = options['race']['h']
                    newRow.append(newItem)
                elif item == 'White' or item == 'White/Caucasian':
                    newItem = options['race']['e']
                    newRow.append(newItem)
                elif item == 'American Indian AND White':
                    newItem = options['race']['f']
                    newRow.append(newItem)
                elif item == 'Asian AND White':
                    newItem = options['race']['g']
                    newRow.append(newItem)
                elif item == 'Other Multiple Race' or item == 'Multi-Race' or item == 'Other multiple race':
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
                elif item == 'HUD Adj: Extremely Low (0-30%)' or item == '<30%' or item == '< 30% of AMI':
                    newItem = options['incomeBand']['a']
                    newRow.append(newItem)
                elif item == 'HUD Adj: Very Low (31-50%)' or item == '30-49%' or item == '30 - 49% of AMI':
                    newItem = options['incomeBand']['b']
                    newRow.append(newItem)
                elif item == 'HUD Adj: Low (51-80%)' or item == '50-79%' or item == '50 - 79% of AMI':
                    newItem = options['incomeBand']['c']
                    newRow.append(newItem)
                elif item == 'HUD Adj: (81-100%)' or item == '80-100%' or item == '80 - 100% of AMI':
                    newItem = options['incomeBand']['d']
                    newRow.append(newItem)
                elif item == 'HUD Adj: Over (100%)' or item == '>120%' or item == '100%-120%':
                    newItem = options['incomeBand']['e']
                    newRow.append(newItem)
                elif item == 'Check required fields--Income level, MSA, Household size.':
                    newItem = options['incomeBand']['f']
                    newRow.append(newItem)

                # Eng Proficiency
                elif item == 'Is English proficient' or item == 'English' or item == 'Household is Limited English Proficient':
                    newItem = options['englishProficiency'][1]
                    newRow.append(newItem)
                elif item == 'Is not English proficient' or item == 'Household is not Limited English Proficient':
                    newItem = options['englishProficiency'][0]
                    newRow.append(newItem)
                elif item == 'Chose not to respond' or item == 'Chose Not to Respond':
                    newItem = options['englishProficiency'][2]
                    newRow.append(newItem)

                # Rural Status
                elif item == 'Household lives in a rural area' or item == 'Household Lives in a Rural Area' or item == 'Lives in rural area':
                    newItem = options['ruralStatus'][0]
                    newRow.append(newItem)
                elif item == 'Household does not live in a rural area' or item == 'Household Does Not Live in a Rural Area' or item == 'Does not live in rural area':
                    newItem = options['ruralStatus'][1]
                    newRow.append(newItem)

                # Client Case Status
                elif item == 'In-Process':
                    newItem = options['status'][1]
                    newRow.append(newItem)
                elif item == 'Suspended' or item == 'Ineligible':
                    newItem = options['status'][4]
                    newRow.append(newItem)
                elif item == 'Fulfilled':
                    newItem = options['status'][2]
                    newRow.append(newItem)
                elif item == 'Withdrew':
                    newItem = options['status'][3]
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
                # elif re.search(r'\d{1,4}(?P<delim>[.\-/])\d{1,2}(?P=delim)\d{1,4}', item):
                #     newItem = validate_dates(item)
                #     newRow.append(newItem)
                # else:
                #     newRow.append(item)
                
            # THE NUMBERS IN THE FOLLOWING ROWS COULD POTENTIALLY NEED UPDATED IF AGENCIES DIDN'T 
            # FOLLOW OUR EXACT TEMPLATE, CHECK NUMBERS BEFORE RUNNING
            # This will be a better way in the future to do all of this
            # Right now this just overwrites race to the proper item
            # if newRow[10] == 'c. Chose not to respond':
            #     newRow[10] = options['race']['k']
            # if newRow[18] == 'c. Chose not to respond':
            #     newRow[18] = options['incomeBand']['f']


            # *************************************************************************
            # UNCOMMENT IF YOU NEED TO SEPARATE THE HOUSE NUMBER FROM THE ADDRESSES
            # ENSURE THAT BEFORE YOU RUN MAKE THE STREET NUMBER COLUMN ON THE ORIGINAL
            # CSV DOCUMENT. EDIT AS NEEDED

            # This will break out the street numbers from the addresses
            # directions = ['N', 'S', 'E', 'W']

            # street_array = newRow[21].split()
            # if street_array:
            #     # street_direction 
            #     # street_numbers
            #     # newAddress

            #     if street_array[0][0] in directions:
            #         street_direction = street_array[0][0]
            #         street_numbers = street_array[0][1:]
            #         street_array[0] = street_direction
            #         newAddress = ' '.join(street_array)
            #     else:
            #         street_numbers = street_array[0]
            #         newAddress = ' '.join(street_array[1:])
            
            #     newRow[20] = street_numbers
            #     newRow[21] = newAddress
            

            w.writerow(newRow)


    # Check length of copy
    copyCount = get_length(outputFileName)

    if length == copyCount:
        return "Successful"
    else:
        return "There has been an error"