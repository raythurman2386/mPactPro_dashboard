import csv
from utils import get_length, options


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
            # if newRow[6] == '1':
            #     newRow[6] = options['gender'][0]
            # elif newRow[6] == '2':
            #     newRow[6] = options['gender'][1]

            # Race
            if newRow[9] == 'Native American/American Indian' or newRow[9] == 'a.':
                newRow[9] = options['race']['a']
            elif newRow[9] == 'Black/African American' or newRow[9] == 'c.':
                newRow[9] = options['race']['c']
            elif newRow[9] == 'White/Caucasian' or newRow[9] == 'e.' or newRow[9] == 'e':
                newRow[9] = options['race']['e']
            elif newRow[9] == 'Hispanic/Latino':
                newRow[9] = options['race']['j']
            elif newRow[9] == 'Multi-Race':
                newRow[9] = options['race']['j']
            # elif newRow[9] == 'Not Reported':
            #     newRow[9] = options['race']['k']
            # elif newRow[9] == 'Not Reported':
            #     newRow[9] = options['race']['k']
            # elif newRow[9] == 'Not Reported':
            #     newRow[9] = options['race']['k']
            # elif newRow[9] == 'Not Reported':
            #     newRow[9] = options['race']['k']
            elif newRow[9] == 'Other' or newRow[9] == 'j.':
                newRow[9] = options['race']['j']
            elif newRow[9] == 'Not Reported' or newRow[9] == '':
                newRow[9] = options['race']['k']

            # Ethnicity
            if newRow[10] == 'Hispanic or Latino' or newRow[10] == 'a.':
                newRow[10] = options['ethnicity']['a']
            elif newRow[10] == 'Not Hispanic or Latino' or newRow[10] == 'b.':
                newRow[10] = options['ethnicity']['b']
            elif newRow[10] == '':
                newRow[10] = options['ethnicity']['c']

            # HouseholdIncomeBand
            if newRow[17] == '<30%' or newRow[17] == '1':
                newRow[17] = options['incomeBand']['a']
            elif newRow[17] == '30-49%' or newRow[17] == '2':
                newRow[17] = options['incomeBand']['b']
            elif newRow[17] == '50-79%' or newRow[17] == '3':
                newRow[17] = options['incomeBand']['e']
            elif newRow[17] == '80-100%' or newRow[17] == '4':
                newRow[17] = options['incomeBand']['d']
            elif newRow[17] == '100%-120%' or newRow[17] == '>120%' or newRow[17] == '5':
                newRow[17] = options['incomeBand']['e']
            elif newRow[17] == '' or newRow[17] == '6':
                newRow[17] = options['incomeBand']['f']

            #Street Corrections
            # This will break out the street numbers from the addresses
            # directions = ['N', 'S', 'E', 'W']

            # street_array = newRow[16].split()
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

            #     newRow[15] = street_numbers
            #     newRow[16] = newAddress

            # Rural Status
            if newRow[27] == 'Household Lives in a Rural Area' or newRow[27] == 'a.':
                newRow[27] = options['ruralStatus'][0]
            elif newRow[27] == 'Household Does Not Live in a Rural Area' or newRow[27] == 'b.':
                newRow[27] = options['ruralStatus'][1]
            elif newRow[27] == '' or newRow[27] == 'c.':
                newRow[27] = options['ruralStatus'][2]

            # # English Proficiency
            if newRow[28] == 'No English' or newRow[28] == 'b.':
                newRow[28] = options['englishProficiency'][0]
            elif newRow[28] == 'English' or newRow[28] == 'a.':
                newRow[28] = options['englishProficiency'][1]
            elif newRow[28] == '':
                newRow[28] = options['englishProficiency'][2]

            # Marital Status
            if newRow[64] == 'Unmarried':
                newRow[64] = options['maritalStatus']['a']
            # elif newRow[64] == '':
            #     pass

            # Household Type
            if newRow[66] == '1':
                newRow[66] = options['householdType']['a']
            elif newRow[66] == '2':
                newRow[66] = options['householdType']['b']
            elif newRow[66] == '3':
                newRow[66] = options['householdType']['c']
            elif newRow[66] == '4':
                newRow[66] = options['householdType']['d']
            elif newRow[66] == '5':
                newRow[66] = options['householdType']['e']
            elif newRow[66] == '6':
                newRow[66] = options['householdType']['f']
            elif newRow[66] == '7':
                newRow[66] = options['householdType']['g']

            # Referal Source
            if newRow[68] == '1':
                newRow[68] = options['referalSource']['a']
            elif newRow[68] == '2':
                newRow[68] = options['referalSource']['b']
            elif newRow[68] == '3':
                newRow[68] = options['referalSource']['c']
            elif newRow[68] == '4':
                newRow[68] = options['referalSource']['d']
            elif newRow[68] == '5':
                newRow[68] = options['referalSource']['e']
            elif newRow[68] == '6':
                newRow[68] = options['referalSource']['f']
            elif newRow[68] == '7':
                newRow[68] = options['referalSource']['g']
            elif newRow[68] == '8':
                newRow[68] = options['referalSource']['h']
            elif newRow[68] == '9':
                newRow[68] = options['referalSource']['i']
            elif newRow[68] == '10':
                newRow[68] = options['referalSource']['j']
            elif newRow[68] == '11':
                newRow[68] = options['referalSource']['k']

            w.writerow(newRow)


    # Check length of copy
    copyCount = get_length(outputFileName)

    if length == copyCount:
        return "Successful"
    else:
        return "There has been an error"
