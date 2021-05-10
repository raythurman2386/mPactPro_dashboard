from utils import case_options


def fix_case_data(case):
    try:
        # Return the client with all corrections
        if case[0] == 'Home Purchase':
            case[0] = case_options['caseType']['a']
        elif case[0] == 'Seeking Shelter or Homeless Srvcs':
            case[0] = case_options['caseType']['b']
        elif case[0] == 'Homeowner Services':
            case[0] = case_options['caseType']['c']
        elif case[0] == 'Mortgage Default/Early Delinquency':
            case[0] = case_options['caseType']['d']
        elif case[0] == 'Rental Counseling' or case[0] == 'Education':
            case[0] = case_options['caseType']['e']

        client_name_arr = case[9].split(' ')
        if len(client_name_arr) == 2:
            case[9] = client_name_arr[0]
            case[11] = client_name_arr[1]
        elif len(client_name_arr) == 3:
            case[9] = client_name_arr[0]
            case[10] = client_name_arr[1]
            case[11] = client_name_arr[2]
        elif len(client_name_arr) == 4:
            case[9] = client_name_arr[0]
            case[10] = client_name_arr[1]
            case[11] = client_name_arr[3]

        # Fix client case status
        if case[7] == 'In-Process':
            case[7] = case_options['clientCaseStatus']['a']
        elif case[7] == 'Suspended':
            case[7] = case_options['clientCaseStatus']['j']
        return case
    finally:
        return case
