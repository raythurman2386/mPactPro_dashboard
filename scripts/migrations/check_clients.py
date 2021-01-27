import csv
import re
from utils import get_length, options, validate_dates

def check_clients(masterFile, outputFileName, length):
    # Work with the masterfile
    with open(masterFile) as master, open(outputFileName, 'w') as outfile:
        r = csv.reader(master)
        w = csv.writer(outfile)

        # Skip the old header
        next(r)

        # WRITE A NEW HEADER IF NEEDED TO MATCH WHAT IS NEEDED
        # With header names to match MSSQL Server
        w.writerow(['ClientID', 'ClientCaseStatus', 'ClientProgramEnrollment', 'ActiveStaff', 'ClientFirstName', 'ClientMiddleName', 'ClientLastName', 'DateOfBirth', 'Gender', 'Race', 'Ethnicity', 'VeteranStatus', 'ActiveMilitary', 'FirstTimeHomebuyer', 'HouseholdSize', 'CountyAmiIncomeLimit', 'HouseholdIncome', 'HouseholdIncomeBand', 'IntakeDate', 'StreetNumber', 'StreetName', 'ApartmentNumber', 'ClientCity', 'ClientCounty', 'ClientState', 'ClientZip', 'PrivacyOptOut', 'RuralAreaStatus', 'EnglishProficiencyLevel', 'BillToHud', '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h', '8i', '9a', '9b', '9c', '9d', '9e', '9f', '10a', '10b', '10c', '10d', '10e', '10f', '10g', '10h', '10i', '10j', '10k', '10l', '10m', 'PhoneNumberMobile', 'PhoneNumberWork', 'PhoneNumberHome', 'ImmigrationStatus', 'EmailHome', 'EmailWork', 'MaritalStatus', 'Disability', 'HouseholdType', 'Education', 'ReferalSource', 'LastContact', 'ActiveReportDateHUD', 'CompletedDate', 'InactiveDate'])

        # Writes the remaining rows to the file
        for row in r:
            # Changes to individuals will need done through here
            newRow = []
            
            # Add all items to a new row to alter
            for item in row:
                newRow.append(item)

            # THE NUMBERS IN THE FOLLOWING ROWS COULD POTENTIALLY NEED UPDATED IF AGENCIES DIDN'T 
            # FOLLOW OUR EXACT TEMPLATE, CHECK NUMBERS BEFORE RUNNING

            # ClientCaseStatus
            if newRow[1] == 'In-Process':
                newRow[1] = options['status'][1]
            elif newRow[1] == 'Fulfilled':
                newRow[1] = options['status'][2]
            elif newRow[1] == 'Suspended':
                newRow[1] = options['status'][4]
            # elif newRow[1] == '':
            #     newRow[1] = options['status'][]
            # elif newRow[1] == '':
            #     newRow[1] = options['status'][]
            # elif newRow[1] == '':
            #     newRow[1] = options['status'][]

            # Gender
            if newRow[6] == '1':
                newRow[6] = options['gender'][0]
            elif newRow[6] == '2':
                newRow[6] = options['gender'][1]

            # Race
            if newRow[7] == 'Native American/American Indian':
                newRow[7] = options['race']['a']
            elif newRow[7] == 'Black/African American':
                newRow[7] = options['race']['c']
            elif newRow[7] == 'White/Caucasian':
                newRow[7] = options['race']['e']
            elif newRow[7] == 'Hispanic/Latino':
                newRow[7] = options['race']['j']
            elif newRow[7] == 'Multi-Race':
                newRow[7] = options['race']['j']
            # elif newRow[7] == 'Not Reported':
            #     newRow[7] = options['race']['k']
            # elif newRow[7] == 'Not Reported':
            #     newRow[7] = options['race']['k']
            # elif newRow[7] == 'Not Reported':
            #     newRow[7] = options['race']['k']
            # elif newRow[7] == 'Not Reported':
            #     newRow[7] = options['race']['k']
            elif newRow[7] == 'Other':
                newRow[7] = options['race']['j']
            elif newRow[7] == 'Not Reported' or newRow[7] == '':
                newRow[7] = options['race']['k']

            # Ethnicity
            if newRow[8] == 'Hispanic or Latino':
                newRow[8] = options['ethnicity']['a']
            elif newRow[8] == 'Not Hispanic or Latino':
                newRow[8] = options['ethnicity']['b']
            elif newRow[8] == '':
                newRow[8] = options['ethnicity']['c']

            # HouseholdIncomeBand
            if newRow[13] == '<30%':
                newRow[13] = options['incomeBand']['a']
            elif newRow[13] == '30-49%':
                newRow[13] = options['incomeBand']['b']
            elif newRow[13] == '50-79%':
                newRow[13] = options['incomeBand']['e']
            elif newRow[13] == '80-100%':
                newRow[13] = options['incomeBand']['d']
            elif newRow[13] == '100%-120%' or newRow[13] == '>120%':
                newRow[13] = options['incomeBand']['e']
            elif newRow[13] == '':
                newRow[13] = options['incomeBand']['f']

            #Street Corrections
            # This will break out the street numbers from the addresses
            directions = ['N', 'S', 'E', 'W']

            street_array = newRow[16].split()
            if street_array:
                # street_direction 
                # street_numbers
                # newAddress

                if street_array[0][0] in directions:
                    street_direction = street_array[0][0]
                    street_numbers = street_array[0][1:]
                    street_array[0] = street_direction
                    newAddress = ' '.join(street_array)
                else:
                    street_numbers = street_array[0]
                    newAddress = ' '.join(street_array[1:])
            
                newRow[15] = street_numbers
                newRow[16] = newAddress

            # Rural Status
            if newRow[23] == 'Household Lives in a Rural Area':
                newRow[23] = options['ruralStatus'][0]
            elif newRow[23] == 'Household Does Not Live in a Rural Area':
                newRow[23] = options['ruralStatus'][1]
            elif newRow[23] == '':
                newRow[23] = options['ruralStatus'][2]
            
            # English Proficiency
            if newRow[24] == 'No English':
                newRow[24] = options['englishProficiency'][0]
            elif newRow[24] == 'English':
                newRow[24] = options['englishProficiency'][1]
            elif newRow[24] == '':
                newRow[24] = options['englishProficiency'][2]


            w.writerow(newRow)


    # Check length of copy
    copyCount = get_length(outputFileName)

    if length == copyCount:
        return "Successful"
    else:
        return "There has been an error"