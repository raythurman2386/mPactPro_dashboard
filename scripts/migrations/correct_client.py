from utils import options


def fix_data(client):
    try:
        # Correct client case status index 1
        if client[1] == 'In-Process':
            client[1] = options['ClientCaseStatus']['b']
        elif client[1] == 'Fulfilled':
            client[1] = options['ClientCaseStatus']['c']
        elif client[1] == 'Suspended':
            client[1] = options['ClientCaseStatus']['e']

        # Correct Client Program Enrollment index 2
        if client[2] == 'Financial Capability Counseling':
            client[2] = options['ClientProgramEnrollment']['e']

        # Correct Gender if needed index 8
        if client[8] == 'M':
            client[8] = options['gender'][0]
        elif client[8] == 'Female' or client[8] == 'F':
            client[8] = options['gender'][1]
        elif client[8] == 'O':
            client[8] = None

        # Correct Race index 9
        if client[9] == 'American Indian Alaskan Native':
            client[9] = options['race']['a']

        elif client[9] == 'Asian':
            client[9] = options['race']['b']

        elif client[9] == 'c. c. Black or African American or African American' or client[9] == 'Black or African American':
            client[9] = options['race']['c']

        elif client[9] == 'Native Hawaiian or Other Pacific Islander':
            client[9] = options['race']['d']

        elif client[9] == 'White':
            client[9] = options['race']['e']

        elif client[9] == 'American Indian Alaska Native and White':
            client[9] = options['race']['f']

        elif client[9] == 'Asian and White':
            client[9] = options['race']['g']

        elif client[9] == 'Black or African American and White':
            client[9] = options['race']['h']

        elif client[9] == 'Other multiple race' or client[9] == 'Cuban' or client[9] == 'Central America' or \
            client[9] == 'Colombian' or client[9] == 'Puerto Rican' or client[9] == 'South American':
            client[9] = options['race']['j']

        elif client[9] is None or client[9] == 'Chose not to respond':
            client[9] = options['race']['k']

        # Correct Ethnicity index 10
        if client[10] == 'a.  Hispanic' or client[10] == 'Hispanic':
            client[10] = options['ethnicity']['a']
        elif client[10] == 'b.  Not Hispanic' or client[10] == 'Not Hispanic':
            client[10] = options['ethnicity']['b']
        elif client[10] is None:
            client[10] = options['ethnicity']['c']

        # Correct Income Band index 17
        if client[17] == '<30%' or client[17] == '1':
            client[17] = options['incomeBand']['a']
        elif client[17] == '30-49%' or client[17] == '2':
            client[17] = options['incomeBand']['b']
        elif client[17] == '50-79%' or client[17] == '3':
            client[17] = options['incomeBand']['c']
        elif client[17] == '80-100%' or client[17] == '4':
            client[17] = options['incomeBand']['d']
        elif client[17] == '100%-120%' or client[17] == '>120%' or client[17] == '5':
            client[17] = options['incomeBand']['e']
        elif client[17] == '' or client[17] == '6':
            client[17] = options['incomeBand']['f']

        # TODO: IF THE ADDRESS DOES NOT NEED CORRECTED COMMENT THIS OUT
        # Correct Street if needed
        # po_variations = ['PO', 'P.O.']
        # if client[20] is not None:
        #     street_arr = client[20].split()
        #     if street_arr[0] not in po_variations:
        #         street_num = street_arr[0]
        #         new_address = ' '.join(street_arr[1:])
        #         client[19] = street_num
        #         client[20] = new_address
        #     else:
        #         client[20] = ' '.join(street_arr)

        # Correct Rural Status index 27
        if client[27] == 'a. Household lives in a rural area' or client[27] == 'Household lives in a rural area':
            client[27] = options['ruralStatus']['a']
        elif client[27] == 'b. Household does not live in a rural area' or client[
            27] == 'Household does not live in a rural area':
            client[27] = options['ruralStatus']['b']
        elif client[27] is None:
            client[27] = options['ruralStatus']['c']

        # Correct English Proficiency index 28
        if client[28] == 'Is not English proficient' or client[28] == 'Household is Limited English Proficient':
            client[28] = options['englishProficiency']['a']
        elif client[28] == 'b . Household is not Limited English Proficient' or client[
            28] == 'Household is not Limited English Proficient':
            client[28] = options['englishProficiency']['b']
        elif client[28] is None:
            client[28] = options['englishProficiency']['c']

        # Remove dashes from phone number
        if client[60] is not None:
            if '-' in client[60]:
                phone_arr = client[60].split('-')
                client[60] = int(''.join(phone_arr))
            else:
                pass

        # Correct Marital Status index 64
        if client[64] == 'Single':
            client[64] = options['maritalStatus']['a']
        elif client[64] == 'Married':
            client[64] = options['maritalStatus']['b']
        elif client[64] == 'Divorced':
            client[64] = options['maritalStatus']['c']
        elif client[64] == 'Widowed':
            client[64] = options['maritalStatus']['e']
        elif client[64] is None:
            client[64] = None

        # Correct Household Type index 66
        if client[66] == 'Female-headed single parent household':
            client[66] = options['householdType']['a']
        elif client[66] == 'Male-headed single parent household':
            client[66] = options['householdType']['b']
        elif client[66] == 'Single Adult':
            client[66] = options['householdType']['c']
        elif client[66] == 'Married with children':
            client[66] = options['householdType']['e']
        elif client[66] == 'Married without children':
            client[66] = options['householdType']['f']
        elif client[66] == 'Other':
            client[66] = options['householdType']['g']

        # Correct Education index 67
        if client[67] == 'Junior High School' or client[67] == 'Elementary':
            client[67] = options['education']['a']
        elif client[67] == 'High School':
            client[67] = options['education']['b']
        elif client[67] == 'Junior College':
            client[67] = options['education']['c']
        elif client[67] == 'University':
            client[67] = options['education']['d']
        elif client[67] == 'Unknown':
            client[67] = options['education']['g']
        elif client[67] == 'Other':
            client[67] = options['education']['h']

        # Correct Referral Source index 68
        client[68] = None

        # Return the client with all corrections
        return client
    finally:
        return client
