from utils import options


def correct_data(client, address=False, tab='Client_Case'):
    try:
        # Split address if address=True
        if address:
            po_variations = ['PO', 'P.O.', 'P', 'HOMELESS', 'Alden', 'COMFORT', 'POBOX', 'NO', 'Homeless', 'Chicago',
                             'ss', 'NAOMI', 'Thresholds', 'NULL', 'Courtyard', 'YMCA', 'NA', 'CORNERSTONE', 'no',
                             'POBox', 'HOMLESS', 'SALVATION', 'POBOX368463', 'Homeless-']
            directions = ['N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE']
            if client[5] is not None:
                street_arr = client[5].split()
                # print(street_arr)
                # print(len(street_arr))
                if street_arr[0] not in po_variations:
                    street_num = street_arr[0]
                    new_address = ' '.join(street_arr[1:3])
                    client[4] = street_num
                    client[5] = new_address
                else:
                    client[5] = ' '.join(street_arr)

        # Correct Race index 10
        if client[10] == 'American Indian Alaskan Native' or client[10] == 908:
            client[10] = options['race']['a']

        elif client[10] == 'Asian' or client[10] == 901:
            client[10] = options['race']['b']

        elif client[10] == 'Black or African American' or client[10] == 'Black/African American' or client[10] == 895:
            client[10] = options['race']['c']

        elif client[10] == 'Native Hawaiian or Other Pacific Islander' or client[10] == 897:
            client[10] = options['race']['d']

        elif client[10] == 'White' or client[10] == 902:
            client[10] = options['race']['e']

        elif client[10] == 'American Indian Alaska Native and White' or client[10] == 'American Indian/Alaskan Native' or client[10] == 898:
            client[10] = options['race']['f']

        elif client[10] == 'Asian and White' or client[10] == 899:
            client[10] = options['race']['g']

        elif client[10] == 'Black or African American and White' or client[10] == 900:
            client[10] = options['race']['h']

        elif client[10] == 'American Indian or Alaska Native and Black or African American':
            client[10] = options['race']['i']

        elif client[10] == 'Other multiple race' or client[10] == 'Other' or client[10] == 'Central America' or \
                client[10] == 'Hispanic' or client[10] == 'Puerto Rican' or client[10] == 904 or client[10] == 907:
            client[10] = options['race']['j']

        elif client[10] is None or client[10] == 'Chose not to respond' or client[10] == 896:
            client[10] = options['race']['k']

        # Correct Ethnicity index 11
        if client[11] == 'Hispanic' or client[11] == 'Hispanic/Latino':
            client[11] = options['ethnicity']['a']
        elif client[11] == 'Not Hispanic' or client[11] == 'Non Hispanic/Non Latino':
            client[11] = options['ethnicity']['b']
        elif client[11] == 'Unknown' or client[11] is None or client[11] == 'Chose not to respond':
            client[11] = options['ethnicity']['c']

        # Correct English Proficiency index 12
        if client[12] == 'Is not English proficient' or client[12] == 'Household is Limited English Proficient':
            client[12] = options['englishProficiency']['a']
        elif client[12] == 'b . Household is not Limited English Proficient' or client[
                28] == 'Household is not Limited English Proficient':
            client[12] = options['englishProficiency']['b']
        elif client[12] is None or client[12] == 'Chose not to respond':
            client[12] = options['englishProficiency']['c']

        # Correct Case Type index 17
        if client[17] == 'Home Purchase':
            client[17] = options['caseType']['a']
        elif client[17] == 'Seeking Shelter or Homeless Srvcs':
            client[17] = options['caseType']['b']
        elif client[17] == 'Homeowner Services':
            client[17] = options['caseType']['c']
        elif client[17] == 'Mortgage Default/Early Delinquency':
            client[17] = options['caseType']['d']
        elif client[17] == 'Rental Counseling' or client[17] == 'Education':
            client[17] = options['caseType']['e']

        if tab == 'Client_Case':
            # Correct NOFA Grant index 26
            if client[26] == 'Activities for All Counseling and Education':
                client[26] = None

        if tab == 'Client_Class':
            # Correct Attended Status index 23
            pass

        return client
    finally:
        return client
